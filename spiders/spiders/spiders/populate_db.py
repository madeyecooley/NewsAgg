#This script is supposed to populate a database with the info that is scraped 
#***THIS FILE SHOULD NOT BE SHARED***


import mysql.connector as mariadb

mariadb_connection = mariadb.connect(user='madi', password='yourpassword', 
	database='newsaggdb')

cursor = mariadb_connection.cursor()


#def add_to_db(article_title, article_summary, article_photosrc, article_url, article_site):
#    cursor.execute("INSERT INTO articles_article (article_title, article_summary, article_url, article_site) VALUES (%s,%s,%s,%s)", (article_title, article_summary, article_url, article_site))
#    cursor.execute("INSERT articles_article VALUES (article_title, article_summary, article_url, article_site)")

#    mariadb_connection.commit#()


#cursor.execute("LOAD DATA LOCAL INFILE 'db_data.txt' INTO TABLE articles_article COLUMNS TERMINATED BY '\t' LINES TERMINATED BY '\n'")

cursor.execute("LOAD DATA LOCAL INFILE 'db_data.txt' INTO TABLE articles_article")

mariadb_connection.commit()

cursor.close()
mariadb_connection.close()
