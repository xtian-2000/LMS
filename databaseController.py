import mysql.connector as mysql

db = mysql.connect(host="localhost",
                   user="PongoDev",
                   password="PongoDev44966874",
                   database="LMSdatabase"
                   )
mycursor = db.cursor()


class Database:
    def __init__(self):
        try:
            self.db = mysql.connect(host="localhost",
                               user="PongoDev",
                               password="PongoDev44966874",
                               database="LMSdatabase"
                               )
            print("Connected successfully")
            mycursor = db.cursor()
        except Exception as e:
            print(e)
            print("Failed to connect")

    def create(self):
        # Creating a database
        try:
            mycursor = db.cursor()
            mycursor.execute("CREATE DATABASE LMSdatabase")
            print("LMSdatabase")
        except Exception as e:
            print("Could not create database")
            print(e)
