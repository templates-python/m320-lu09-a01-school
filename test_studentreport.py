import pytest

from studentreport import StudentReport


@pytest.fixture
def subject_list():
    """ returns a list of subjects """
    return ['English', 'Math', 'History']


@pytest.fixture
def report_empty():
    """ returns an empty report """
    return StudentReport()


@pytest.fixture
def report_max_subjects(report_empty: StudentReport, subject_list):
    """ returns a report with the maximum number of subjects """
    for subject in subject_list:
        report_empty.add_subject(subject)
    return report_empty


def test_empty_report(report_empty):
    """ tests the constructor with an empty report"""
    assert len(report_empty._subjects) == 0
    assert report_empty.student is None


def test_add_subject(report_empty):
    """ tests adding a single subject """
    report_empty.add_subject('English')
    assert len(report_empty._subjects) == 1
    assert 'English' in report_empty._subjects


def test_add_multiple_subjects(report_max_subjects, subject_list):
    """ tests adding multiple subjects """
    assert len(report_max_subjects._subjects) == 3
    subject_set = set(report_max_subjects._subjects)
    assert set(subject_list) == subject_set


def test_max_subjects(report_max_subjects, subject_list):
    """ tests adding too many subjects """
    with pytest.raises(OverflowError):
        report_max_subjects.add_subject('too many subjects')
    assert report_max_subjects.count_subjects() == 3
    subject_set = set(report_max_subjects._subjects)
    assert set(subject_list) == subject_set


def test_take_valid(report_max_subjects):
    """ tests reading a subject with a valid index """
    subject = report_max_subjects.take_subject(1)
    assert subject == 'Math'

def test_take_invalid(report_empty):
    """ tests reading a subject with an valid index """
    report_empty.add_subject('English')
    with pytest.raises(IndexError):
        report_empty.take_subject(2)