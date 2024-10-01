""" Provides the Subject-class """
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from grade import Grade


class Subject:
    """
    A school subject for the grade report of one student

    Attributes
    ----------
    name: String
        The subject name
    grades: List
        A list of grades
    """

    def __init__(self, name):
        self._name = name
        self._grades = []

    def add_grade(self, grade: Grade) -> None:
        """
        adds a grade to the grades list
        :param: grade(Grade) the grade-object to add
        :raises: OverflowError  if more than 4 grades are added to the list
        """
        if self.count_grades() < 4:
            self._grades.append(grade)
        else:
            raise OverflowError

    def take_grade(self, index: int) -> Grade:
        """
        returns the grade identified by the index
        :param: index(int):  the index of the grade
        :raises: IndexError: if the index does not exist
        """
        if index < self.count_grades():
            return self._grades[index]
        raise IndexError

    def count_grades(self) -> int:
        """
        counts the number of grades in the list
        :return: size of the list(int)
        """
        return len(self._grades)

    @property
    def average(self) -> float:
        """
        calculates the average of all grades in the list or 0 if the grades-list ist empty
        :return: average grade(float)
        """
        if self.count_grades() == 0:
            return 0.0
        else:
            total = 0.0
            for number in range(self.count_grades()):
                total += self.take_grade(number).value
            return total / self.count_grades()

    @property
    def name(self) -> str:
        """ returns the name """
        return self._name
