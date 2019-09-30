import sqlite3
conn = sqlite3.connect('ExerciseAges.db')
cur = conn.cursor()

myDictionary = {'Elijah': 37, 'Livie': 19, 'Brannan': 29, 'Girls': 38, 'Rebekkah': 18 , 'Samara': 18}

cur.execute('''
CREATE TABLE IF NOT EXISTS Ages (name VARCHAR(128), age INTEGER)''')

cur.execute('''DELETE FROM Ages''')

for x in myDictionary :
  cur.execute('''INSERT INTO Ages (name, age) VALUES (?, ?)''',
                            (x,myDictionary[x]))
