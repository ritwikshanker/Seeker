import pymysql.cursors

# Connect to the database
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
            sql = "CREATE TABLE IF NOT EXISTS " \
                  "users_data(" \
                  "ID INT PRIMARY KEY NOT NULL AUTO_INCREMENT," \
                  "email_id TEXT NOT NULL," \
                  "tv_series TEXT NOT NULL)"
            cursor.execute(sql)
            # Create a new record
            sql = "INSERT INTO users_data (email_id, tv_series) VALUES (%s, %s)"
            cursor.execute(sql, (email_Add, series_Name))

        # Commiting changes to database
        connection.commit()

        with connection.cursor() as cursor:
            # Read a all record
            sql = "SELECT * FROM users_data"
            cursor.execute(sql, )
            result = cursor.fetchall()
            print(result)
    finally:
        connection.close()
