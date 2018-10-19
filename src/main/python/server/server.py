import sqlite3

conn = sqlite3.connect('test.db')

c = conn.cursor()

#erstellen der DB
c.execute('''CREATE TABLE user
             (id id, username text, email text)''')

conn.commit()

conn.close()