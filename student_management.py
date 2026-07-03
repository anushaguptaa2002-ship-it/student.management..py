import json
import os

FILE_NAME = "student.json"

class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade
    
    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "grade": self.grade
        }
        
class StudentManager:
    def __init__(self):
        self.students = []
        self.load_data()
        
    def load_data(self):
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r") as file:
                try:
                    data = json.load(file)
                    for item in data:
                        self.students.append(
                            Student(
                                item["student_id"],
                                item["name"],
                                item["grade"]
                            )  
                        )
                        
                except:
                    self.students = []
    def save_data(self):
        data = []
        for student in self.students:
            data.append(student.to_dict())
        
        with open(FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)

    def add_student(self):
        student_id = input("Enter student ID: ")
        for student in self.students:
        
            if student.student_id == student_id:
                print("Student ID already exists!")
                return
            
        name = input("Enter student name: ")
        grade = input("Enter student grade: ")
        
        
        self.students.append(Student(student_id, name, grade))
        self.save_data()
        print("Student added successfully!")
        
        
    def display_students(self):
        if len(self.students) == 0:
            print("No students records found!")
            return
        print("\n------------------------------")
        print("ID\tName\t\tGrade")
        print("------------------------------")
        
        for student in self.students:
            print(student.student_id, "\t", student.name, "\t\t", student.grade)
            
        print("------------------------------")
    def search_student(self):
        student_id = input("Enter student ID: ")
        for student in self.students:
            if student.student_id == student_id:
                print("\nStudent found!")
                print("ID:", student.student_id)
                print("Name:", student.name)
                print("Grade:", student.grade)
                return
        print("Student ID not found!")
    def update_student(self):
        student_id = input("Enter student ID ")
        for student in self.students:
            if student.student_id == student_id:
                
                student.name = input("Enter new name: ")
                student.grade = input("Enter new grade: ")
                self.save_data()
                print("Student updated successfully!")
                return
            print("Student ID not found!")
    def delete_student(self):
        student_id = input("Enter student ID to delete: ")
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                self.save_data()
                print("Student deleted successfully!")
                return
        print("Student ID not found!")
    def total_students(self):
        print("Total Students :", len(self.students))
manager = StudentManager()
while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Total Students")
    print("7. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        manager.add_student()
    elif choice == "2":
        manager.display_students()
    elif choice == "3":
        manager.search_student()
    elif choice == "4":
        manager.update_student()
    elif choice == "5":
        manager.delete_student()
    elif choice == "6":
        manager.total_students()
    elif choice == "7":
        print("Thank you for using the Student Management System!")
        break
    else:
        print("Invalid choice. Please try again.")
           