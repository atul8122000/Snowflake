import snowflake.connector as sf

conn=sf.connect(
    user='<USER>',
    password='<password>',
    account='<account>'
    )
print("Connection Created ")

conn.cursor().execute("create or replace stage my_ext_unload_stage url='s3://unload/files/' storage_integration = s3_int file_format = my_csv_unload_format;")
print("Stage Created")

conn.cursor().execute("copy into s3://mybucket/unload/ from mytable storage_integration = s3_int;")
print("Data unloaded sucessfully")


