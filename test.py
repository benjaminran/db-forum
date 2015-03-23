import psycopg2
import time

db = psycopg2.connect('dbname=forum')
cur = db.cursor()

cur.execute("select content, time from posts order by time;")
rows = cur.fetchall()
list = []
print type(cur)
print type(rows)
for row in rows:
    print type(row)
    print row
    list.append({"content": row[0], "time": row[1]})
    print list
for string in ["hello", "world", "this", "is", "some", "data"]:
    cur.execute("insert into posts (content, time) values ('"+string+"', '"+time.strftime('%c', time.localtime())+"');")
db.commit()
for record in cur.execute("select * from posts;"):
    print record
