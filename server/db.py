import mysql.connector

cnx = mysql.connector.connect(user='root', password='Antonio06!',
                              host='127.0.0.1',
                              database='booklib')

cursor = cnx.cursor()

create_users = '''CREATE TABLE IF NOT EXISTS users(
    ID VARCHAR(40),
    PRIMARY KEY(ID),
    username VARCHAR(20) NOT NULL,
    email VARCHAR(40) NOT NULL,
    password VARCHAR(40) NOT NULL
)'''

create_books = '''CREATE TABLE IF NOT EXISTS books(
    ID VARCHAR(20) NOT NULL,
    PRIMARY KEY(ID),
    status ENUM('finished', 'to read', 'paused', 'reading') DEFAULT NULL,
    userID VARCHAR(40) NOT NULL,
    FOREIGN KEY(userID) REFERENCES users(ID)
)'''
# startDate Date default now()
# finishDate Date

cursor.execute(create_users)
cursor.execute(create_books)
