import pandas as pd
from loguru import logger
import json
from datetime import datetime


def read_config():
    """
    This is used to read the config file as json object
    :return: config
    """
    with open("../config/config.json") as f:
        config = json.load(f)
    return config


def logging():
    """
    This function is used to log all config details
    :return: logger object
    """
    logger.add("../logs/",
               level="INFO",
               retention="10 days",
               rotation="10 days")
    return logger


def timeit(method1):
    """
    UDF to find the time each function takes to execute
    :param method1: function method
    :return: decorator function
    """
    def wrapper(*args, **kwargs):
        try:
            start_ts = datetime.now()
            result = method1(*args, **kwargs)
            end_ts = datetime.now()
            print("Total time taken is {}".format(end_ts-start_ts))
            logger.info("Total time taken is {}".format(end_ts-start_ts))
            return result
        except Exception as e:
            print(e)
            exit(1)
    return wrapper


def read_data():
    """
    This UDF is used to read excel dataset and stores the data as pandas dataframe in memory
    :return: Boolean Object
    """
    config = read_config()
    file_type = config['File_Type']
    file_name = config['Name_of_the_file']
    sheet_name = config['sheet_name']
    try:
        if file_type.upper() == 'xls':
            data = pd.read_excel(file_name,
                                 sheet_name=sheet_name
                                 )
            logger.info("First 5 rows are shown below")
            logger.info(data.head())
            return True
    except Exception as e:
        print(e)
        exit(1)


def load_data_to_kinesis():
    pass

