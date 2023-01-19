# Create empty dataframe to store the databases and tables name
tables_df = spark.sql("show tables in default like 'XXX'") #default is the database

#Loop through all databases
for _ in spark.sql("show databases").collect():
  # we can also use  regex to filter out the databases name
  # e.g-  spark.sql("show databases like '*test*'")
  # above spark query will list out all the dababases which contains test in name
  #create a dataframe with list of tables from the database
  df = spark.sql(f"show tables in {_.databaseName}")
  #union the tables list dataframe with main dataframe 
  tables_df = tables_df.union(df)
  
#After the loop, show the results
tables_df.display()
