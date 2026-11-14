import sqlite3

connection = sqlite3.connect("itstep2_DB.sl3", 5)
cur = connection.cursor()

cur.execute("INSERT INTO first_table (name) VALUES ('sasha');")
cur.execute("INSERT INTO first_table (name) VALUES ('sasha');")
cur.execute("INSERT INTO first_table (name) VALUES ('stas');")
cur.execute("INSERT INTO first_table (name) VALUES ('andrey');")
cur.execute("INSERT INTO first_table (name) VALUES ('danil');")
cur.execute("INSERT INTO first_table (name) VALUES ('miroslav');")
cur.execute("INSERT INTO first_table (name) VALUES ('masha');")
cur.execute("INSERT INTO first_table (name) VALUES ('sasha');")
cur.execute("INSERT INTO first_table (name) VALUES ('kira');")
cur.execute("INSERT INTO first_table (name) VALUES ('danil');")
connection.commit()

connection.close()