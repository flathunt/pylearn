#!/usr/local/bin/python

import sqlite3

# SQL statements...

create_table = """
CREATE TABLE books (
    id              INTEGER PRIMARY KEY,
    title           TEXT,
    genre           TEXT,
    price           NUMERIC,
    date_added      date DEFAULT (date())
)
"""

insert_book = """
INSERT INTO books (genre, title, price)
VALUES (?, ?, ?)
"""

query = """
SELECT genre, title, price, date_added
FROM books 
ORDER BY genre, title
"""

# Connect and get a cursor object...

db = sqlite3.connect('library.db')
cur = db.cursor()

# Create and populate table...

cur.execute(create_table)

for line in open('data.csv'):
    fields = line[:-1].split(',')
    cur.execute(insert_book, fields)

db.commit()

# Query the table...

cur.execute(query)
for row in cur:
    print("{0[0]:15s} {0[1]:30s} {0[2]:6.2f} ({0[3]:})".format(row))
    
cur.close()
db.close()
