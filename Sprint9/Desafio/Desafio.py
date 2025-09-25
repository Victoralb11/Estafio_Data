import sys
from pyspark.sql import functions as F
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

parquet_csv_path = "s3://desafiovictor/trusted/local/csv/movies/filtrados/"
parquet_json_path = "s3://desafiovictor/trusted/tmdb/api/movies/2025/01/24/"
refined_output_path = "s3://desafiovictor/refined/"

csv_df = spark.read.format("parquet").load(parquet_csv_path)
json_df = spark.read.format("parquet").load(parquet_json_path)

json_df = json_df.withColumnRenamed("genero", "genero_json")
csv_df = csv_df.withColumnRenamed("genero", "genero_csv")

json_df = json_df.withColumn("ano_lancamento", F.year(F.to_date(F.col("ano"), "yyyy-MM-dd")))

dim_generos = csv_df.select("id", "genero_csv").withColumn(
    "genero", F.explode(F.split(F.col("genero_csv"), ","))
).select("id", "genero").distinct()

dim_paises = json_df.select("id", "paises_de_origem").withColumn(
    "pais", F.explode(F.col("paises_de_origem"))
).select("id", "pais").distinct()

dim_filmes = csv_df.select(
    "id", "tituloPincipal", "tituloOriginal", "anoLancamento", "tempoMinutos", "notaMedia"
).withColumnRenamed("tituloPincipal", "titulo_principal") \
 .withColumnRenamed("tituloOriginal", "titulo_original") \
 .withColumnRenamed("anoLancamento", "ano_lancamento") \
 .withColumnRenamed("tempoMinutos", "duracao_minutos") \
 .withColumnRenamed("notaMedia", "nota_media")

fato_df = csv_df.join(
    json_df, on="id", how="left"
).select(
    csv_df["id"],
    csv_df["tituloPincipal"].alias("titulo_principal"),
    csv_df["anoLancamento"].alias("ano_lancamento"),
    csv_df["notaMedia"].alias("nota_media"),
    csv_df["numeroVotos"].alias("numero_votos"),
    json_df["descricao"],
    json_df["genero_json"],
    json_df["paises_de_origem"],
    json_df["origem"],
    json_df["avaliacao"],
    json_df["data_lancamento"]
)

dim_generos.write.mode("overwrite").parquet(f"{refined_output_path}/dim_generos/")
dim_paises.write.mode("overwrite").parquet(f"{refined_output_path}/dim_paises/")
dim_filmes.write.mode("overwrite").parquet(f"{refined_output_path}/dim_filmes/")
fato_df.write.mode("overwrite").parquet(f"{refined_output_path}/fato_filmes/")

job.commit()