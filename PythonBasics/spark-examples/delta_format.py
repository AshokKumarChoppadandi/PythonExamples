from pyspark.sql import SparkSession
from delta import *

packages = ["io.delta:delta-spark_2.12:3.2.0"]

builder = SparkSession.builder.appName("Delta Read and Write Operations").master("local") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \

spark = configure_spark_with_delta_pip(builder, extra_packages=packages).getOrCreate()

input_file = "C:\\Users\\lenovo\\IdeaProjects\\PythonExamples\\PythonBasics\\input2.csv"
df1 = spark.read.option("header", True).option("inferSchema", True).csv(input_file)

df1.printSchema()
df1.show()

output_dir = "C:\\Users\\lenovo\\IdeaProjects\\PythonExamples\\PythonBasics\\delta_output"

print("Started writing output data in Delta format")
df1.write.mode("overwrite").format("delta").save(output_dir)
print("Writing output data in Delta format is completed successfully")

input_data_dir = "C:\\Users\\lenovo\\IdeaProjects\\PythonExamples\\PythonBasics\\delta_output"

print("Reader data in Delta format")
df2 = spark.read.format("delta").load(input_data_dir)

df2.printSchema()
df2.show()
