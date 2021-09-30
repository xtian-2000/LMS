import mysql.connector as mysql

host = "localhost"
user = "PongoDev"
password = "PongoDev44966874"


class Database:
    def __init__(self):
        # Connecting to mysql database
        try:
            self.db = mysql.connect(host=host,
                                    user=user,
                                    password=password)
            print("Connected successfully")
        except Exception as e:
            print("Failed to connect")
            print(e)

        # Creating lmsdatabase
        try:
            self.mycursor = self.db.cursor()
            self.mycursor.execute("CREATE DATABASE lmsdatabase")
            print("lmsdatabase has been created")
        except Exception as e:
            print("Could not create database")
            print(e)

        # Viewing all databases
        try:
            self.mycursor.execute("SHOW DATABASES")
            print("These are the available databases")
            for database in self.mycursor:
                print(database)
        except Exception as e:
            print("Could not show all the databases")
            print(e)

        # Connecting to lmsdatabase
        try:
            self.db1 = mysql.connect(host=host,
                                     user=user,
                                     password=password,
                                     database="lmsdatabase")
            print("Connected to lmsdatabase")
        except Exception as e:
            print("Could not connect to lmsdatabase")
            print(e)

        # Creating user table in database
        try:
            self.mycursor = self.db1.cursor()
            self.mycursor.execute("CREATE TABLE `lmsdatabase`.`user` (`userid` INT NOT NULL AUTO_INCREMENT, "
                                  "`username` VARCHAR(45) NOT NULL,`password` VARCHAR(45) NOT NULL,`email` VARCHAR("
                                  "45) NOT NULL,PRIMARY KEY (`userid`),UNIQUE INDEX `userid_UNIQUE` (`userid` ASC) "
                                  "VISIBLE,UNIQUE INDEX `username_UNIQUE` (`username` ASC) VISIBLE);")
            print("'user' table is created successfully")
        except Exception as e:
            print("'user' table could not be created")
            print(e)

        # Creating borrower table in database
        try:
            self.mycursor = self.db1.cursor()
            self.mycursor.execute("CREATE TABLE `lmsdatabase`.`borrower` (`userid` INT NOT NULL,`borrowerid` INT NOT "
                                  "NULL AUTO_INCREMENT,`name` VARCHAR(45) NOT NULL,`address` VARCHAR(45) NOT NULL,"
                                  "`age` VARCHAR(45) NULL,`created` VARCHAR(45) NULL,`gender` VARCHAR(45) NULL,"
                                  "PRIMARY KEY (`borrowerid`),UNIQUE INDEX `borrowerid_UNIQUE` (`borrowerid` ASC) "
                                  "VISIBLE,INDEX `userid_idx` (`userid` ASC) VISIBLE,CONSTRAINT `userid`FOREIGN KEY ("
                                  "`userid`) REFERENCES `lmsdatabase`.`user` (`userid`) ON DELETE NO ACTION ON UPDATE "
                                  "NO ACTION);")
            print("'borrower' table is created successfully")
        except Exception as e:
            print("'borrower' table could not be created")
            print(e)

        # Creating loans table in database
        try:
            self.mycursor = self.db1.cursor()
            self.mycursor.execute("CREATE TABLE `lmsdatabase`.`loan` (`loanid` INT NOT NULL AUTO_INCREMENT,"
                                  "`borrowerid` INT NOT NULL, `amount` INT NOT NULL, `interest` INT NOT NULL,"
                                  " `days` INT NOT NULL, `created` VARCHAR(45) NOT NULL, PRIMARY KEY (`loanid`),"
                                  " INDEX `borrowerid_idx` (`borrowerid` ASC) VISIBLE, CONSTRAINT `borrowerid`"
                                  " FOREIGN KEY (`borrowerid`) REFERENCES `lmsdatabase`.`borrower` (`borrowerid`)"
                                  " ON DELETE NO ACTION ON UPDATE NO ACTION);")
            self.mycursor.execute("ALTER TABLE `lmsdatabase`.`loan` ADD COLUMN `userid` INT NOT"
                                  " NULL AFTER `borrowerid`;")
            self.mycursor.execute("ALTER TABLE `lmsdatabase`.`loan` ADD COLUMN `dateissued` VARCHAR(45)"
                                  " NOT NULL AFTER `created`;")
            self.mycursor.execute("ALTER TABLE `lmsdatabase`.`loan` ADD COLUMN `status` VARCHAR(45) NOT NULL AFTER "
                                  "`dateissued`;")

            print("'loan' table is created successfully")
        except Exception as e:
            print("'loan' table could not be created")
            print(e)
