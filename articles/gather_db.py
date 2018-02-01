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

    cursor.execute("SELECT article_site, article_title, article_url, article_summary, article_photosrc, article_text FROM articles_article")

    data = cursor.fetchall()
    np.random.shuffle(data)
    encoding = "utf-8"

    converted = {}
    for row in data:
        info = [row[0].encode(encoding), row[2].encode(encoding), row[3].encode(encoding), row[4].encode(encoding), row[5].encode(encoding)]
        converted[row[1]] = [info]

    #print converted
    return converted

    cursor.close()
    mariadb_connection.close()



