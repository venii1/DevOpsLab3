import employee_info as employ

item = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
    {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
]


def test_avg_salary():
    test = (50000+60000+56000+70000+65000+60000)/6
    actual = employ.calculate_average_salary()
    assert (actual == test)


def test_employee_dept():
    test = [item[3], item[4]]
    result = employ.get_employees_by_dept('Engineering')
    assert (result == test)


def test_age_range():
    test = [item[0], item[1], item[2]]
    result = employ.get_employees_by_age_range(19, 31)
    assert (result == test)

