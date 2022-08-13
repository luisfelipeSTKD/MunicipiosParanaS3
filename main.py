# imports

import boto3
import os
import wget
import pandas as pd

# Download do csv

def download():

    os.mkdir('./data')
    
    url = 'https://www.gov.br/receitafederal/dados/municipios.csv'

    local_file = './data/'

    d = wget.download(url, local_file)

    return d

# Carregamento do dataset e filtragem da coluna UF por PR

def selecionaPR():

    global data_PR

    data_raw = pd.read_csv('./data/municipios.csv', encoding='ISO-8859-1', sep=';')

    # Aproveitei e renomeei as colunas para facilitar futuras consultas

    data_raw = data_raw.rename(columns={'CÓDIGO DO MUNICÍPIO': 'cod_mun', 'NOME DO MUNICÍPIO': 'nome_mun'})

    data_PR = data_raw[data_raw['UF'] == 'PR']

    return data_PR

# Salva os dados filtrados em um novo arquivo csv

def salvaPR():
    csv_PR = data_PR.to_csv('data/municipiosPR.csv', index=False)
    return csv_PR

# Chamada das funções

download()
selecionaPR()
salvaPR()

# Serviço AWS S3

s3 = boto3.resource('s3')

# Upload do arquivo tratado

data_upload = open('./data/municipiosPR.csv', 'rb')
# s3.Bucket('test-municipios').put_object(Key='./data/municipiosPR.csv', Body=data_upload)
