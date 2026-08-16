students = []


#----------------Calculations---------

def total_marks(marks):
    return sum(marks.values())

def average_marks(total):
    return total/5

def calculate_percentage(total):
    return (total / 500) * 100

def grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"

def check_result(marks):
    for mark in marks.values():
        if mark < 35:
            return "FAIL"

    return "PASS"

# ---------------- INPUT VALIDATION ----------------

def get_marks(subject):
    while True:
        try:
            mark = int(input(f"Enter {subject} marks (0-100):"))

            if 0 <= mark <= 100:
                return mark
            else:
                print("❌ marks must be between 0 and 100")

        except ValueError:
            print("❌ Please enter numbers only.")

# ---------------- ADD STUDENT ----------------

def add_student():

    print("\n========== ADD STUDENT ==========")

    roll_no = input("Enter Roll No: ")

    #Check duplicate roll number
    for student in students:
        if student["roll_no"] == roll_no:
            print("❌ Roll number already exists!")
            return

    name = input("Enter Student Name:  ")

    marks = {}

    subjects = [
        "English",
        "Maths",
        "Science",
        "Social",
        "Computer",
    ]

    for subject in subjects:
        marks[subject] = get_marks(subject)

    total = total_marks(marks)
    average = average_marks(total)
    percentage = calculate_percentage(total)
    student_grade = grade(average)
    result = check_result(marks)

    student = {
        "roll_no": roll_no,
        "name": name,
        "marks": marks,
        "total": total,
        "average": average,
        "percentage": percentage,
        "grade": student_grade,
        "result": result,
    }

    students.append(student)

    print("\n✅ Student added successfully!")

# ---------------- DISPLAY STUDENT ----------------

def display_student(student):


    print("\n=======================")
    print("        Student Report")
    print("========================")

    print("Roll No: ", student["roll_no"])
    print("Name: ", student["name"])

    print("\n------- Subject marks ------")

    for subject, mark in student["marks"].items():
        print(f"{subject:<10}: {mark}")

    print("\n------- Result ------")

    print("Total       :", student["total"], "/ 500")
    print("Average     :", round(student["average"], 2))
    print("Percentage  :", round(student["percentage"], 2), "%")
    print("Grade       :", student["grade"])
    print("Result      :", student["result"])

    print("===============================")

# ---------------- VIEW ALL STUDENTS ----------------

def view_students():

    if len(students) == 0:
        print("\n❌ No students found.")
        return

    print("\n============== ALL STUDENTS ============")

    for student in students:
        print(
            f"Roll No: {student['roll_no']}, |"
            f"Name: {student['name']}, |"
            f"total: {student['total']}, |"
            f"Grade: {student['grade']}, |"
            f"Result: {student['result']}, |"
        )


# ---------------- SEARCH STUDENT ----------------

def search_student():

    roll_no = input("\nEnter Roll Number to search:  ")

    for student in students:

        if student["roll_no"] == roll_no:
            display_student(student)
            return

    print("❌ student not found.")

# ---------------- DELETE STUDENT ----------------

def delete_student():
    roll_no = input("\nEnter Roll Number to delete:  ")

    for student in students:

        if student["roll_no"] == roll_no:

            students.remove(student)

            print("✅ student deleted successfully!")
            return

    print("❌ student not found. ")

# ---------------- CLASS STATISTICS ----------------

def class_statistics():

    if len(students) == 0:
        print("\n❌ No student data available.")
        return

    total_marks_list = []

    passed = 0
    failed = 0

    for student in students:

        total_marks_list.append(student["total"])

        if student["result"] == "PASS":
            passed += 1
        else:
            failed += 1

    highest = max(total_marks_list)
    lowest  = min(total_marks_list)

    class_average = sum(total_marks_list) / len(total_marks_list)

    print("\n================= CLASS STATISTICS ===============")

    print("Total students  :", len(students))
    print("passed students :", passed)
    print("failed students :", failed)
    print("Highest Total   :", highest)
    print("Lowest Total    :", lowest)


 # ---------------- MAIN MENU ----------------

while True:

     print("\n")
     print("===================================")
     print("      Student Management System")
     print("===================================")

     print("1. ADD Student")
     print("2. View All Students")
     print("3. Search Student")
     print("4. Delete Student")
     print("5. Class Statistics")
     print("6. Exit")

     choice = input("\nEnter your choice: ")

     if choice == "1":
         add_student()

     elif choice == "2":
         view_students()

     elif choice == "3":
         search_student()

     elif choice == "4":
         delete_student()

     elif choice == "5":
         class_statistics()

     elif choice == "6":
         print("\n Thank you for using Student Management System")
         break

     else:
         print("❌ Invalid choice. Please try again.")

    
