import sqlite3

conn = sqlite3.connect('Chinook_Sqlite.sqlite')

cursor = conn.cursor()

cursor.execute('SELECT name from artists;')


conn.close()
