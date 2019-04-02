#!/usr/local/bin/python

import sqlite3

db = sqlite3.connect('orders.db')
cur = db.cursor()

query = """
SELECT 
  cu.first_name || ' ' || cu.last_name AS cust_name,
  prod.title,  
  ord.quantity * prod.price AS order_value
FROM orders AS ord 
JOIN products AS prod ON ord.product_id = prod.id
JOIN customers AS cu ON ord.cust_code = cu.cust_code;
"""

print(query)

cur.execute(query)

for row in cur:
    print(row)
    # print("{0[0]:20s} {0[1]:30s} {0[2]:6.2f}".format(row))

 









 
    
'''
print(
    "{0[0]:20s} {0[1]:30s} {0[2]:6s}".format(
        [column[0].upper() for column in cur.description]
        )
    )
'''    