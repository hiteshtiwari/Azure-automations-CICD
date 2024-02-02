# Databricks notebook source
from concurrent.futures import ThreadPoolExecutor

# COMMAND ----------

class NotebookData:
    
     def __init__(self, path, timeout, parameters=None, retry=0):
        self.path = path
        self.timeout = timeout
        self.parameters = parameters
        self.retry = retry
     
     def submitNotebook(notebook):
        print("Running notebook %s" % notebook.path)
        try:
            if (notebook.parameters):
                return dbutils.notebook.run(notebook.path, notebook.timeout, notebook.parameters)
            else:
                return dbutils.notebook.run(notebook.path, notebook.timeout)
        except Exception:
             if notebook.retry < 1:
                raise
        print("Retrying notebook %s" % notebook.path)
        notebook.retry = notebook.retry - 1
        submitNotebook(notebook)
        

# COMMAND ----------

def parallelNotebooks(notebooks, numInParallel):
   # If you create too many notebooks in parallel the driver may crash when you submit all of the jobs at once. 
   # This code limits the number of parallel notebooks.
    with ThreadPoolExecutor(max_workers=numInParallel) as ec:
        return [ec.submit(NotebookData.submitNotebook, notebook) for notebook in notebooks]

notebooks = []
for num, fol in enumerate(folders):
    notebooks.append(NotebookData("./<Notebook_file>", 0, {'param1':'value1', 'param2':'value2'}))

res = parallelNotebooks(notebooks, 3) # 3 is the number to run parallel notebooks
result = [i.result(timeout=12800) for i in res]
