import psycopg2
import csv
import os

def extract_ZAGDB():
    # table list in ZAGDB
    table=['category','customer','product','region','salestransaction','soldvia','store','vendor']

    connection=psycopg2.connect(host='127.0.0.1',dbname='ZAGDB',user='postgres',password='Rr24824487',gssencmode="disable")

    cur = connection.cursor()

    parent_dir="C:/Users/AsusPC/Desktop/Saint Peter's University Note/DS 530 Big data and data management/Final Project"

    dir='ZAGDB'

    if not os.path.isdir(os.path.join(parent_dir,dir)):
        os.makedirs(os.path.join(parent_dir,dir))

    for t in table:
        cur.execute('select * from {}'.format(t))
        data=cur.fetchall()

        # cursor.description show the column name and typeID
        header=[h[0] for h in cur.description]

        with open('{}/{}.csv'.format(os.path.join(parent_dir,dir),t),'w',newline='') as f:
            writer=csv.writer(f,delimiter=",")
            writer.writerow(header)
            writer.writerows(data)

    # Close the cursor and connection
    cur.close()
    connection.close()


