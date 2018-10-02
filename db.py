import sqlite3
import os



def db_execute(statement):
    db = sqlite3.connect('postcards.sqlite')
    cur = db.cursor()
    cur.execute(statement)
    db.commit()
    db.close()




#Setup - Runs on app start, if database does not exist will create.  
db = None
db_exist = os.path.isfile('postcards.sqlite')
if db_exist != True:
    db_execute("CREATE TABLE IF NOT EXISTS postcards(Serial INTEGER PRIMARY KEY AUTOINCREMENT, UID TEXT, from_user TEXT, to_user TEXT, photo_id TEXT, Body TEXT, Stamp, Private TEXT)")
    db_execute("CREATE TABLE IF NOT EXISTS photos(photo_id INTEGER PRIMARY KEY AUTOINCREMENT, photo_name TEXT, username TEXT, url TEXT)")
    db_execute("CREATE TABLE IF NOT EXISTS stamps(Photo_ID INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, To_User TEXT, url TEXT)")
    #we know storing login passwords is bad here, going to figure out another way later.
    db_execute("CREATE TABLE IF NOT EXISTS users(user_id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)")
else:
    pass

