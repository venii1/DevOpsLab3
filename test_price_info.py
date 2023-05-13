price_list = {'apple': 1.2, 'orange': 1.4, 'watermel': 6.5, 'pineap': 2.7, 'pear': 0.9, 'papaya': 2.95, 'pomegra': 4.95}

quantity_list = {'apple': 5, 'orange': 5, 'watermel': 1, 'pineap': 2, 'pear': 10, 'papaya': 1, 'pomegra': 2}

import price_info as price


def test_total_cost():
    test = 46.75
    total_cost = price.total_cost_shopping()
    assert (total_cost == test)


def test_fruit_cost():
    test = 9.0
    fruit_cost = price.cost_of_fruits('pear', 10)
    assert (fruit_cost == test)



