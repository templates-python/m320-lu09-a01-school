from grade import Grade
from school_class import SchoolClass
from student import Student
from studentreport import StudentReport
from subject import Subject


def main():
    """ Let's create some data and see how it works """
    # In the beginning, there was a class
    the_class = SchoolClass('IM993a')

    # Let there be some studentreports
    report_moritz = StudentReport()
    create_subject_list(report_moritz)

    report_pia = StudentReport()
    create_subject_list(report_pia)

    report_cem = StudentReport()
    create_subject_list(report_cem)

    # And some students, of course
    moritz = Student('Moritz', report_moritz)
    pia = Student('Pia', report_pia)
    cem = Student('Cem', report_cem)

    # Add those students to the class
    the_class.add_student(moritz)
    the_class.add_student(pia)
    the_class.add_student(cem)
    # And print the list of students in this class
    print(the_class.show_student_list())

    # Next we need a couple of grades
    report_moritz.take_subject(0).add_grade(Grade(4.0, '1.1.11'))
    report_moritz.take_subject(0).add_grade(Grade(4.5, '2.2.22'))
    report_moritz.take_subject(1).add_grade(Grade(4.0, '3.3.33'))
    report_moritz.take_subject(1).add_grade(Grade(6.0, '4.4.44'))
    report_moritz.take_subject(1).add_grade(Grade(5.0, '5.5.55'))
    report_moritz.take_subject(2).add_grade(Grade(4.5, '6.6.66'))
    report_moritz.take_subject(2).add_grade(Grade(5.0, '7.7.77'))
    report_moritz.take_subject(2).add_grade(Grade(5.0, '8.8.88'))
    report_moritz.take_subject(2).add_grade(Grade(5.5, '9.9.99'))

    report_pia.take_subject(0).add_grade(Grade(5.5, '1.1.11'))
    report_pia.take_subject(0).add_grade(Grade(5.5, '2.2.22'))
    report_pia.take_subject(1).add_grade(Grade(4.5, '3.3.33'))
    report_pia.take_subject(1).add_grade(Grade(6.0, '4.4.44'))
    report_pia.take_subject(1).add_grade(Grade(5.5, '5.5.55'))
    report_pia.take_subject(2).add_grade(Grade(4.0, '6.6.66'))
    report_pia.take_subject(2).add_grade(Grade(5.5, '7.7.77'))
    report_pia.take_subject(2).add_grade(Grade(6.0, '8.8.88'))
    report_pia.take_subject(2).add_grade(Grade(5.5, '9.9.99'))

    report_cem.take_subject(0).add_grade(Grade(5.0, '1.1.11'))
    report_cem.take_subject(0).add_grade(Grade(3.5, '2.2.22'))
    report_cem.take_subject(1).add_grade(Grade(5.5, '3.3.33'))
    report_cem.take_subject(1).add_grade(Grade(6.0, '4.4.44'))
    report_cem.take_subject(1).add_grade(Grade(5.0, '5.5.55'))
    report_cem.take_subject(2).add_grade(Grade(4.5, '6.6.66'))
    report_cem.take_subject(2).add_grade(Grade(6.0, '7.7.77'))
    report_cem.take_subject(2).add_grade(Grade(6.0, '8.8.88'))
    report_cem.take_subject(2).add_grade(Grade(5.5, '9.9.99'))

    print(the_class.show_student_report('Moritz'))
    print(the_class.show_student_report('Pia'))
    print(the_class.show_student_report('Cem'))
    print(the_class.show_student_report('Theo'))

    # Finally we show the detailed report for one student

    print(report_cem.show_details())


def create_subject_list(actual_report):
    """ creates a list of subjects """
    actual_report.add_subject(Subject('Mathe'))
    actual_report.add_subject(Subject('Deutsch'))
    actual_report.add_subject(Subject('Turnen'))


if __name__ == '__main__':
    main()
