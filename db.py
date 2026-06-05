import json

import psycopg2
from psycopg2.extras import RealDictCursor

conn = psycopg2.connect(database="postgres", user="postgres", password="123")

cur = conn.cursor(cursor_factory=RealDictCursor)

cur.execute(""" CREATE TABLE IF NOT EXISTS student(
    id INT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255)
)
    """)

# cur.execute(""" INSERT INTO student (id, name, email) VALUES
#     (1, 'Arul', 'arulsampathcyr@gmail.com'),
#     (2, 'John Doe', 'johndoe@gmail.com')
#     """)

cur.execute("""SELECT * FROM student""")

print(json.dumps(cur.fetchall()))

conn.commit()
cur.close()
conn.close()
