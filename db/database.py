import sqlite3

conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    company TEXT,
    location TEXT,
    url TEXT UNIQUE,
    score INTEGER
)
""")

conn.commit()

def save_job(job):
    try:
        cursor.execute("""
        INSERT INTO jobs (title, company, location, url, score)
        VALUES (?, ?, ?, ?, ?)
        """, (
            job["title"],
            job["company"],
            job["location"],
            job["url"],
            job["score"]
        ))
        conn.commit()
        return True
    except:
        return False
