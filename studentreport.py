""" Provides the StudentReport-class """
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from student import Student
    from subject import Subject


class StudentReport:
    """
    The grade reports for a student with the subjects and grades
    """

    def __init__(self) -> None:
        """
        initializes the student report with empty attributs
        """
        self._subjects = []
        self._student = None

    def show_overview(self) -> str:
        """
        shows an overview of all subjects and average marks for the student.

        :return: overview report
        """
        output = 'Zeugnis für: '
        # Needs a student-object to show the name.
        if self._student is not None:
            output += self._student.name

        # List all subjects with the average mark.
        for subject in self._subjects:
            output += f'\n\t  {subject.name:<10}:  {subject.average:.2f}'
        return output

    def show_details(self) -> str:
        """
        shows the details of all subjects and marks for the student.

        :return: detailed report (str)
        """
        output = ''
        for subject in self._subjects:
            output += f'Fach: {subject.name:<10} mit {subject.count_grades()} Noten\n'
            for count in range(subject.count_grades()):
                grade = subject.take_grade(count)
                output += f' - {count + 1}: {grade.value:.2f} am {grade.date:%d.%m.%Y}\n'
            output += f' Schnitt: {subject.average:.2f}\n'
        return output

    def add_subject(self, subject: Subject) -> None:
        """
        adds a subject to the list, if there are less than 3 subjects in the list

        :param: subject (Subject): the new subject to be added.
        :raises: OverflowError: if the list is already full
        """
        if len(self._subjects) < 3:
            self._subjects.append(subject)
        else:
            raise OverflowError

    def take_subject(self, index: int) -> Subject:
        """
        returns the subject at the specified index, if it exists.

        :param: index (int): the index of the subject.
        :return: Subject or None
        :raises: IndexError  if the index doesn't exists in the list
        """
        if index < len(self._subjects):
            return self._subjects[index]
        raise IndexError

    def count_subjects(self) -> int:
        """
        counts the number of subjects in the list

        :return: length (int)
        """
        return len(self._subjects)

    @property
    def student(self) -> Student:
        """ returns the student-object """
        return self._student

    @student.setter
    def student(self, value: Student):
        """ Sets the student-object """
        self._student = value
