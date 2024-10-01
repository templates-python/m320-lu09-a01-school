""" Provides the student-object """
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from studentreport import StudentReport
    from school_class import SchoolClass


class Student:
    """
    A student in a schoolclass with subjects and grades

    Attributes
    ----------
    name: String
        The fullname of the student
    school_class: SchoolClass
        The schoolclass this student is part of
    report: StudentReport
        The report-object with the subjects and grades for this student
    """

    def __init__(self, name, student_report: StudentReport) -> None:
        """
        creates the object with references to the schoolclass and studentreport
        :param report: Referenz zum Zeugnis
        """
        self._name = name
        # create the two-way relationship between student and studentreport
        self._report = student_report
        student_report.student = self
        self._school_class = None  # this reference will be set later

    def show_report(self) -> StudentReport:
        """ returns the report for this student """
        return self.report

    @property
    def name(self) -> str:
        """
        Liefert den Namen des Studenten
        :return: Name des Studenten
        """
        return self._name

    @property
    def school_class(self) -> SchoolClass:
        """
        Liefert die Referenz der Klasse
        :return: Referenz der Klasse
        """
        return self._school_class

    @school_class.setter
    def school_class(self, school_class: SchoolClass) -> None:
        """
        sets the reference to the schoolclass
        """
        self._school_class = school_class

    @property
    def report(self) -> StudentReport:
        """
        gets the reference to the studentreport
        """
        return self._report
