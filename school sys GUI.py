import tkinter as tk

class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

class SchoolSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def search_student(self, name):
        for student in self.students:
            if student.name == name:
                return student
        return None

school_system = SchoolSystem()

def add_student():
    name = name_entry.get()
    grade = grade_entry.get()
    age = age_entry.get()
    student = Student(name, grade, age)
    school_system.add_student(student)
    status_label.config(text="Student added")

def remove_student():
    name = name_entry.get()
    student = school_system.search_student(name)
    if student:
        school_system.remove_student(student)
        status_label.config(text="Student removed")
    else:
        status_label.config(text="Student not found")

def search_student():
    name = name_entry.get()
    student = school_system.search_student(name)
    if student:
        status_label.config(text=f"Name: {student.name}\nGrade: {student.grade}\nAge: {student.age}")
    else:
        status_label.config(text="Student not found")

root = tk.Tk()
root.geometry("300x350")
root.title("School System")

# create the name label and entry
name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

# create the grade label and entry
grade_label = tk.Label(root, text="Grade:")
grade_label.pack()
grade_entry = tk.Entry(root)
grade_entry.pack()

# create the age label and entry
age_label = tk.Label(root, text="Age:")
age_label.pack()
age_entry = tk.Entry(root)
age_entry.pack()

# create the add button
add_button = tk.Button(root, text="Add Student", command=add_student)
add_button.pack()

# create the remove button
remove_button = tk.Button(root, text="Remove Student", command=remove_student)
remove_button.pack()

# create the search button
search_button = tk.Button(root, text="Search Student", command=search_student)
search_button.pack()

# create the status label
status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
