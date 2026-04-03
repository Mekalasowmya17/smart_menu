from flask import Blueprint, render_template, request
import sqlite3

menu_bp = Blueprint('menu', __name__)

# store selected items
selected_items_global = []


# HOME
@menu_bp.route('/')
def home():
    return render_template("index.html")


# VIEW MENU (only display)
@menu_bp.route('/view_menu')
def view_menu():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT name, cost FROM menu")
    data = cursor.fetchall()

    conn.close()

    dishes = [{"name": row[0], "cost": row[1]} for row in data]

    return render_template("view_menu.html", dishes=dishes)


# ADD ITEMS (checkbox selection)
@menu_bp.route('/add_items')
def add_items():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT name, cost FROM menu")
    data = cursor.fetchall()

    conn.close()

    dishes = [{"name": row[0], "cost": row[1]} for row in data]

    print(dishes)  # 👉 ADD THIS LINE (debug)

    return render_template("add_menu.html", dishes=dishes)


# AFTER SELECTING ITEMS → GO TO BUDGET PAGE
@menu_bp.route('/go_optimize', methods=['POST'])
def go_optimize():
    global selected_items_global
    selected_items_global = request.form.getlist('items')

    return render_template("optimize_menu.html")


# FINAL OPTIMIZATION
@menu_bp.route('/optimize', methods=['POST'])
def optimize():
    global selected_items_global

    budget = int(request.form['budget'])

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # get only selected items
    query = "SELECT name, cost FROM menu WHERE name IN ({})".format(
        ",".join(["?"] * len(selected_items_global))
    )

    cursor.execute(query, selected_items_global)
    data = cursor.fetchall()

    conn.close()

    dishes = [{"name": row[0], "cost": row[1]} for row in data]

    # optimization logic
    final = []
    total = 0

    for dish in dishes:
        if total + dish['cost'] <= budget:
            final.append(dish)
            total += dish['cost']

    return render_template("result.html", dishes=final, total=total)