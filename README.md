# Student Record Management System

A Python-based console application for managing student records.

**Course:** MCA Semester I – Python Programming & Relational Database

**Assignment:** Assignment 1 – Mini Project: Console Record-Management Application

## Project Description

This project is a console-based application designed to manage student records efficiently. It allows users to add, view, search, update, and delete student data. The application was created to demonstrate fundamental Python programming concepts such as functions, loops, and dictionaries. All student records are stored persistently using a JSON file (`students.json`), ensuring that data is retained across application restarts.

## Features

### Core Features

* Add student records
* View all student records
* Search students by ID
* Update student records
* Delete student records
* Menu-driven interface
* Persistent JSON storage

### Additional Features

* Automatic Student ID generation
* User-defined starting ID
* Sequential ID generation
* IDs are not reused after deletion
* Individual field update
* Delete confirmation

## Python Concepts Demonstrated

| Concept                | Usage in Project                                 |
| ---------------------- | ------------------------------------------------ |
| Variables              | Store student and application data               |
| Data Types             | Integers, strings, lists, dictionaries           |
| Conditional Statements | Menu selection and record operations             |
| Loops                  | Menu loop and record iteration                   |
| Functions              | Separate functions for application operations    |
| Exception Handling     | Handling `FileNotFoundError` during file loading |
| File I/O               | Reading and writing persistent records           |
| JSON                   | Storing structured student records               |

## Application Menu

```text
========================================
       STUDENT RECORD MANAGEMENT
========================================
1. Add Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
========================================
```

## Student Record Structure

```text
Student
├── ID
├── Name
├── Age
├── Course
└── Email
```

```json
[
    {
        "id": 1,
        "name": "Vinit Surve",
        "age": 21,
        "course": "MCA",
        "email": "example@gmail.com"
    }
]
```

## Automatic Student ID

The application supports automatic Student ID generation. When adding the first student, the user is prompted to enter a starting ID.

```text
Starting Student ID: 101

First student  → 101
Second student → 102
Third student  → 103
Fourth student → 104
```

Subsequent IDs are generated from the highest existing ID + 1. If a record is deleted, its ID is not reused.

## Update Functionality

The application supports updating individual fields instead of forcing the user to rewrite every field.

```text
1. Update Name
2. Update Age
3. Update Course
4. Update Email
5. Back
```

## Delete Confirmation

Deletion requires user confirmation before removing a record permanently.

```text
Are you sure you want to delete this student? (y/n): 
```

## File Storage

Records are loaded into memory when the program starts using the `load_records()` function and saved whenever changes are made (Add, Update, Delete) using the `save_records()` function. Data is persistently stored in `students.json`.

## Project Structure

```text
student-record-management-system/
│
├── main.py
├── students.json
└── README.md
```

## Requirements

```text
Python 3.x
```

No external Python packages are required.

## How to Run

```bash
git clone https://github.com/VinitSurve/student-record-management-system.git
cd student-record-management-system
python main.py
```
*(Alternatively, use `py main.py` on Windows)*

## Sample Usage

**1. Starting the Application:**

```text
========================================
       STUDENT RECORD MANAGEMENT
========================================
1. Add Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
========================================
Enter your choice:
```

**2. Adding a Student:**

```text
---------- Add Student ----------
Enter starting Student ID: 101
Student ID: 101
Enter Student Name: John Doe
Enter Student Age: 22
Enter Course: MCA
Enter Email: john@example.com

Student added successfully!
```

**3. Viewing the Student:**

```text
---------- Student Records ----------

ID: 101
Name: John Doe
Age: 22
Course: MCA
Email: john@example.com
--------------------------------------
```

**4. Searching:**

```text
---------- Search Student ----------
Enter Student ID to search: 101

Student Found!
ID: 101
Name: John Doe
Age: 22
Course: MCA
Email: john@example.com
```

**5. Updating:**

```text
---------- Update Student ----------
Enter Student ID to update: 101

Student Found!

1. Update Name
2. Update Age
3. Update Course
4. Update Email
5. Back
Enter your choice: 1
Enter new name: John Smith
Name updated successfully!
```

**6. Deleting:**

```text
---------- Delete Student ----------
Enter Student ID to delete: 101

Student Found!
ID: 101
Name: John Smith
Age: 22
Course: MCA
Email: john@example.com

Are you sure you want to delete this student? (y/n): y

Student deleted successfully!
```

**7. Exiting:**

```text
Enter your choice: 6
Thank you for using Student Record Management System.
```

## Screenshots

Screenshots demonstrating the application's execution are currently pending.

The following screenshots will be added before final submission:

* Main menu
* Add student
* View records
* Search
* Update
* Delete confirmation
* Successful deletion
* Persistent records after restart

## Assignment Requirements Coverage

| Requirement | Implementation |
| --- | --- |
| Data Types and Variables | Student data and application variables |
| Conditional Statements | Menu selection and record operations |
| Loops | Menu loop and record iteration |
| Functions | Modular functions for each operation |
| Exception Handling | Handling `FileNotFoundError` during file load |
| File I/O | JSON file read/write (`students.json`) |
| Menu-driven Application | Console menu |
| Add Records | Implemented |
| View Records | Implemented |
| Search Records | Implemented |
| Update Records | Implemented |
| Delete Records | Implemented |

## Testing

The application has been tested for:

* Application startup
* Adding records
* Viewing records
* Searching existing/non-existing records
* Updating records
* Individual field updates
* Deleting records
* Delete confirmation/cancellation
* Automatic ID generation
* ID behavior after deletion
* Data persistence
* Restart persistence

**Note on Exception Handling:**

* `FileNotFoundError` is currently handled gracefully.
* Invalid numeric input such as letters entered for ID/Age currently causes a crash.
* Corrupted JSON currently causes a crash.

## Future Improvements

* Stronger numeric input validation
* `ValueError` handling
* JSON parsing error handling
* Email validation
* Age validation
* Better user interface
* Database integration
* Authentication
* Export/import functionality

## GitHub Repository

[Student Record Management System](https://github.com/VinitSurve/student-record-management-system)

## Academic Assignment

**Course:** MCA Semester I – Python Programming & Relational Database

**Assignment:** Assignment 1 – Mini Project: Console Record-Management Application
