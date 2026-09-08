import json

students = []


def load_records():
    global students

    try:
        with open("students.json", "r") as file:
            students = json.load(file)

    except FileNotFoundError:
        students = []


def save_records():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)

def get_next_student_id():
    if len(students) == 0:
        return int(input("Enter starting Student ID: "))

    return max(student["id"] for student in students) + 1


def display_menu():
    print("\n========================================")
    print("       STUDENT RECORD MANAGEMENT")
    print("========================================")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    print("========================================")


def add_student():
    print("\n---------- Add Student ----------")

    student_id = get_next_student_id()

    print("Student ID:", student_id)

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
    save_records()

    print("\nStudent added successfully!")


def view_students():
    print("\n---------- Student Records ----------")

    if len(students) == 0:
        print("No student records found.")
        return

    for student in students:
        print("\nID:", student["id"])
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Course:", student["course"])
        print("Email:", student["email"])
        print("--------------------------------------")


def search_student():
    print("\n---------- Search Student ----------")

    search_id = int(input("Enter Student ID to search: "))

    for student in students:
        if student["id"] == search_id:
            print("\nStudent Found!")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])
            print("Email:", student["email"])
            return

    print("\nStudent not found.")


def update_student():
    print("\n---------- Update Student ----------")

    update_id = int(input("Enter Student ID to update: "))

    for student in students:
        if student["id"] == update_id:
            print("\nStudent Found!")

            while True:
                print("\n1. Update Name")
                print("2. Update Age")
                print("3. Update Course")
                print("4. Update Email")
                print("5. Back")

                choice = input("Enter your choice: ")

                if choice == "1":
                    student["name"] = input("Enter new name: ")
                    save_records()
                    print("Name updated successfully!")

                elif choice == "2":
                    student["age"] = int(input("Enter new age: "))
                    save_records()
                    print("Age updated successfully!")

                elif choice == "3":
                    student["course"] = input("Enter new course: ")
                    save_records()
                    print("Course updated successfully!")

                elif choice == "4":
                    student["email"] = input("Enter new email: ")
                    save_records()
                    print("Email updated successfully!")

                elif choice == "5":
                    break

                else:
                    print("Invalid choice. Please try again.")

            return

    print("\nStudent not found.")


def delete_student():
    print("\n---------- Delete Student ----------")

    delete_id = int(input("Enter Student ID to delete: "))

    for student in students:
        if student["id"] == delete_id:
            print("\nStudent Found!")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])
            print("Email:", student["email"])

            confirmation = input("\nAre you sure you want to delete this student? (y/n): ")

            if confirmation.lower() == "y":
                students.remove(student)
                save_records()

                print("\nStudent deleted successfully!")

            else:
                print("\nDelete cancelled.")

            return

    print("\nStudent not found.")

def main():
    while True:
        display_menu()

        choice = input("Enter your choice: ")

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
            print("Thank you for using Student Record Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


load_records()
main()