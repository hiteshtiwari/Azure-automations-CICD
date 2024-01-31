from pyspark.sql import SparkSession
from pyspark.sql.functions import concat_ws, sha2

# Create a Spark session
spark = SparkSession.builder.appName("UniqueKeyGeneration").getOrCreate()

# Sample data
data = [("John", "Doe", "12345", "New York", "USA"),
        ("Jane", "Smith", "67890", "San Francisco", "USA"),
        ("Alice", "Johnson", "54321", "London", "UK")]

# Define your schema
columns = ["first_name", "last_name", "zipcode", "city", "country"]
schema = ["string"] * len(columns)

# Create a DataFrame
df = spark.createDataFrame(data, schema=columns)

# Concatenate the values from the 5 columns
concatenated_columns = concat_ws("", *df.columns)

# Apply SHA-2 hash function to generate a unique key
df = df.withColumn("unique_key", sha2(concatenated_columns, 256))

# Show the result
df.show(truncate=False)
