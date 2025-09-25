import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

job = Job(glueContext)
job.init(args['JOB_NAME'], args)

caminho_csv = "s3://desafiovictor/Raw/Local/CSV/Movies/2024/12/13/movies.csv"

df = spark.read.option("header", "true").option("delimiter", "|").csv(caminho_csv)

print("Colunas no DataFrame:", df.columns)

df.printSchema()

df = df.withColumnRenamed("genero ", "genero")

df_filtrado = df.filter(
    (df['genero'] == "War") & 
    (df['anoLancamento'].isNotNull()) & 
    (df['notaMedia'].isNotNull()) & 
    (df['notaMedia'] != 0) & 
    (df['anoLancamento'] >= 1945) & 
    (df['anoLancamento'] <= 1955)
)

df_filtrado.show()

caminho_trusted = "s3://desafiovictor/trusted/local/csv/movies/filtrados/"
df_filtrado.write.mode("overwrite").parquet(caminho_trusted)

job.commit()