import json
import urllib.request
import boto3
from datetime import datetime

API_KEY = "Chave"
BASE_URL = "https://api.themoviedb.org/3"
GENRE_ID = "10752"
START_YEAR = 1945
END_YEAR = 1955

def fetch_movies(api_key, genre_id, start_year, end_year):
    movies = []
    for year in range(start_year, end_year + 1):
        url = f"{BASE_URL}/discover/movie?api_key={api_key}&with_genres={genre_id}&primary_release_year={year}&language=pt-BR"
        
        try:
            with urllib.request.urlopen(url) as response:
                data = json.load(response)
                movies.extend(data.get("results", []))
        except urllib.error.URLError as e:
            print(f"Erro ao fazer a requisição para o ano {year}: {e}")
    return movies

def get_movie_country(api_key, movie_id):
    url = f"{BASE_URL}/movie/{movie_id}?api_key={api_key}&language=pt-BR"
    
    try:
        with urllib.request.urlopen(url) as response:
            data = json.load(response)
            countries = data.get("production_countries", [])
            return [country["name"] for country in countries] if countries else ["Desconhecido"]
    except urllib.error.URLError as e:
        print(f"Erro ao obter o país do filme {movie_id}: {e}")
        return ["Desconhecido"]

def save_to_s3(data, bucket_name, file_path):
    s3 = boto3.client('s3')
    s3.put_object(Bucket=bucket_name, Key=file_path, Body=json.dumps(data, ensure_ascii=False))
    print(f"Arquivo JSON salvo no S3 em {file_path}")

def lambda_handler(event, context):
    try:
        current_date = datetime.now()
        year = current_date.year
        month = current_date.month
        day = current_date.day
        file_name = f"filmes_de_guerra.json"
        file_path = f"Raw/Local/TMDB/JSON/{year}/{month}/{day}/{file_name}"
        
        print(f"Buscando filmes de guerra entre {START_YEAR} e {END_YEAR}...")
        movies = fetch_movies(API_KEY, GENRE_ID, START_YEAR, END_YEAR)
        print(f"Total de filmes encontrados: {len(movies)}")

        movie_data = []
        for movie in movies:
            title = movie["title"]
            release_date = movie.get("release_date", "N/A")
            year = release_date.split("-")[0] if release_date != "N/A" else "N/A"
            overview = movie.get("overview", "Descrição não disponível.")
            rating = movie.get("vote_average", "N/A")
            movie_id = movie["id"]
            countries = get_movie_country(API_KEY, movie_id)
            
            movie_data.append({
                "titulo": title,
                "ano": year,
                "descricao": overview,
                "avaliacao": rating,
                "paises_de_origem": countries
            })

        save_to_s3(movie_data, "desafiovictor", file_path)
        print(f"Processo concluído com sucesso!")

    except Exception as e:
        print(f"Erro: {e}")
        raise e