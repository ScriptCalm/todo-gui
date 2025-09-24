# db.py
import sqlite3
import os

DB_NAME = os.path.join(os.getenv("APPDATA"), "todo_gui_tasks.db")


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def get_tasks():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, task FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def add_task(task):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
