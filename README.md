# Student Management System

A simple **Python-based Student Management System** that allows users to add students, view student details, and check their results.

## Features

* Add a new student
* Store student data in a text file
* View student details
* Calculate total marks
* Check whether a student has passed or failed
* Load previously saved students when the program starts
* Basic input validation and error handling

## Subjects

The system stores marks for:

* English
* Maths
* Physics
* Chemistry
* Computer Science

## How It Works

Student information is stored in `students.txt`.

Each student record follows this format:

```text
Name,Class,English,Maths,Physics,Chemistry,Computer Science,Total
```

Example:

```text
Rahul,12,75,82,68,71,90,386
```

## Result Criteria

The program currently uses the following rule:

```text
Total marks >= 125 → Pass
Total marks < 125 → Fail
```

You can modify this condition in `student_management.py`.

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/Student-Management-System.git
```

### 2. Open the project

```bash
cd Student-Management-System
```

### 3. Run the program

```bash
python student_management.py
```

## Technologies Used

* Python
* File Handling
* Dictionaries
* Loops
* Conditional Statements
* Exception Handling
* User Input

## Future Improvements

Some possible improvements are:

* Add student ID
* Add update/delete student functionality
* Calculate percentage
* Calculate grades
* Search students by name
* Use CSV or SQLite instead of a text file
* Add a graphical user interface
* Add password-based admin login

## Author

**Sahil Sharma**

Aspiring Computer Science / AI & ML Engineer.
