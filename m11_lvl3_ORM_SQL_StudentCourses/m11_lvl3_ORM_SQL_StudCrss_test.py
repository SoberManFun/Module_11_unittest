import sqlite3
import unittest
import m8plvl3


class TestORMAddStudent(unittest.TestCase):

    def test_add_student_to_course(self):
        # Добавление студента на курс
        m8plvl3.add_student_to_course(2, 2)

        # Проверка, что студент был добавлен на курс
        conn = sqlite3.connect('StudyDBORM_test.sqlite')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM student_courses WHERE student_id = 2 AND course_id = 2")
        result = cursor.fetchone()
        conn.close()
        self.assertIsNotNone(result)
        print(result)

class TestORMDelStudent(unittest.TestCase):

    def test_delete_student_from_course(self):
        # Удаление студента из курса
        m8plvl3.delete_student_from_course(2, 2)

        # Проверка, что студент был удален из курса
        conn = sqlite3.connect('StudyDBORM_test.sqlite')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM student_courses WHERE student_id = 2 AND course_id = 2")
        result = cursor.fetchone()
        conn.close()
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()