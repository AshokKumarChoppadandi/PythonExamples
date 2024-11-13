from pyspark.sql import SparkSession
from pyspark.sql.types import *


def main():
    print("First PySpark Program from IntelliJ")
    input_file = "/input2.csv"
    spark = get_spark_session()
    df = read_data(spark=spark, input_file=input_file)
    df.printSchema()
    df.show()

    schema = get_schema()
    df2 = df.toDF(*schema)
    df2.printSchema()
    df2.show()


def get_spark_session():
    spark = SparkSession.builder.appName("WordCount").master("local[*]").getOrCreate()
    print('Spark Session object created - {}'.format(spark))
    return spark


def read_data(spark: SparkSession, input_file: str, is_header: bool = True, infer_schema: bool = True):
    df = spark.read.option("header", is_header).option("inferSchema", infer_schema).csv(input_file)
    return df


def get_schema():
    schema = StructType(
        [
            StructField("ID", IntegerType(), True),
            StructField("NAME", StringType(), True),
            StructField("AGE", IntegerType(), True),
            StructField("SALARY", IntegerType(), True),
            StructField("DEPT", IntegerType(), True)
        ]
    )
    return schema


if __name__ == '__main__':
    main()
