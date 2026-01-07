import student

def test_calculate_average():
    avg = student.calculate_average(85, 90, 95)
    assert avg == 90.0

def test_grade_S():
    assert student.calculate_grade(92) == "S"

def test_grade_A():
    assert student.calculate_grade(85) == "A"

def test_grade_B():
    assert student.calculate_grade(70) == "B"

def test_grade_C():
    assert student.calculate_grade(55) == "C"

def test_grade_D():
    assert student.calculate_grade(45) == "D"

def test_grade_F():
    assert student.calculate_grade(30) == "F"\
