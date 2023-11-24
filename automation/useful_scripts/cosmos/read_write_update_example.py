cosmosEndpoint = "https://<cosmos_db_name>.documents.azure.com:443/"
cosmosMasterKey = "<key_to_access_cosmos_db>"
cosmosDatabaseName = "<database_name>"
cosmosContainerName = "<container_name>"

# configuration to write records in cosmos db using spark/databricks
write_config = {
'spark.cosmos.accountEndpoint': cosmosEndpoint,
'spark.cosmos.accountKey': cosmosMasterKey,
'spark.cosmos.database': cosmosDatabaseName,
'spark.cosmos.container': cosmosContainerName,
"spark.cosmos.read.inferSchema.enabled" : "true",
"spark.cosmos.write.strategy": "ItemOverwrite"
}

# configuration to read records from cosmos db using spark/databricks
read_config = {
  "spark.cosmos.accountEndpoint" : cosmosEndpoint,
  "spark.cosmos.accountKey" : cosmosMasterKey,
  "spark.cosmos.database" : cosmosDatabaseName,
  "spark.cosmos.container" : cosmosContainerName
}

# configuration to delete records from cosmos db
del_config = {
'spark.cosmos.accountEndpoint': cosmosEndpoint,
'spark.cosmos.accountKey': cosmosMasterKey,
'spark.cosmos.database': cosmosDatabaseName,
'spark.cosmos.container': cosmosContainerName,
'spark.cosmos.write.strategy': 'ItemDelete',
'spark.cosmos.write.bulk.enabled': 'true'
}


recordsToDelete = spark.read.format("cosmos.oltp").options(**read_config).option("spark.cosmos.read.inferSchema.enabled", "true")\
 .load()
# recordsToDelete dataframe will return data from cosmos db


recordsToDelete.write.format('cosmos.oltp').mode('append').options(**del_config).save()

df_to_insert_update_records = <some_data_which_needs_to_be_insert/update_in_cosmos>
# update will only work if id and pk(partition_key) columns are matching
df_to_insert_update_records.write.format('cosmos.oltp').mode('append').options(**insert_update_write_config).save()

