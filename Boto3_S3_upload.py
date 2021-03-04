import boto3
import os

#create s3 object
s3=boto3.client('s3')

path="C:/Users/AsusPC/Desktop/Saint Peter's University Note/DS 530 Big data and data management/Final Project/ZAGDB"

#Create  bucket
s3.create_bucket(Bucket='ds530-aws-zagdb',CreateBucketConfiguration={'LocationConstraint':'us-east-2'})

for i in os.listdir(path):
    # file location,bucket name, file name
    s3.upload_file(os.path.join(path,i),'ds530-aws-zagdb',i)