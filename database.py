import mysql.connector


def connect_db():

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Payel12@",
        database="quiz_db"
    )

    return db