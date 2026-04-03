import sqlite3

def connect_db():
    return sqlite3.connect("database.db")

def add_dish(name, cost):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO menu (name, cost) VALUES (?, ?)", (name, cost))

    conn.commit()
    conn.close()

def get_dishes():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT name, cost FROM menu")
    data = cursor.fetchall()

    conn.close()

    return [{"name": d[0], "cost": d[1]} for d in data]