#
# Database access functions for the web forum.
# 

import psycopg2
import time

## Database connection
DB = psycopg2.connect("dbname=forum")
cur = DB.cursor()

## Get posts from database.
def GetAllPosts():
    cur.execute("select content, time from posts order by time desc;")
    rows = cur.fetchall()
    return [{"content": row[0], "time": row[1]} for row in rows]
    '''Get all the posts from the database, sorted with the newest first.

    Returns:
      A list of dictionaries, where each dictionary has a 'content' key
      pointing to the post content, and 'time' key pointing to the time
      it was posted.
    '''
#    posts = [{'content': str(row[1]), 'time': str(row[0])} for row in DB]
#    posts.sort(key=lambda row: row['time'], reverse=True)
#    return posts

## Add a post to the database.
def AddPost(content):
    cur.execute("insert into posts (content, time) values ('"+content+"', '"+time.strftime('%c', time.localtime())+"');")
    DB.commit()
    '''Add a new post to the database.

    Args:
      content: The text content of the new post.
    '''
