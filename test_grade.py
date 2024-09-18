from datetime import datetime

import pytest

from grade import Grade


@pytest.fixture
def some_date():
    return datetime(2024, 8, 28)


def test_grade_init_valid(some_date):
    """ tests the constructor with valid data """
    grade = Grade(4.0, some_date)
    assert grade.value == 4.0
    grade = Grade(1.0, some_date)
    assert grade.value == 1.0
    grade = Grade(6.0, some_date)
    assert grade.value == 6.0


def test_grade_init_invalid(some_date):
    """ tests the constructor with invalid data """
    with pytest.raises(TypeError):
        Grade('a', some_date)


def test_grade_init_too_small():
    """ tests the constructor with an illegal grade """
    with pytest.raises(ValueError):
        Grade(0.5)


def test_grade_init_too_high():
    """ tests the constructor with an illegal grade """
    with pytest.raises(ValueError):
        Grade(7.0)