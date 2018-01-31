#delete_db.py

#This script deletes everything in the database. 

import mysql.connector as mariadb
from connectdb import connect

def deletedb():
    mariadb_connection = connect()

    cursor = mariadb_connection.cursor()

    cursor.execute("TRUNCATE TABLE articles_article")

    mariadb_connection.close()
