#Author @Ritwik Shanker

import pymysql.cursors

# Connect to the database
db1 = pymysql.connect(host="localhost", user="root", passwd="")
cursor = db1.cursor()
sql = "SET sql_notes = 0"
cursor.execute(sql)
sql = 'CREATE DATABASE IF NOT exists hackercamp'
cursor.execute(sql)
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='hackercamp',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


def connect_to_db(email_Add, series_Name):
    try:
        with connection.cursor() as cursor:
            # Create table if not exists
            sql = "SET sql_notes = 0"  # Temporarily disable the "Table already exists" warning
            cursor.execute(sql)
            cursor.execute(sql)
            sql = "CREATE TABLE IF NOT EXISTS " \
                  "users_data(" \
                  "ID INT PRIMARY KEY NOT NULL AUTO_INCREMENT," \
                  "email_id TEXT NOT NULL," \
                  "tv_series TEXT NOT NULL)"
            cursor.execute(sql)
            # Create a new record
            sql = "SET sql_notes = 1"  # And then re-enable the warning again
            cursor.execute(sql)
            sql = "INSERT INTO users_data (email_id, tv_series) VALUES (%s, %s)"
            cursor.execute(sql, (email_Add, series_Name))

        # Commiting changes to database
        connection.commit()
    finally:
        connection.close()
