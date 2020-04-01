import psycopg2
from flask import Flask, request

#connect to Db
con = psycopg2.connect(
    host = "localhost",
    database="bank",
)
#cursor
cur = con.cursor()

#execute query
cur.execute("insert into accounts (id, username) values (%s, %s)", (13, "Burdorf") )

cur.execute("SELECT id, username from accounts")

rows = cur.fetchall()

for r in rows:
    print(f"id {r[0]} username {r[1]}")

# commit 
con.commit()

#close the curser
cur.close()

#close connection
con.close()





