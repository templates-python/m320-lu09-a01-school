from datetime import datetime

import pytest

from grade import Grade
from subject import Subject


@pytest.fixture
def subject():
    """ returns the subject 'Mathe' """
    return Subject('Mathe')


@pytest.fixture
def grade():
    """ returns a grade """
    return Grade(4.0, '1.2.33')


def test_empty_subject(subject):
    """ tests the constructor without grades """
    assert subject.name == 'Mathe'
    assert subject.count_grades() == 0


def test_single_grade_added(subject):
    """ tests adding a single grade"""
    subject.add_grade(Grade(3.0, '1.2.33'))
    assert subject.count_grades() == 1


def test_multi_grade_added(subject):
    """ tests adding multiple grades """
    subject.add_grade(Grade(3.0, '1.2.33'))
    subject.add_grade(Grade(5.0, '1.2.44'))
    subject.add_grade(Grade(4.0, '1.2.55'))
    assert subject.count_grades() == 3


def test_too_many_grades_added(subject):
    """ tests adding too many grades """
    subject.add_grade(Grade(3.0, '1.2.33'))
    subject.add_grade(Grade(5.0, '1.2.44'))
    subject.add_grade(Grade(4.0, '1.2.55'))
    subject.add_grade(Grade(1.0, '1.2.44'))
    with pytest.raises(OverflowError):
        subject.add_grade(Grade(2.0, '1.2.55'))
    assert subject.count_grades() == 4


def test_get_grade_valid(subject, grade):
    """ tests reading a grade with a valid index """
    subject.add_grade(grade)
    assert subject.take_grade(0).value == grade.value
    assert subject.take_grade(0).date == grade.date


def test_get_grade_invalid(subject, grade):
    """ tests reading a grade with an invalid index """
    subject.add_grade(grade)
    with pytest.raises(IndexError):
        subject.take_grade(1)


def test_multi_grade(subject):
    """ tests reading multiple grades and their attributes """
    subject.add_grade(Grade(3.0, '1.2.33'))
    subject.add_grade(Grade(5.0, '1.2.44'))
    subject.add_grade(Grade(4.0, '1.2.55'))
    assert subject.take_grade(0).value == 3.0
    assert subject.take_grade(1).value == 5.0
    assert subject.take_grade(2).value == 4.0
    assert subject.take_grade(0).date == datetime(2033, 2, 1)
    assert subject.take_grade(1).date == datetime(2044, 2, 1)
    assert subject.take_grade(2).date == datetime(2055, 2, 1)


def test_average_without_grade(subject):
    """ tests the average without any grades """
    assert subject.average == 0


def test_single_grade_average(subject):
    """ tests the average with a single grade """
    subject.add_grade(Grade(3.0, '1.2.33'))
    assert subject.average == 3.0


def test_average(subject):
    """ tests the average with multiple grades """
    subject.add_grade(Grade(2.0, '1.2.33'))
    subject.add_grade(Grade(5.0, '1.2.44'))
    subject.add_grade(Grade(4.0, '1.2.55'))
    subject.add_grade(Grade(1.0, '1.2.44'))
    assert subject.average == 3.0
