import sqlite3
from os import system
a= system("rm dbz")
conn = sqlite3.connect('dbz')
conn.execute("""
CREATE TABLE targets (hash TEXT NOT NULL PRIMARY KEY, name TEXT)
""")

conn.execute("""
CREATE TABLE phished (hash TEXT, timings DATETIME)
""")

conn.execute("""
CREATE TABLE data (hash TEXT NOT NULL PRIMARY KEY, details TEXT)
""")


conn.commit()
conn.close()

