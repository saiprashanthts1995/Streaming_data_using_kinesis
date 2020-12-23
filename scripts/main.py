__Author__ = "Sai Prashanth Thalanayar Swaminathan"
__email__ = "saiprashanthts@gmail.com"
__purpose__ = "To load data to kinesis using python"

from utils import logging, timeit, read_data, load_data_to_kinesis, read_config, load_data_to_kinesis
import argparse
import boto3


@timeit
def run(env):
    logger.infof
    print(read_config(env))
    data = read_data(env)
    load_data_to_kinesis(data,env)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="to load data to kinesis",
        prog="main.py")
    parser.add_argument("--env",
                        "-e",
                        dest="env",
                        required=True,
                        choices=['dev', 'qa'],
                        help=" decide on the environment to load the data"
                        )
    args = parser.parse_args()
    logger = logging()
    env = args.env
    print(args.env)
    logger.info('Process of loading data is ')
    logger.info("The environment we are going to load is {}".format(env))
    run(env)