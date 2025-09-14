import sqlite3
from pathlib import Path

DB_PATH = Path('data.db')

def initialize():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS photos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            action TEXT NOT NULL,
            image BLOB NOT NULL
        )
        '''
    )
    conn.commit()
    conn.close()

def insert_image(name: str, action: str, image_path: Path) -> None:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    with open(image_path, 'rb') as f:
        image_bytes = f.read()
    cursor.execute(
        'INSERT INTO photos (name, action, image) VALUES (?, ?, ?)',
        (name, action, image_bytes)
    )
    conn.commit()
    conn.close()

def fetch_all():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, action, image FROM photos')
    rows = cursor.fetchall()
    conn.close()
    return rows

if __name__ == '__main__':
    initialize()
    print(f"Database initialized at {DB_PATH.resolve()}")
