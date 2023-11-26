from peewee import *


conn = SqliteDatabase('StudyDBORM_test.sqlite')


class BaseModel(Model):
	class Meta:
		database = conn


class Students(BaseModel):
	name = CharField()
	surname = CharField()
	age = IntegerField()
	city = CharField()


class Courses(BaseModel):
	name = CharField()
	time_start = DateField(formats=['%d:%m:%y'])
	time_end = DateField(formats=['%d:%m:%y'])


class Student_courses(BaseModel):
	student = ForeignKeyField(Students)
	course = ForeignKeyField(Courses)


with conn:
	conn.create_tables([Students, Courses, Student_courses])

result = Students.select().count()
if result == 0:
	student1 = Students.create(name='Max', surname='Brooks', age=24, city='Spb')
	student2 = Students.create(name='John', surname='Stones', age=15, city='Spb')
	student3 = Students.create(name='Andy', surname='Wings', age=45, city='Manhester')
	student4 = Students.create(name='Kate', surname='Brooks', age=34, city='Spb')

result = Courses.select().count()
if result == 0:
	course1 = Courses.create(name='Python', time_start='21.07.21', time_end='21.08.21')
	course2 = Courses.create(name='java', time_start='13.07.21', time_end='16.08.21')

result = Student_courses.select().count()
if result == 0:
	student_course1 = Student_courses.create(student=student1, course=course1)
	student_course2 = Student_courses.create(student=student2, course=course1)
	student_course3 = Student_courses.create(student=student3, course=course1)
	student_course4 = Student_courses.create(student=student4, course=course2)

students_over_30 = Students.select().where(Students.age > 30)
print('\nСтуденты старше 30 лет:')
for student in students_over_30:
	print(student.name, student.surname)

students_python_course = (
	Students
	.select()
	.join(Student_courses)
	.join(Courses)
	.where(Courses.name == 'Python')
)
print('\nСтуденты, проходящие курс по Python:')
for student in students_python_course:
	print(student.name, student.surname)

students_python_spb = (
	Students
	.select()
	.join(Student_courses)
	.join(Courses)
	.where(Courses.name == 'Python', Students.city == 'Spb')
)
print('\nСтуденты, проходящие курс по Python и из Spb:')
for student in students_python_spb:
	print(student.name, student.surname)

conn.commit()	
conn.close()