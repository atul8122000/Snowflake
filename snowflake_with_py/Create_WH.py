from genericpath import exists
import snowflake.connector


############## SET CONECTION TO SNOWFLACK ######################
conn = snowflake.connector.connect(
    user='<USER>',
    password='<password>',
    account='<account>'
    )
print("Connected sucessfully")


############## DROP WAREHOUSE ######################
# conn.cursor().execute("DROP WAREHOUSE IF EXISTS new")
# print(" WAREHOUSE DROPED SUCSESSFULY")


############# CREATE WAREHOUSE ######################
conn.cursor().execute("CREATE WAREHOUSE IF NOT EXISTS new")
print(" WAREHOUSE CREATED SUCSESSFULY")


############# USE WAREHOUSE ######################
conn.cursor().execute("USE WAREHOUSE tiny_warehouse_mg")
print(conn," WAREHOUSE USED  SUCSESSFULY")


############# CREATE DATABASE ######################
conn.cursor().execute("CREATE DATABASE IF NOT EXISTS new")
print(" DATABASE CREATED SUCSESSFULY")


############# USE DATABASE ######################
conn.cursor().execute("USE DATABASE new")
print(" DATABASE USED  SUCSESSFULY")


############# CREATE AND USE SCHEMA ######################
conn.cursor().execute("CREATE SCHEMA IF NOT EXISTS testschema")
conn.cursor().execute("USE SCHEMA new.testschema")
print(" SCHEMA CREATED SUCSESSFULY")


############# USED SCHEMA WITH DB NAME ######################
# conn.cursor().execute("USE SCHEMA MY_DB.PUBLIC")
# print(" SCHEMA USED SUCSESSFULY")


############# CREATE TABLE ######################
conn.cursor().execute(
    "CREATE OR REPLACE TABLE "
    "test_table(col1 integer, col2 string)")
print(" TABLE CREATED SUCSESSFULY")


############# INSERT DATA ######################
conn.cursor().execute(
    "INSERT INTO test_table(col1, col2) "
    "VALUES(123, 'test string1'),(456, 'test string2')")
print(" DATA INSERTED SUCSESSFULY")

############# QUERY DATA ######################
for (col1, col2) in conn.cursor().execute("SELECT col1, col2 FROM test_table"):
	print('{0}, {1}'.format(col1, col2))


############## CLOSE CONNECTION ######################
# conn.close()
# print("Connection closed sucessfully")
