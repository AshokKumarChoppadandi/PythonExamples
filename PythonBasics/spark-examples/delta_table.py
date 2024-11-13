from delta import configure_spark_with_delta_pip
from pyspark.sql import SparkSession
from delta.tables import *

packages = ["io.delta:delta-spark_2.12:3.2.0"]


builder = SparkSession.builder.appName("Delta Read and Write Operations").master("local") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")

spark = configure_spark_with_delta_pip(builder, extra_packages=packages).getOrCreate()

input_data_dir = "C:\\Users\\lenovo\\IdeaProjects\\PythonExamples\\PythonBasics\\delta_output"

'''
print("Reader data in Delta format")
df1 = spark.read.format("delta").load(input_data_dir)

df1.printSchema()
df1.show()
'''

table = DeltaTable.forPath(spark, input_data_dir)
table.toDF().show()

