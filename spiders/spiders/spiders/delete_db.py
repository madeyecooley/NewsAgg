#This script deletes everything in the database. 
#DONT SHARE

import mysql.connector as mariadb

mariadb_connection = mariadb.connect(user='madi', password='yourpassword', 
	database='newsaggdb')

cursor = mariadb_connection.cursor()

cursor.execute("TRUNCATE TABLE articles_article")

mariadb_connection.close()
