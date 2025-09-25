# Desafio: Processamento de Dados com AWS Glue e PySpark

## Objetivo do Desafio
Este desafio consistiu em processar e transformar grandes conjuntos de dados armazenados no S3 utilizando o **AWS Glue** com **PySpark**. Os dados vieram de arquivos CSV e JSON e foram transformados em **Parquet** para melhor desempenho e otimização.

------------------------------------------------------------------------------------------------

## Tarefas Realizadas

### 1. Processamento de Arquivos CSV
#### **Entrada**
- Local: `s3://desafiovictor/Raw/Local/CSV/Movies/2024/12/13/movies.csv`
- Formato: CSV com delimitador `|`.

#### **Transformações**
- Filtros aplicados:
  - Apenas filmes do gênero "War".
  - `anoLancamento` entre 1945 e 1955.
  - `notaMedia` presente e diferente de 0.

#### **Saída**
- Local: `s3://desafiovictor/trusted/local/csv/movies/filtrados/`
- Formato: Parquet.

[codigo_csv](../Desafio/CSV.py)

------------------------------------------------------------------------------------------------

### 2. Processamento de Arquivos JSON
#### **Entrada**
- Local: `s3://desafiovictor/Raw/Local/TMDB/JSON/2024/12/30/`
- Formato: JSON multilinha.

#### **Transformações**
- Explosão de arrays no campo `paises_de_origem` para normalizar os dados.
- Conversão para formato Parquet com organização por data de execução.

#### **Saída**
- Local: `s3://desafiovictor/trusted/tmdb/api/movies/{ano}/{mês}/{dia}/`
- Formato: Parquet.

[Codigo_json](../Desafio/JSON.py)

------------------------------------------------------------------------------------------------

## Resultados

### 1. Arquivos CSV
- Filmes do gênero "War" com notas válidas no intervalo de anos especificado.
- Dados otimizados no formato Parquet para melhor performance.

![Imagem](../Evidencias/Evidencia%20Desafio/Job_csv_sucesso.png)

### 2. Arquivos JSON
- Normalização dos arrays no campo `paises_de_origem`.
- Organização em estrutura Parquet no S3, pronta para análise.

![Imagem](../Evidencias/Evidencia%20Desafio/job_json_sucesso.png)

---

## Próximos Passos
1. **Consulta no Athena**:
   - Configurar um **Crawler** para catalogar os dados no Glue Data Catalog.
   - Realizar consultas SQL no Athena para validação e análises 

### Crawler
[Imagem](../Evidencias/Evidencia%20Desafio/Crawlers.png)

### Tables
![Imagem](../Evidencias/Evidencia%20Desafio/Crwaler_CSV.png)
![Imagem](../Evidencias/Evidencia%20Desafio/Crawler_json.png)   