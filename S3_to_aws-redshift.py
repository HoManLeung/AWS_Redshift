import psycopg2

# connect to redshift, we need database name, username, host name, port, password
# These information can be find in AWS redshift cluster
connection=psycopg2.connect(host='redshift-cluster-1.c1rosdv93x1v.us-east-2.redshift.amazonaws.com',
                            dbname='ds530',user='ds530awsuser',password='Rr24824487',port='5439')

table=['category','customer','product','region','salestransaction','soldvia','store','vendor']

cur=connection.cursor()

for i in table:
    sql="""copy {} from 's3://ds530-aws-zagdb/{}.csv' credentials 'aws_iam_role=arn:aws:iam::197892593282:role/DS530-redshift' csv delimiter ',' ignoreheader 1 region 'us-east-2';""".format(i,i)
    cur.execute(sql)
    connection.commit()


