from models.menu_model import get_dishes

def optimize_menu(budget):
    dishes = get_dishes()
    selected = []
    total = 0

    for dish in dishes:
        if total + dish["cost"] <= budget:
            selected.append(dish)
            total += dish["cost"]

    return {
        "menu": selected,
        "total_cost": total
    }