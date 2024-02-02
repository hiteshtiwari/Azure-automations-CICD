import logging
import concurrent.futures

# Set up logging
logger = logging.getLogger("data_writer")
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

# Define a function to write data to a specific table
def write_data_to_table(table):
    try:
        # Perform your data processing and create the DataFrame to be written
        data_df = ...

        # Write the DataFrame to the table
        data_df.write.format("delta").mode("overwrite").saveAsTable(table)

        # Log success message
        logger.info(f"Data writing to {table} completed successfully.")
    except Exception as e:
        # Log error message
        logger.error(f"Error writing to {table}: {str(e)}")

# Configure the tables you want to write data to
table_list = ["table1", "table2", "table3"]

# Create a ThreadPoolExecutor for parallel execution
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Submit each table write task to the executor
    futures = [executor.submit(write_data_to_table, table) for table in table_list]

    # Wait for all tasks to complete
    concurrent.futures.wait(futures)

# All write tasks have completed
logger.info("Data writing to multiple tables completed.")
