import os
import urllib.parse as up
import psycopg2


DATABASE_URL ='postgres://olvugkyr:fsBHvOPyzJzO21reozT7mZsyv7FSez7G@kandula.db.elephantsql.com/olvugkyr'
up.uses_netloc.append("postgres")
url = up.urlparse(DATABASE_URL)
conn = psycopg2.connect(database=url.path[1:],
user=url.username,
password=url.password,
host=url.hostname,
port=url.port
)

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS course;')
cur.execute('CREATE TABLE course (id serial PRIMARY KEY,'
                                 'NumRéunion varchar (2) NOT NULL,'
                                 'NumCourse varchar (2) NOT NULL,'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )

cur.execute('INSERT INTO course (NumRéunion, NumCourse)'
            'VALUES (%s, %s)',
            ('R1',
             'C1')
            )

cur.execute('INSERT INTO course (NumRéunion, NumCourse)'
            'VALUES (%s, %s)',
            ('R2',
             'C2')
            )

conn.commit()

cur.close()
conn.close()