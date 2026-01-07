import pytest
from student_detils import calculate_grade

@pytest.mark.parametrize(
    "avg, expected_grade",
    [
        (95, "S"),   # >= 90
        (90, "S"),
        (89.9, "A"), # >= 80
        (85, "A"),
        (70, "B"),   # >= 65
        (65, "B"),
        (60, "C"),   # >= 50
        (50, "C"),
        (45, "D"),   # >= 40
        (40, "D"),
        (39.9, "F"), # < 40
        (20, "F"),
    ]
)
def test_calculate_grade(avg, expected_grade):
    assert calculate_grade(avg) == expected_grade
