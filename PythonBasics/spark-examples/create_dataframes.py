from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType, StringType

spark = SparkSession.builder.appName("Create Dataframes").master("local").getOrCreate()

'''
Creating a DataFrame from list provided the type of the elements i.e., Integers
'''

ages_list = [25, 18, 28, 32, 45, 33]

df1 = spark.createDataFrame(ages_list, 'int')
df1.show()

'''
Creating a DataFrame from list provided the type of the elements i.e., Integers
'''

df2 = spark.createDataFrame(ages_list, IntegerType())
df2.show()

'''
Creating a DataFrame from list provided the type of the elements i.e., Strings
'''

names = ['ABC', 'DEF', 'GHI', 'JKL', 'LMN']
df3 = spark.createDataFrame(names, 'string')
df3.show()

'''
Creating a DataFrame from list provided the type of the elements i.e., Strings
'''

df4 = spark.createDataFrame(names, StringType())
df4.show()

