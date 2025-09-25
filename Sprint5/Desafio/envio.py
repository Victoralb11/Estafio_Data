import boto3
import os
import logging

logging.basicConfig(level=logging.DEBUG)

os.environ['AWS_ACCESS_KEY_ID'] = 'codigo_id'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'chave_de_acesso_secreta'
os.environ['AWS_SESSION_TOKEN'] = 'token de acesso'
s3 = boto3.client('s3')


bucket_name = 'desafio5'

arquivos_para_subir = [
    'teste_filtro_desafio.py',
    'dados_filtrados.csv',
    'tb_geral.csv',
]


print("Arquivos no diretório:", os.listdir())

def verificar_upload(arquivo):
    try:
       
        s3.upload_file(arquivo, bucket_name, arquivo)
        print(f"Arquivo {arquivo} carregado com sucesso!")
    except Exception as e:
        print(f"Erro ao carregar o arquivo {arquivo}: {e}")

for arquivo in arquivos_para_subir:
    if arquivo in os.listdir(): 
        print(f"Iniciando o upload do arquivo {arquivo}...")
        verificar_upload(arquivo) 
    else:
        print(f"O arquivo {arquivo} não foi encontrado no diretório.")