menu = []

def add_dish(name, cost):
    menu.append({
        "name": name,
        "cost": int(cost)
    })

def get_dishes():
    return menu