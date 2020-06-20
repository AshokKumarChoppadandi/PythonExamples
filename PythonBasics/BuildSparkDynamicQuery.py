print("Hello world")

requiredColumns = ["id", "name", "test"]
dbName = "test_db"
tableName = "employee_text"
query1 = "select * from " + dbName + "." + tableName

tableData1 = spark.sql(query1)
tempTableName = "temp_table"
tableData1.createOrReplaceTempView(tempTableName)

tableColumns1 = tableData1.columns

finalColumns = ""

for column in requiredColumns:
    var = column + " as " + column if column in tableColumns1 else "-1 as " + column
    finalColumns += var + ", "


print(finalColumns)

finalSelectQuery = "select " + finalColumns[:-2] + " from " + dbName + "." + tableName





