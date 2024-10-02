import pytest

from school_class import SchoolClass
from student import Student
from studentreport import StudentReport


@pytest.fixture
def a_class():
    return SchoolClass('Musterklasse 23 A')


@pytest.fixture
def a_report():
    return StudentReport()


def test_school_class_init(a_class):
    """ tests the constructor """
    assert a_class.designation == 'Musterklasse 23 A'
    assert a_class.count_students() == 0


def test_single_student_added(a_class, a_report):
    """ tests adding a single student """
    peter = Student("Peter", a_report)
    a_class.add_student(peter)
    assert a_class.take_student(0) is peter
    assert peter.school_class is a_class


def test_take_invalid_student(a_class, a_report):
    """ tests adding a single student """
    peter = Student("Peter", a_report)
    a_class.add_student(peter)
    with pytest.raises(IndexError):
        a_class.take_student(3)


def test_multi_student_added(a_class, a_report):
    """ tests adding multiple students """
    for idx in range(4):
        a_class.add_student(Student('A', a_report))
    assert a_class.count_students() == 4


def test_too_many_student_added(a_class, a_report):
    """ tests adding more than 20 students """
    for idx in range(20):
        a_class.add_student(Student('A', a_report))
    with pytest.raises(OverflowError):
        a_class.add_student(Student('B', a_report))
    assert a_class.count_students() == 20


def test_student_list(a_class, a_report):
    """ tests showing the list of all students in a schoolclass """
    a_class.add_student(Student('Max', a_report))
    a_class.add_student(Student('Mia', a_report))
    a_class.add_student(Student('Cem', a_report))
    a_class.add_student(Student('Ali', a_report))
    output = a_class.show_student_list()
    assert output == 'Max\nMia\nCem\nAli\n'