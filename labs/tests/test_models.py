import datetime
from django.test import TestCase
from ..models import Course, Lab, Student
from django.contrib.auth.models import User


def create_test_user(username='test_user', email='user@example.com',
                     password='test', first_name='test', last_name='user'):
    return User.objects.create_user(
        username=username,
        email=email,
        password=password,
    )


class CourseModelTest(TestCase):

    @staticmethod
    def create_course(cid='CZ3001', year=2019, semester=1,
                      course_name='ADVANCED COMPUTER ARCHITECTURE'):
        return Course.objects.create(cid=cid, year=year, semester=semester,
                                     course_name=course_name)

    def setUp(self):
        self.course = self.create_course()

    def test_course(self):
        self.assertEqual(self.course.cid, 'CZ3001')
        self.assertEqual(self.course.year, 2019)
        self.assertEqual(self.course.course_name, 'ADVANCED COMPUTER ARCHITECTURE')

    def test_default_year(self):
        oop_course = Course.objects.create(cid='CZ2004', semester=1, course_name='OBJECT ORIENTED DESIGN')
        this_year = datetime.date.today().year
        self.assertEqual(oop_course.year, this_year)


class LabModelTest(TestCase):
    def setUp(self):
        self.course = CourseModelTest.create_course()
        self.instructor = create_test_user()
        self.lab = Lab.objects.create(group='TS5', course=self.course)
        self.testuser1 = create_test_user(username='testuser1')
        self.testuser2 = create_test_user(username='testuser2')

    def test_lab(self):
        self.assertEqual(self.lab.group, 'TS5')

    def test_getLabsByCourse(self):
        Lab.objects.create(group='TS6', course=self.course)
        self.assertEqual(len(self.course.labs.all()), 2)

    def test_getLabsByInstructor(self):
        self.lab.instructors.add(self.testuser1, self.testuser2)
        self.assertEqual(len(self.lab.instructors.all()), 2)

    def test_getInstructorsByLabs(self):
        self.testuser1.labs.add(self.lab)
        self.assertEqual(len(self.testuser1.labs.all()), 1)


class StudentModelTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(mid='U1622102L', name='test',
                                              email='test@example', face_encoding=b'ab')

    def test_student(self):
        self.assertEqual(self.student.mid, 'U1622102L')
        self.assertEqual(self.student.face_encoding, b'ab')


class AttendanceModelTest(TestCase):
    # TODO
    pass


class SessionModelTest(TestCase):
    # TODO
    pass
