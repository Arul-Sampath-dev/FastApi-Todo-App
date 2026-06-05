import os

import psycopg2
from dotenv import load_dotenv
from psycopg2.extras import RealDictCursor

load_dotenv()


def get_db_cursor():
    conn = psycopg2.connect(
        database=os.getenv("DATABASE"),
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
    )

    cur = conn.cursor(cursor_factory=RealDictCursor)

    yield cur

    conn.commit()

    cur.close()
    conn.close()
