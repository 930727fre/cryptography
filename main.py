import getpass
import bcrypt
import sqlite3 as sql
import os



#pw =getpass.getpass("input your password:")
pw=12345678
salt=bcrypt.gensalt()
hashed=bcrypt.hashpw(pw,salt)


if bcrypt.checkpw(pw, hashed):
    print("match")
    print(hashed.hashpw(hasded,salt))
else:
    print("does not match")
