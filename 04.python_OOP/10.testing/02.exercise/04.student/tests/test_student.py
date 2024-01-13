from project.student import Student

from unittest import TestCase, main


class TestStudent(TestCase):
    def setUp(self):
        self.student = Student('testName',
                               {
                                   'programming': ['note1', 'note2'],
                                   'IT': []
                                       })

    def test_init(self):
        self.assertEqual('testName', self.student.name)
        self.assertEqual({
                        'programming': ['note1', 'note2'],
                        'IT': []
                        }, self.student.courses)

    def test_init_no_courses(self):
        student = Student('a')
        self.assertEqual('a', student.name)
        self.assertEqual({}, student.courses)

    def test_enroll_existing(self):
        msg = self.student.enroll('programming', ['note3'], 'N')
        self.assertEqual(['note1', 'note2', 'note3'], self.student.courses['programming'])
        self.assertEqual(msg, 'Course already added. Notes have been updated.')

    def test_enroll_new_notes_y(self):
        msg = self.student.enroll('Physics', ['note1', 'note2'], 'Y')
        self.assertEqual(msg, 'Course and course notes have been added.')
        self.assertEqual({
            'programming': ['note1', 'note2'],
            'IT': [],
            'Physics': ['note1', 'note2']
        }, self.student.courses)

    def test_enroll_new_notes_empty_string(self):
        msg = self.student.enroll('Physics', ['note1', 'note2'])
        self.assertEqual(msg, 'Course and course notes have been added.')
        self.assertEqual({
            'programming': ['note1', 'note2'],
            'IT': [],
            'Physics': ['note1', 'note2']
        }, self.student.courses)

    def test_enroll_new_no_notes(self):
        msg = self.student.enroll('Physics', ['test'], 'N')
        self.assertEqual('Course has been added.', msg)
        self.assertEqual({
            'programming': ['note1', 'note2'],
            'IT': [],
            'Physics': []
        }, self.student.courses)

    def test_add_notes_valid(self):
        msg = self.student.add_notes('IT', 'testing')
        self.assertEqual('Notes have been updated', msg)
        self.assertEqual(['testing'], self.student.courses['IT'])

    def test_add_notes_invalid_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes('Geography', ['something'])

        self.assertEqual('Cannot add notes. Course not found.', str(ex.exception))

    def test_leave_course_valid(self):
        msg = self.student.leave_course('IT')
        self.assertEqual(msg, 'Course has been removed')
        self.assertEqual(self.student.courses, {'programming': ['note1', 'note2']})
        self.assertTrue('IT' not in self.student.courses)

    def test_leave_course_invalid(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course('Physics')
        self.assertEqual('Cannot remove course. Course not found.', str(ex.exception))


if __name__ == '__main__':
    main()
