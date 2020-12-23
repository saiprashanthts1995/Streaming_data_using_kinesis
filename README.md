# Streaming_data_using_kinesis
This repository is used to load streaming data to kinesis and use kinesis firehose to load data into s3

## Process of Loading streaming data into S3
1. I have written a code in python which takes source file of format .xls and loads the data as pandas dataframe
2. Pandas dataframe is dumped as streaming data into kinesis stream
3. Kinesis Data firehose is created which takes data from kinesis shard and loads the data into s3

### to install python3 and packages in EC2 isntance
`sudo yum install python3`
`python3 -m pip install -r requirement.txt`

To get list of installed packages, execute the following command
`python3 -m pip freeze >> requirement.txt`

## Below section shows the list of images obtained from AWS is shown below

1. ![AWS_ROLE](https://github.com/saiprashanthts1995/Streaming_data_using_kinesis/blob/main/images/EC2_Kinesis_ROle.PNG)
When EC2 instance is created make sure to create an role and attach that role to EC2 instance. SO in this fashion, We will be able to interact with kinesis from EC2 Instance
2. ![Kinesis_SHard](https://github.com/saiprashanthts1995/Streaming_data_using_kinesis/blob/main/images/creation_of_shard.PNG)
Above image shows the Kinesis stream created to load data into kinesis stream by provisioning a single shard
3. ![Kinesis_Data_Firehose](https://github.com/saiprashanthts1995/Streaming_data_using_kinesis/blob/main/images/KDF.PNG)
Above image represents the created Kinesis data firehose whose source is Kinesis stream and target is S3
4. ![Data_Present_In_S3](https://github.com/saiprashanthts1995/Streaming_data_using_kinesis/blob/main/images/data_present_in_s3.PNG) 
Picture which is present above represents the output data loaded from Kinesis fire hose.    
