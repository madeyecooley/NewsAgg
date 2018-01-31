#populate_db.py

#This script is supposed to populate a database with the info that is scraped 


import mysql.connector as mariadb
from connectdb import connect

def populatedb():
    mariadb_connection = connect()

    cursor = mariadb_connection.cursor()
    cursor.execute("LOAD DATA LOCAL INFILE 'db_data.txt' INTO TABLE articles_article")

    mariadb_connection.commit()

    cursor.close()
    mariadb_connection.close()
