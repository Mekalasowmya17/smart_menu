def optimize_menu(dishes, budget):
    selected = []
    total = 0

    for dish in dishes:
        if total + dish['cost'] <= budget:
            selected.append(dish)
            total += dish['cost']

    return selected, total