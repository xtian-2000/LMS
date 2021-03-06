import mysql.connector as mysql

host = "lms.cm10enqi961k.us-east-2.rds.amazonaws.com"
user = "admin"
password = "44966874"


class Database:
    def __init__(self):
        """
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
            print(e)"""

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
        """
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
            self.mycursor.execute("ALTER TABLE `lmsdatabase`.`loan` ADD COLUMN `balance` INT NOT NULL AFTER "
                                  "`borrowerid`;")
            self.mycursor.execute("ALTER TABLE `lmsdatabase`.`loan` ADD COLUMN `duedate` VARCHAR(45) NOT NULL"
                                  " AFTER `status`;")

            print("loan table is created successfully")
        except Exception as e:
            print("loan table could not be created")
            print(e)

        # Creating payment table in database
        try:
            self.mycursor = self.db1.cursor()
            self.mycursor.execute("CREATE TABLE `lmsdatabase`.`payment` (`paymentid` INT NOT NULL,`loanid` INT NOT"
                                  " NULL,`amount` INT NOT NULL, `dateissued` VARCHAR(45) NOT NULL, PRIMARY KEY"
                                  " (`paymentid`), INDEX `loanid_idx` (`loanid` ASC) VISIBLE, CONSTRAINT `loanid`"
                                  " FOREIGN KEY (`loanid`) REFERENCES `lmsdatabase`.`loan` (`loanid`) ON DELETE NO"
                                  " ACTION ON UPDATE NO ACTION);")
            self.mycursor.execute("ALTER TABLE `lmsdatabase`.`payment` CHANGE COLUMN `paymentid` `paymentid` INT NOT"
                                  " NULL AUTO_INCREMENT ;")
            self.mycursor.execute("ALTER TABLE `lmsdatabase`.`payment` ADD COLUMN `balance` INT NOT NULL AFTER"
                                  " `amount`;")

            print("payment table is created successfully")
        except Exception as e:
            print("payment table could not be created")
            print(e)
        """
