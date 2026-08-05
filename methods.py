def addStudent(name,age,marks):
    student = {
        "name": name,
        "age": age,
        "marks": marks
    }
    return student

def showAllStudents(students):
    if not students:
        print("No students found.")
        return

    for student in students:
        print(f"Name: {student['name']}, Age: {student['age']}, Marks: {student['marks']}")

def searchStudent(students, name):
    for student in students:
        if student['name'].lower() == name.lower():
        
            return student
    return None
def showTopper(students):
    if not students:
        print("No students found.")
        return

    topper = max(students, key=lambda student: student['marks'])
    print(f"Topper: {topper['name']}, Age: {topper['age']}, Marks: {topper['marks']}")






