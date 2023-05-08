import Lab2_bmi.bmi as bmi


def test_bmi_underweight():
    result = bmi.calculate_bmi(1.6, 30)
    assert (result == -1)


def test_bmi_normal():
    result = bmi.calculate_bmi(1.6, 50)
    assert (result == 0)


def test_bmi_overweight():
    result = bmi.calculate_bmi(1.6, 100)
    assert (result == 1)


