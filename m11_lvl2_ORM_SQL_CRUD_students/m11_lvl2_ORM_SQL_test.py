import sqlite3
import unittest
from m8plvl3 import Students, Courses, Student_courses


# name='Олег', surname='Ступенькин', age=21, city='Moscow'

# name='C#', time_start='25.11.23', time_end='25.03.24'

# name='Эраст', surname='Времянкин', age=22, city='Tula'


class TestORMSystem(unittest.TestCase):
#Тестируем ORM систему с проверкой через SQL-запрос

    def test_add_student(self):
        # Добавление студента
        student = Students.create(name='Олег', surname='Ступенькин', age=21, city='Moscow')
        student.save()

        # Проверка, что студент был добавлен
        conn = sqlite3.connect('StudyDBORM_test.sqlite')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE (name='Олег' and surname='Ступенькин' and age=21 and city='Moscow')")
        result = cursor.fetchone()
        conn.close()
        self.assertIsNotNone(result)

    def test_add_course(self):
        # Добавление курса
        course = Courses.create(name='C#', time_start='25.11.23', time_end='25.03.24')
        course.save()

        # Проверка, что курс был добавлен
        conn = sqlite3.connect('StudyDBORM_test.sqlite')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM courses WHERE (name='C#' and time_start='25.11.23' and time_end='25.03.24')")
        result = cursor.fetchone()
        conn.close()
        self.assertIsNotNone(result)

    def test_delete_student(self):
        # Добавление студента
        student = Students.create(name='Эраст', surname='Времянкин', age=22, city='Tula')
        student.save()

        # Удаление студента
        Students.delete().where(Students.name == 'Эраст', Students.surname == 'Времянкин', Students.age == 22, Students.city == 'Tula').execute()

        # Проверка, что студент был удален
        conn = sqlite3.connect('StudyDBORM_test.sqlite')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE (name='Эраст' and surname='Времянкин' and age=22 and city='Tula')")
        result = cursor.fetchone()
        conn.close()
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()