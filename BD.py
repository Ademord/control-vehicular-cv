#!/usr/bin/python
import psycopg2
import sys
 
def execute(query):
	#Define our connection string
	conn_string = "host='127.0.0.1' port='54320' dbname='control_vehicular' user='homestead' password='secret'"
	# print the connection string we will use to connect
	# print ("Connecting to database\n->{}".format(conn_string))
	# get a connection, if a connect cannot be made an exception will be raised here
	conn = psycopg2.connect(conn_string)
	# conn.cursor will return a cursor object, you can use this cursor to perform queries
	cursor = conn.cursor()
	# print ("Connected to DB!")
	#cursor.execute("""SELECT c.ip, (SELECT nombre FROM lugar WHERE id = c.lugar_id) FROM camara c""")
	cursor.execute(query)
	try:
		results = cursor.fetchall()
		conn.commit()
		cursor.close()
		conn.close()
		return results
	except psycopg2.ProgrammingError:
		conn.commit()
		cursor.close()
		conn.close()
		return 
