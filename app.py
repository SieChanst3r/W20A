import dbcreds
import mariadb

# username = input("Insert a username: ")
# content = input("What is on your mind? insert here: ")

def createPost():
    content = input("What is on your mind? insert here: ")
    conn =mariadb.connect(user = dbcreds.user, password = dbcreds.password, host = dbcreds.host, port = dbcreds.port, database = dbcreds.database)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO blog_post(username, content, id) VALUES(?, ?, NULL)", [username, content])
    conn.commit()
    print("Your Post has beed Created!")
    cursor.close()
    conn.close()

def allPosts():
    conn = mariadb.connect(user = dbcreds.user, password = dbcreds.password, host = dbcreds.host, port = dbcreds.port, database = dbcreds.database)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM blog_post")
    rows = cursor.fetchall()
    print(rows)
    cursor.close()
    conn.close()

# username and options
print("This is a command line blog! Insert username and choose what you would like to do: ")
username = input("Username: ")
userChoice = input("a = Create blog post [OR] b = View all posts: ")

if userChoice == "a":
    createPost()
elif userChoice == "b":
    allPosts()
else:
    print("Not a valid selection")