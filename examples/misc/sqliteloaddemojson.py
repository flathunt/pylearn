#!/usr/local/bin/python

import os
import sqlite3
import pprint
import json

dbname = 'numbers.db'
try:
    os.remove(dbname)
except FileNotFoundError:
    pass
   

# SQL statements...

create_table = """
CREATE TABLE numbers (
    id              INTEGER PRIMARY KEY,
    title           TEXT,
    value           REAL
)
"""

insert_number = """
INSERT INTO numbers (title, value)
VALUES (?, ?)
"""

query = """
SELECT *
FROM numbers 
"""

# Connect and get a cursor object...

db = sqlite3.connect(dbname)
cur = db.cursor()

# Create and populate table...

cur.execute(create_table)

number_data = (
    "pi,3.14159265359",
    "Avogadro constant,6.02214e23",
    "c,299792458",
    "e,1.6e-19"
)

for line in number_data:
   fields = line.split(',')
   
   cur.execute(insert_number, fields)

db.commit()

# Query the table...

cur.execute(query)

column_names = [ col[0] for col in cur.description ]

results = []
for row in cur:
    results.append(dict(zip(column_names, row)))

pprint.pprint(json.dumps(results))    
    
cur.close()
db.close()
