import pandas as pd
from loguru import logger
import json
from datetime import datetime
import boto3

def read_config(env):
    """
    This is used to read the config file as json object
    :return: config
    """
    with open("../config/config.json") as f:
        config = json.load(f)
    return config[env.lower()]


def logging():
    """
    This function is used to log all config details
    :return: logger object
    """
    logger.add("../logs/load_data_to_kinesis.log",
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


def read_data(env):
    """
    This UDF is used to read excel dataset and stores the data as pandas dataframe in memory
    :return: Boolean Object
    """
    config = read_config(env)
    file_type = config['File_Type']
    file_name = config['Name_of_the_file']
    sheet_name = config['sheet_name']
    try:
        if file_type.lower() == 'xls':
            data = pd.read_excel("../data/" + file_name,
                                 sheet_name=sheet_name
                                 )
            logger.info("First 5 rows are shown below")
            logger.info(data.head())
            return data
    except Exception as e:
        print(e)
        logger.exception(e)
        exit(1)


def load_data_to_kinesis(data, env):
    try:
        config = read_config(env)
        shard_name = config['Shard_name']
        kinesis_client = boto3.client('kinesis', region_name='us-east-1')
        logger.info('Boto3 client to kinesis made successfully')
        for i, j in data.iterrows():
            # print(i)  # prints the index number
            # print(j)   # prints that row as series
            # print(j['Row ID'])   # prints the corresponding row id value
            # print(data.iloc[i, :].tolist())
            data_string = '|'.join([str(element) for element in data.iloc[i, :].tolist()])
            partition_key = '{}'.format(j['Row ID'])
            kinesis_client.put_record(Data=data_string,
                                      StreamName=shard_name,
                                      PartitionKey=partition_key)
        logger.info('Data Pushed into kinesis')
        return True
    except Exception as e:
        print(e)
        logger.exception(e)
