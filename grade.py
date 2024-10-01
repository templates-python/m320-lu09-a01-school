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

    def __post_init__(self) -> None:
        """
        validates the initial value
        :raises: ValueError: if the value is out of bounds
        """
        if self._value > 6.0 or self._value < 1.0:
            raise ValueError


    @property
    def value(self) -> float:
        """ returns the value for this grade"""
        return self._value


    @value.setter
    def value(self, value: float) -> None:
        """ sets the value for this grade """
        self._value = value


    @property
    def date(self) -> datetime:
        """ returns the date of this grade """
        return self._date


    @date.setter
    def date(self, value: datetime|str) -> None:
        """
        sets the date of this grade.
        If a string "(d)d.(m)m.(yy)yy" is provided, it converts it to DateTime
        :param: value(mixed): The date or None=now
        """

        if isinstance(value, datetime):
            self._date = value
        elif isinstance(value, str) and value != '':
            self._date = datetime.strptime(value, '%d.%m.%y')
        else:
            self._date = datetime.now()
