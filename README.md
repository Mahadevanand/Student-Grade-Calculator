# 🎓 Student-Grade-Calculator

A simple **Python-based Student Grade Calculator** that allows users to add, view, search, delete students, and calculate student results and class statistics.

This project is designed to practice **Python functions, dictionaries, lists, loops, conditions, input validation, and basic data management**.

## 🚀 Features

* ➕ Add a new student
* 📋 View all students
* 🔍 Search student by Roll Number
* 🗑️ Delete a student
* 📊 Calculate class statistics
* 🧮 Calculate total marks
* 📈 Calculate average marks
* 📌 Calculate percentage
* 🏆 Automatically assign grades
* ✅ Check PASS/FAIL status
* ⚠️ Validate marks between 0 and 100
* 🚫 Prevent duplicate Roll Numbers
* ❌ Handle invalid input

## 📚 Subjects

The system accepts marks for five subjects:

* English
* Maths
* Science
* Social
* Computer

Each subject has a maximum of **100 marks**.

**Maximum Total = 500 marks**

## 🏆 Grading System

|  Average | Grade |
| -------: | :---- |
|   90–100 | A+    |
|    80–89 | A     |
|    70–79 | B     |
|    60–69 | C     |
|    50–59 | D     |
| Below 50 | F     |

### Pass/Fail Rule

A student must score at least **35 marks in every subject** to pass.

If the student scores below 35 in even one subject:

**Result = FAIL**

Otherwise:

**Result = PASS**

## 🛠️ Technologies Used

* **Python 3**
* Lists
* Dictionaries
* Functions
* `for` loops
* `while` loops
* `if-elif-else`
* Exception handling
* Input validation
* `sum()`
* `max()`
* `min()`

## 📂 Project Structure

```text
Student-Management-System/
│
├── student_management.py
└── README.md
```

## ▶️ How to Run

### 1. Install Python

Make sure Python 3 is installed on your computer.

Check your Python version:

```bash
python --version
```

### 2. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 3. Open the Project Folder

```bash
cd Student-Management-System
```

### 4. Run the Program

```bash
python student_management.py
```

## 🖥️ Main Menu

```text
===================================
      Student Management System
===================================

1. ADD Student
2. View All Students
3. Search Student
4. Delete Student
5. Class Statistics
6. Exit

Enter your choice:
```

## 📝 Example

When adding a student:

```text
========== ADD STUDENT ==========

Enter Roll No: 101
Enter Student Name: Mahadevanand

Enter English marks (0-100): 85
Enter Maths marks (0-100): 90
Enter Science marks (0-100): 78
Enter Social marks (0-100): 88
Enter Computer marks (0-100): 95

✅ Student added successfully!
```

The system calculates:

```text
Total      : 436 / 500
Average    : 87.2
Percentage : 87.2 %
Grade      : A
Result     : PASS
```

## 📊 Class Statistics

The Class Statistics option displays:

* Total number of students
* Number of passed students
* Number of failed students
* Highest total marks
* Lowest total marks

## 🧠 Python Concepts Practiced

This project is useful for practicing the following concepts:

### 1. Functions

The program is divided into functions such as:

```python
def add_student():
def view_students():
def search_student():
def delete_student():
def class_statistics():
```

### 2. Lists

A list stores all student records:

```python
students = []
```

### 3. Dictionaries

Each student is stored as a dictionary:

```python
student = {
    "roll_no": roll_no,
    "name": name,
    "marks": marks,
    "total": total,
    "average": average,
    "percentage": percentage,
    "grade": student_grade,
    "result": result
}
```

### 4. Loops

`for` and `while` loops are used for processing students, subjects, and menu operations.

### 5. Conditional Statements

`if`, `elif`, and `else` are used for grading, validation, and menu selection.

### 6. Exception Handling

`try-except` is used to handle invalid mark input:

```python
try:
    mark = int(input(...))
except ValueError:
    print("Please enter numbers only.")
```

## 🔮 Future Improvements

Possible improvements for this project:

* 💾 Save student data to a file
* 📂 Load student data when the program starts
* ✏️ Update student details
* 🔐 Add login/authentication
* 🖥️ Create a GUI using Tkinter
* 🗄️ Use SQLite/MySQL database
* 📊 Add graphical statistics
* 🔎 Search students by name
* 🏅 Display the class topper
* 📄 Generate student report cards

## 🎯 Project Purpose

The main purpose of this project is to build a **beginner-friendly Python application** while practicing real-world programming concepts such as functions, data structures, validation, and CRUD-style operations.

## 👨‍💻 Author

**Mahadevanand**

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub!
