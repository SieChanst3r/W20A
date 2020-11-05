import dbcreds
import mariadb

# username = input("Insert a username: ")
# content = input("What is on your mind? insert here: ")

def createPost():
    content = input("What is on your mind? insert here: ")
    conn =mariadb.connect(user = dbcreds.user, password = dbcreds.password, host = dbcreds.host, port = dbcreds.port, database = dbcerds.database)
    