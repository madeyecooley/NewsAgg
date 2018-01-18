#This script pulls info from the database

import mysql.connector as mariadb
import numpy as np
try:
    import simplejson as json
except:
    import json
from .connectdb import connect

def get_data():
    mariadb_connection = connect()

    cursor = mariadb_connection.cursor()

    cursor.execute("SELECT article_site, article_title FROM articles_article")

    data = cursor.fetchall()
    np.random.shuffle(data)

    for row in data:
        converted = {
            "title" : row[1],
            "site" : row[0]
        }
       
    #print json.dumps(data)

    print converted
    return converted

    cursor.close()
    mariadb_connection.close()



