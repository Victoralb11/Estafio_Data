import boto3
import os
import logging
from datetime import datetime

logging.basicConfig(level=logging.DEBUG)

os.environ['AWS_ACCESS_KEY_ID'] = 'Chave de acesso'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'Chave secreta'
os.environ['AWS_SESSION_TOKEN'] = 'Token de sessão'

s3 = boto3.client('s3')

bucket_name = 'desafiovictor'

try:
    
    s3.create_bucket(
        Bucket=bucket_name
    )
    print(f"Bucket {bucket_name} criado com sucesso!")
except s3.exceptions.BucketAlreadyExists as e:
    print(f'O bucket {bucket_name} já existe.')

data_atual = datetime.now().strftime('%Y/%m/%d')

caminho_pasta_movies = f'Raw/Local/CSV/Movies/{data_atual}/movies.csv'
caminho_pasta_series = f'Raw/Local/CSV/Series/{data_atual}/series.csv'

arquivo_movies = '/data/movies.csv'
arquivo_series = '/data/series.csv'

try:
    s3.upload_file(arquivo_movies, bucket_name, caminho_pasta_movies)
    s3.upload_file(arquivo_series, bucket_name, caminho_pasta_series)
    print(f"Arquivos enviados com sucesso para {bucket_name}/{caminho_pasta_movies} e {bucket_name}/{caminho_pasta_series}")
except Exception as e:
    print(f"Erro ao enviar os arquivos: {e}")

