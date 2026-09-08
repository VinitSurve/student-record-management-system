students = []

def display_menu():
    print("\n========================================")
    print("       STUDENT RECORD MANAGEMENT")
    print("==========================================")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    print("==========================================")

def add_student():
    print("\n---------- Add Student ----------")

    student_id = int(input("Enter Student ID: "))
    name = input("Enter Student Name: ")
    age = int(input("Enter Student Age: "))
    course = input("Enter Course: ")
    email = input("Enter Email: ")


    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course,
        "email": email
    }

    students.append(student)

    print("\nStudent added successfully!")

def view_students():
    print("\n---------- Student Records ----------")

    if len(students) == 0:
        print("No student record found!")
        return
    
    for student in students:
        print("Student ID: ", student["id"])
        print("Name: ", student["name"])
        print("Age: ", student["age"])
        print("Course: ", student["course"])
        print("Email: ", student["email"])
        print("------------------------------------")

def search_student():
    print("\n---------- Search Student ----------")

    search_id = int(input("Enter Student ID to search: "))

    for student in students:
        if student["id"] == search_id:
            print("Student Found!")
            print("Student ID: ", student["id"])
            print("Name: ", student["name"])
            print("Age: ", student["age"])
            print("Course: ", student["course"])
            print("Email: ", student["email"])
            print("------------------------------------")
            return
    
    print("Student not found!")

def update_student():
    print("\n---------- Update Student ----------")

    update_id = int(input("Enter Student ID to update: "))

    for student in students:
        if student["id"] == update_id:
            print("Student Found!")
            print("Enter New Details: ")

            print("Student ID: ", student["id"])
            print("Name: ", student["name"])
            print("Age: ", student["age"])
            print("Course: ", student["course"])
            print("Email: ", student["email"])
            print("------------------------------------")
            return
    
    print("Student not found!")

def delete_student():
    print("\n---------- Delete Student ----------")

    delete_id = int(input("Enter Student ID to delete: "))

    for student in students:
        if student["id"] == delete_id:
            students.remove(student)
            print("\nStudent deleted successfully!")
            return

    print("\nStudent not found.")
    

def main():
    while True:
        display_menu()
        choice = input("Enter you choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exit")
            break
        else:
            print("Invalid choice. Please try again!")

main()