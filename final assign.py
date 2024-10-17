# Base class for Human (common properties between students and teachers)
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"{self.name}, Age: {self.age}"

# Student class inheriting from Human
class Student(Human):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.enrolled_sections = []

    def enroll_in_section(self, section):
        self.enrolled_sections.append(section)
        section.add_student(self)

    def get_enrolled_sections(self):
        return [section.name for section in self.enrolled_sections]

# Teacher class inheriting from Human
class Teacher(Human):
    def __init__(self, name, age, teacher_id):
        super().__init__(name, age)
        self.teacher_id = teacher_id
        self.assigned_sections = []

    def assign_to_section(self, section):
        self.assigned_sections.append(section)
        section.assign_teacher(self)

    def get_assigned_sections(self):
        return [section.name for section in self.assigned_sections]

# Section class
class Section:
    def __init__(self, name, time):
        self.name = name
        self.time = time
        self.students = []
        self.teacher = None

    def add_student(self, student):
        self.students.append(student)

    def assign_teacher(self, teacher):
        self.teacher = teacher

    def get_students(self):
        return [student.name for student in self.students]

    def get_teacher(self):
        return self.teacher.name if self.teacher else "No teacher assigned"

# University class
class University:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []
        self.sections = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def create_section(self, name, time):
        section = Section(name, time)
        self.sections.append(section)
        return section

    def get_students(self):
        return [student.name for student in self.students]

    def get_teachers(self):
        return [teacher.name for teacher in self.teachers]

    def get_sections(self):
        return [section.name for section in self.sections]

# Example usage
# Create a university
uni = University("XYZ University")

# Create students
student1 = Student("Alice", 20, "S001")
student2 = Student("Bob", 22, "S002")

# Create a teacher
teacher1 = Teacher("Dr. Smith", 45, "T001")

# Add students and teacher to the university
uni.add_student(student1)
uni.add_student(student2)
uni.add_teacher(teacher1)

# Create a section
section1 = uni.create_section("Math 101", "10:00 AM")

# Enroll students in the section
student1.enroll_in_section(section1)
student2.enroll_in_section(section1)

# Assign the teacher to the section
teacher1.assign_to_section(section1)

# Output university details
print("University:", uni.name)
print("Students:", uni.get_students())
print("Teachers:", uni.get_teachers())
print("Sections:", uni.get_sections())

# Output section details
print(f"\nSection: {section1.name}")
print(f"Time: {section1.time}")
print(f"Teacher: {section1.get_teacher()}")
print(f"Enrolled Students: {section1.get_students()}")

# Output student and teacher details
print("\nStudent1 enrolled sections:", student1.get_enrolled_sections())
print("Teacher1 assigned sections:", teacher1.get_assigned_sections())




