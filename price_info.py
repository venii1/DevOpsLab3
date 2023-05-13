
price_list = {'apple': 1.2, 'orange': 1.4, 'watermel': 6.5, 'pineap': 2.7, 'pear': 0.9, 'papaya': 2.95, 'pomegra': 4.95}

quantity_list = {'apple': 5, 'orange': 5, 'watermel': 1, 'pineap': 2, 'pear': 10, 'papaya': 1, 'pomegra': 2}


def total_cost_shopping():
    total_cost = 0
    for key in price_list.keys():
        if key in quantity_list:
            total_cost = total_cost + (quantity_list.get(key) * price_list.get(key))
    print("total cost = ", total_cost)
    return total_cost


def cost_of_fruits(fruit, quantity):
    cost = quantity * price_list.get(fruit)
    print("cost of ", quantity, fruit, "=", cost)
    return cost

def main():

    cost_of_fruits('apple', 10)
    total_cost_shopping()


if __name__ == "__main__":
    main()
