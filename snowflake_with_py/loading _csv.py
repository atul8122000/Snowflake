import snowflake.connector as sf

conn=sf.connect( 
    user='<USER>',
    password='<password>',
    account='<account>'
    )
print("Connection Created ")

def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    cursor.close()


try:
    sql = 'use role {}'.format('ACCOUNTADMIN')
    execute_query(conn, sql)

    sql = 'use database {}'.format('NEW')
    execute_query(conn, sql)

    sql = 'use warehouse {}'.format('NEW')
    execute_query(conn, sql)

    sql = 'use schema {}'.format('TESTSCHEMA')
    execute_query(conn, sql)

    try:
        sql = 'alter warehouse {} resume'.format('NEW')
        execute_query(conn, sql)
    except:
        pass

    sql = 'drop table if exists netflix'
    execute_query(conn, sql)

    sql = 'create table netflix(Username VARCHAR, ID INTEGER, First_name STRING, Last_name STRING)'
    execute_query(conn, sql)

    sql = 'drop stage if exists data_stage'
    execute_query(conn, sql)

    sql = 'create stage data_stage file_format = (type = "csv" field_delimiter = "," skip_header = 1)'
    execute_query(conn, sql)

    csv_file = '/home/abc/Desktop/sf/sf/data.csv'
    sql = "PUT file://" + csv_file + " @DATA_STAGE auto_compress=true"
    execute_query(conn, sql)

    sql = 'copy into netflix from @DATA_STAGE/data.csv file_format = (type = "csv" field_delimiter = "," skip_header = 1)' \
          'ON_ERROR = "CONTINUE" '
    execute_query(conn, sql)



    sql = 'select * from "NEW"."TESTSCHEMA"."NETFLIX"'
    cursor = conn.cursor()
    cursor.execute(sql)
    for c in cursor:
        print(c)

except Exception as e:
    print(e)