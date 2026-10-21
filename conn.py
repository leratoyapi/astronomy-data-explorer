
import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  port=3307,
  password="082517@King",
  database="astronomy"
)

print ("connected to database yeppie:)", conn)
