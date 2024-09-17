""" Provides the StudentReport-class """
class StudentReport:
    """
    The grade reports for a student with the subjects and grades
    """
    def __init__(self):
        """
        initializes the student report with empty attributs
        """
        self._subjects = []
        self._student = None

    def show_overview(self):
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
            output += f'\n\t  {subject.name}:  {subject.average}'
        return output

    def show_details(self):
        """
        shows the details of all subjects and marks for the student.

        :return: detailed report (str)
        """
        output = ''
        for subject in self._subjects:
            output += f'\tFach: {subject.name} mit {subject.count_grades()} Noten'
            for count in range(subject.count_grades()):
                grade = subject.take_grade(count)
                output += f'\t\t{count + 1} : {grade.value} {grade.date}'
            output += f'\tSchnitt: {subject.average}\n'
        return output

    def add_subject(self, subject):
        """
        adds a subject to the list, if there are less than 3 subjects in the list

        :param: subject (Subject): the new subject to be added.
        :raises: OverflowError: if the list is already full
        """
        if len(self._subjects) < 3:
            self._subjects.append(subject)
        else:
            raise OverflowError

    def take_subject(self, index):
        """
        returns the subject at the specified index, if it exists.

        :param: index (int): the index of the subject.
        :return: Subject or None
        :raises: IndexError  if the index doesn't exists in the list
        """
        if index < len(self._subjects):
            return self._subjects[index]
        raise IndexError

    def count_subjects(self):
        """
        counts the number of subjects in the list

        :return: length (int)
        """
        return len(self._subjects)

    @property
    def student(self):
        """ returns the student-object """
        return self._student

    @student.setter
    def student(self, value):
        """ Sets the student-object """
        self._student = value
