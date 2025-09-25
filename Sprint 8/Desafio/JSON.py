import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import explode, concat_ws
from datetime import datetime

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

job = Job(glueContext)
job.init(args['JOB_NAME'], args)

caminho_json = "s3://desafiovictor/Raw/Local/TMDB/JSON/2024/12/30/"

df = spark.read.option("multiline", "true").json(caminho_json)

df.printSchema()

df_exploded = df.withColumn("pais", explode(df["paises_de_origem"]))

data_atual = datetime.now()
ano_atual = data_atual.year
mes_atual = data_atual.month
dia_atual = data_atual.day
caminho_parquet = f"s3://desafiovictor/trusted/tmdb/api/movies/{ano_atual}/{mes_atual:02}/{dia_atual:02}/"

df_exploded.write.mode("overwrite").parquet(caminho_parquet)

job.commit()
