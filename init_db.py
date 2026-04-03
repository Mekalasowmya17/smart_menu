import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS menu (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    cost INTEGER
)
''')

# CLEAR old data
cursor.execute("DELETE FROM menu")

# ONLY SOURCE OF ITEMS
items = [
("Pizza",120), ("Burger",80), ("Pasta",100), ("Sandwich",60),
("French Fries",70), ("Cheese Balls",90), ("Veg Roll",50),
("Paneer Tikka",150), ("Chicken Wings",180), ("Fried Rice",110),
("Noodles",100), ("Manchurian",130), ("Soup",60), ("Salad",50),
("Ice Cream",40), ("Brownie",70), ("Milkshake",90),
("Cold Coffee",80), ("Juice",40), ("Tea",20),
("Coffee",30), ("Idli",40), ("Dosa",60), ("Vada",30),
("Biryani",180), ("Paratha",50), ("Dal Rice",70),
("Chapati Curry",80), ("Pizza Combo",200), ("Family Meal",350)
]

cursor.executemany("INSERT INTO menu (name, cost) VALUES (?, ?)", items)

conn.commit()
conn.close()