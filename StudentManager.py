from methods import addStudent, exitProgram,showAllStudents,searchStudent, showTopper

#Get input from the user.
# name=input (("Enter the name of the student: " ))
# age=int(input("Enter the age of the student: "))
# marks=int(input("Enter the marks of the student: ")) 

# Call addStudent(...) to create the dictionary.
# student = addStudent(name,age,marks)

#empty list to store student dictionaries.
students = []

#create a menu  
MENU = """
1. Add Student
2. Show All Students
3. Search Student
4. Show Topper
5. Exit
"""

#While loop to display the menu and get user choice.

while True:
    print(MENU)
    choice = input("Enter your choice: ")

    if choice == "1":
        name=input (("Enter the name of the student: " ))
        age=int(input("Enter the age of the student: "))
        marks=int(input("Enter the marks of the student: "))

        student = addStudent(name,age,marks)
        students.append(student)

        print("Student added successfully.")
       

    elif choice == "2":
        showAllStudents(students)
        pass

    elif choice == "3":
        name = input("Enter the name of the student to search: ")
        student = searchStudent(students, name)
        if student== None:
            print("Student not found.")
        else:
            print(f"\nName: {student['name']}\nAge: {student['age']}\nMarks: {student['marks']}")
        pass

    elif choice == "4":
        showTopper(students)
        pass

    elif choice == "5":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
