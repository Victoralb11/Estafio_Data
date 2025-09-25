import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import upper, col

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

s3_path = "s3://exerciciovictor7/lab-glue/input/"
dataframe = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [s3_path]},
    format="csv",
    format_options={"withHeader": True}
)

dataframe.printSchema()

df_spark = dataframe.toDF()
df_spark = df_spark.withColumn("nome", upper(df_spark["nome"]))

print(f"Total de linhas: {df_spark.count()}")

df_grouped = df_spark.groupBy("ano", "sexo").count().orderBy("ano", ascending=False)
df_grouped.show()

nome_feminino = df_spark.filter(col("sexo") == "F").groupBy("nome", "ano").count().orderBy(col("count").desc()).first()
nome_masculino = df_spark.filter(col("sexo") == "M").groupBy("nome", "ano").count().orderBy(col("count").desc()).first()

print(f"Nome feminino mais comum: {nome_feminino}")
print(f"Nome masculino mais comum: {nome_masculino}")

df_yearly = df_spark.groupBy("ano").count().orderBy("ano").limit(10)
df_yearly.show()

output_path = "s3://exerciciovictor7/lab-glue/frequencia_registro_nomes_eua/"
df_spark.write.mode("overwrite").partitionBy("sexo", "ano").json(output_path)

job.commit()