""" Provides the Grade-class"""
from datetime import datetime
from dataclasses import dataclass


@dataclass
class Grade:
    """
    A single grade for a student in one subject.
    All attribute values are set during construction of the object.

    Attributes
    ----------
    value: float
        the value of the grade must be >= 1.0 and <= 6.0
    date: datetime
        The date/time the grade was set
    """
    value: float = -1.0
    date: datetime = None

    def __post_init__(self):
        """
        validates the initial value
        :raises: ValueError: if the value is out of bounds
        """
        if self._value > 6.0 or self._value < 1.0:
            raise ValueError

    @property
    def value(self):
        """ returns the value for this grade"""
        return self._value

    @value.setter
    def value(self, value):
        """ sets the value for this grade """
        self._value = value

    @property
    def date(self):
        """ returns the date of this grade """
        return self._date

    @date.setter
    def date(self, value):
        """
        sets the date of this grade.
        If a string "(d)d.(m)m.(yy)yy" is provided, it converts it to DateTime
        :param: value(mixed): The date or None=now
        """

        if isinstance(value, datetime):
            self._date = value
        elif isinstance(value, str) and value != '':
            self._date = datetime.strptime(value,'%d.%m.%y')
        else:
            self._date = datetime.now()
