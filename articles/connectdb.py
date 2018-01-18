import mysql.connector as mariadb

def connect():
    mariadb_connection = mariadb.connect(user='madi', password='yourpassword',
                database='newsaggdb')
    return mariadb_connection
