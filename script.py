1. You will have to specify a database name dbname and a user user in the .connect() method. Because of the multiple connections, 
Postgres uses multiple users and databases as a way to improve security and division of data. Without those values attached, 
Postgres will not know where you would like to connect to and will fail. Once you are connected, we are ready to take advantage of 
the features Postgres has.


Instrcutions:

-Import the psycopg2 library.
-Connect to the dq database with the user dq.
-Use the print function to display the Connection object.
-Close the Connection using the close method.

Code:

import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
print(conn)
conn.close()

2. Interacting with the database

Assume that the table being asked to query has been created.

Instructions

-Connect to the dq database as the user dq
-Using the Cursor object, create a string query that selects all from the notes table.
-Execute the query using the execute method.
-Fetch all the results from the table and assign it to the variable notes.
-Close the Connection using the close method.

import psycopg2
conn=psycopg2.connect("dbname=dq user=dq")
cur=conn.cursor()
cur.execute('Select * from notes')
notes = cur.fetchall
conn.close()


3. Creating a Table

Instructions:

-Connect to the dq database as the user dq
-Write a SQL query that creates a table called users in the dq database, with the following columns and data types:
-id -- integer data type, and is a primary key.
-email -- text data type.
-name -- text data type.
-address -- text data type.
-Execute the query using the execute method.
-Don't close the connection.


import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
cur=conn.cursor()
cur.execute("create table users(id integer PRIMARY KEY, email text, name text, address text)")


4. SQL Transactions

Instructions:

-Connect to the dq database as the user dq.
-Write a SQL query that creates a table called users in the dq database, with the following columns and data types:
    id -- integer data type, and is a primary key.
    email -- text data type.
    name -- text data type.
    address -- text data type.
-Execute the query using the execute method.
-Use the commit method on the Connection object to apply the changes in the transaction to the database.
-Close the Connection

import psycopg2
conn=psycopg2.connect("dbname=dq user=dq")
cur=conn.cursor()
cur.execute("create table users(id integer PRIMARY KEY, email text, name text, address text)")
conn.commit()
conn.close()


5. Inserting the Data:

Instructions:

-Import the csv module.
-Load the user_accounts.csv using the csv module
-Connect to the dq database as the user dq
-Execute the insert query on the users table using the execute method from the example above.
  Insert every row from the user_accounts.csv file and skip the header row.
-Fetch all the results from the users table and assign it to the variable users.
-Close the Connection using the close method.


with open('user_accounts.csv','r') as f:
    reader = csv.reader(f)
    next(reader)
    rows=[row for row in reader]
        
conn=psycopg2.connect("dbname=dq user=dq")
cur=conn.cursor()
for row in rows:
    cur.execute("insert into users values (%s,%s,%s,%s)", row)
conn.commit()

cur.execute('select * from users')
users=cur.fetchall()
conn.close()


6. Copying the data:

Another Postgres command called COPY FROM takes in a file (like a CSV) and automatically loads the file into a Postgres table.

Instructions:

-Connect to the dq database as the user dq
-Load the user_accounts.csv using with open(...) as f.
-Skip the header row.
-Using the copy_from method, copy the file into the database.
-Fetch all the results from the users table and assign it to the variable users.
-Close the Connection using the close method.


import psycopg2
conn=psycopg2.connect("dbname=dq user=dq")
cur=conn.cursor()

#user_accounts.csv has a header row.
with open('user_accounts.csv','r') as f:
    #skip the header row
    next(f)
    cur.copy_from(f,'users',sep=",")
conn.commit()

cur.execute('select * from users')
users=cur.fetchall()
conn.close()






































