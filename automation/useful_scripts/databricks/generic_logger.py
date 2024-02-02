# Databricks notebook source
from datetime import datetime
import logging
import os

# COMMAND ----------

def applogger(logfile_name):
    current_date=datetime.now().strftime('%Y%m%d_%H%M')
    directory = '/tmp/' 
    logfilename= logfile_name +current_date+'.log'
    logfilePath=directory + logfilename

    logger = logging.getLogger('Logger')
    logger.setLevel(logging.INFO)

    fh=logging.FileHandler(logfilePath,mode='a')
    formatter=logging.Formatter('%(asctime)s %(name)s %(levelname)s %(lineno)d %(message)s')
    fh.setFormatter(formatter)
    
    sh = logging.StreamHandler()
    sh.setFormatter(formatter)
    
    if not logger.handlers:
        logger.addHandler(sh)
        logger.addHandler(fh)
      
    logger.info('Logger created')
    return logger,logfilePath,logfilename

def saveLogFile(adls_log_path, module_name, logfilePath, logfilename):
    currentTime = datetime.now()
    isPathExist = False
    
    create_log_dir = adls_log_path + module_name + "/"+ str(currentTime.year) + "/" + str(currentTime.month) +"/"+ str(currentTime.day)+"/"
    isPathExist = os.path.exists(create_log_dir)
    os.makedirs(create_log_dir,exist_ok=isPathExist)
    
    logging.shutdown()
    dbutils.fs.mv("file:"+logfilePath, create_log_dir+logfilename)


#Example to create logger
adls_log_path = <path to save the log file>
module_name = "Generic_Logger"
process_name = "log"
try:
    logfile_name = module_name + "_" + process_name + "_"
    logger,logfilePath,logfilename=applogger(logfile_name)
except Exception as e:
    logger.info("Error while creating logger object: \n{}".format(e))
    exit(1)
# Write in logger using. logger.info("value to log in log file")
# To stop the logger and save the log file in the log directory, run the below query
saveLogFile(adls_log_path, module_name, logfilePath, logfilename)
