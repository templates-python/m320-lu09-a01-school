import pytest

from student import Student
from studentreport import StudentReport
from subject import Subject


@pytest.fixture
def student_report():
    return StudentReport()


@pytest.fixture
def mia(student_report):
    return Student('Mia', student_report)


@pytest.fixture
def mathe():
    return Subject('Mathe')

def test_initialisation(mia, student_report):
    """ tests the constructor """
    assert mia.name == 'Mia'
    assert mia.school_class is None
    assert mia.report is student_report

def test_relationship_to_classreport(mia, student_report):
    """ tests the reference between the student and the student-report """
    assert mia.report.student is mia
