""" Provides the class SchoolClass """


class SchoolClass:
    """
    A schoolclass with the students
    
    Attributes
    ----------
    students: List
        a list of student-objects
    designation: String
        the designation of this schoolclass
    """

    def __init__(self, designation):
        """
        constructs the object
        :param: designation(string): the designation of this schoolclass
        """
        self._designation = designation
        self._students = []

    def add_student(self, student):
        """
        adds a student to the students list
        :param: student(Student) the student-object to add
        :raises: OverflowError:  if the student-list is already full
        """
        if self.count_students() < 20:
            self._students.append(student)
        else:
            raise OverflowError

    def take_student(self, index):
        """
        returns the student identified by the index
        :param: index(int):  the index of the student
        :raises: IndexError: if the index does not exist
        """
        if index < self.count_students():
            return self._students[index]
        raise IndexError

    def count_students(self):
        """
        counts the number of students in the list
        :return: size of the list(int)
        """
        return len(self._students)

    def show_student_list(self):
        """ shows a list of all student names """
        output = ''
        for student in self._students:
            output += f'{student.name}\n'
        return output

    def show_student_report(self, name):
        """
        Shows the grades for the student identified by his name
        :param name: The name of the student to be shown
        :return:
        """
        print('----')
        for student in self._students:
            if student.name == name:
                return student.report.show_overview()
        return f'Student {name} nicht gefunden'

    @property
    def designation(self):
        """ returns the designation """
        return self._designation
