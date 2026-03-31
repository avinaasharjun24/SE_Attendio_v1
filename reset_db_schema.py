import os
import sys

# Add the project dir to path
sys.path.insert(0, r"c:\Users\avina\Downloads\attendio")

from utils.db import get_db_connection

def reset_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS attendance_logs;")
    cursor.execute("DROP TABLE IF EXISTS face_embeddings;")
    cursor.execute("DROP TABLE IF EXISTS attendance_sessions;")
    cursor.execute("DROP TABLE IF EXISTS students;")
    cursor.execute("DROP TABLE IF EXISTS users;")
    conn.commit()
    cursor.close()
    conn.close()
    
    from utils.db import initialize_database
    success, res, err = initialize_database()
    print("Initialize:", success, res, err)

if __name__ == "__main__":
    reset_db()
