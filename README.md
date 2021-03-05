# AWS_Redshift

Use python to extract file from database and upload it into AWS S3.

Create the redshift cluster in AWS and use copy command to tranfer the data from S3 to Redshift Cluster

We need psycopg2 and boto3 to perform the data transfer automation.

Follow the steps in:
https://docs.aws.amazon.com/redshift/latest/gsg/rs-gsg-create-sample-db.html
to create redshift cluster and database ( write down your username and password).

Use Python to extract the data from Homeaway or ZAGDB dimensional data to multiple files

Write a python module to upload the file into S3

Load data into redshift by using copy command

![image](https://user-images.githubusercontent.com/58495173/110008517-ccb4ea00-7d56-11eb-964f-45fddfce9292.png)
