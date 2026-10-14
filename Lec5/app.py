# ==========================================
# Python for Beginners
# Lecture 5: Data Types in Python
# ==========================================

# Lecture Contents:
# 1. What Are Data Types?
# 2. String (str)
# 3. Integer (int)
# 4. Float (float)
# 5. Boolean (bool)
# 6. Checking Data Types Using type()
# 7. Practical Example: Student Profile
# 8. Practice Task: About Me

# ==========================================

name = "Mohamed"
age = 20
grade = 99.6
is_student = True

#String => str

Myname = "Mohamed Sayed" # '' => ""
test = "Mohamed"
country = "Egypt"
massage = "Welcome to python"

# print(Myname)
# print(country)
# print(massage)
#integer => int

age = 20 # integer
student_count = -30
Year = 2024

# print(age)
# print(student_count)
# print(Year)

#Float => float

price = 99.99 # 369.99 => 369
weight = 75.5 

# print(price)
# print(weight)



#Boolean => Yes Or No ?

is_student = True # 1

is_graduted = False # 0


# print(is_student)
# print(is_graduted)

#Type()

# print(type(name)) # str
# print(type(age)) # int
# print(type(price)) # float
# print(type(is_student)) # bool

#Student Profile

Student_name = "Mohamed Sayed"
Student_age = 20
Student_grade = 99.6
is_student = True

print("Student Name: ", Student_name)
print("Student Age: ", Student_age)
print("Student Grade: ", Student_grade)
print("Is Student: ", is_student)

print(type(Student_name)) #=> str
print(type(Student_age))# => int
print(type(Student_grade))# => float
print(type(is_student))# => bool