class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        avg_grade = self.get_avg_grade()
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_grade:.1f}'

    def get_avg_grade(self):
        if not self.grades:
            return 0
        total_grades = sum(sum(grades) for grades in self.grades.values())
        count = sum(len(grades) for grades in self.grades.values())
        return total_grades / count if count != 0 else 0

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.get_avg_grade() < other.get_avg_grade()
        return NotImplemented


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            student.grades.setdefault(course, []).append(grade)
        else:
            return 'Ошибка'


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in lecturer.courses_attached
            and course in self.courses_in_progress):
            lecturer.grades.setdefault(course, []).append(grade)
        else:
            return 'Ошибка'

    def __str__(self):
        avg_grade = self.get_avg_grade()
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {avg_grade:.1f}\n'
                f'Курсы в процессе изучения: {courses_in_progress}\n'
                f'Завершенные курсы: {finished_courses}')

    def get_avg_grade(self):
        if not self.grades:
            return 0
        total_grades = sum(sum(grades) for grades in self.grades.values())
        count = sum(len(grades) for grades in self.grades.values())
        return total_grades / count if count != 0 else 0

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.get_avg_grade() < other.get_avg_grade()
        return NotImplemented


# Функции для подсчёта средних оценок
def average_student_grade(students, course):
    total_grades = 0
    count = 0
    for student in students:
        if course in student.grades:
            total_grades += sum(student.grades[course])
            count += len(student.grades[course])
    return total_grades / count if count != 0 else 0


def average_lecturer_grade(lecturers, course):
    total_grades = 0
    count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades += sum(lecturer.grades[course])
            count += len(lecturer.grades[course])
    return total_grades / count if count != 0 else 0


# Полевые испытания
# Студенты
# student1 = Student('Ruoy', 'Eman', 'male')
# student1.courses_in_progress += ['Python', 'Git']
# student1.finished_courses += ['Введение в программирование']
#
# student2 = Student('Jane', 'Doe', 'female')
# student2.courses_in_progress += ['Python']
# student2.finished_courses += ['Git']
#
# # Лекторы
# lecturer1 = Lecturer('John', 'Smith')
# lecturer1.courses_attached += ['Python']
#
# lecturer2 = Lecturer('Alice', 'Brown')
# lecturer2.courses_attached += ['Git']
#
# # Проверяющие
# reviewer1 = Reviewer('Some', 'Buddy')
# reviewer1.courses_attached += ['Python']
#
# reviewer2 = Reviewer('Ann', 'Smith')
# reviewer2.courses_attached += ['Git']
#
# # Выставляем оценки
# reviewer1.rate_hw(student1, 'Python', 9)
# reviewer1.rate_hw(student1, 'Python', 10)
# reviewer1.rate_hw(student2, 'Python', 8)
#
# reviewer2.rate_hw(student1, 'Git', 7)
#
# student1.rate_lecturer(lecturer1, 'Python', 10)
# student1.rate_lecturer(lecturer1, 'Python', 9)
# student2.rate_lecturer(lecturer1, 'Python', 8)
#
# student1.rate_lecturer(lecturer2, 'Git', 10)
#
# # Вывод результатов
# print(reviewer1)
# print(lecturer1)
# print(student1)
#
# print(f'Средняя оценка студентов по Python: {average_student_grade([student1, student2], "Python"):.1f}')
# print(f'Средняя оценка лекторов по Python: {average_lecturer_grade([lecturer1, lecturer2], "Python"):.1f}')
#
# # Сравнение студентов и лекторов
# print(student1 > student2)  # True/False
# print(lecturer1 < lecturer2)  # True/False
