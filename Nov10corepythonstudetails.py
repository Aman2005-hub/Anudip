students = []  # List to store all student records

while True:
    print("----------------------------------------------------------")
    print("-------------------- Student Portal ----------------------")
    print("1. Registration of New Student")
    print("2. Student Profile")
    print("3. Delete Student")
    print("4. List of all Students sorted as per standard")
    print("5. List of Students of Particular Standard")
    print("6. List of students with attendance greater than 50% standard wise")
    print("0. Exit")
    print("----------------------------------------------------------")

    choice = input("Select any one operation: ")

    if choice == "0":
        print("Exiting the program. Goodbye!")
        break

    # 1️⃣ Register new student
    elif choice == "1":
        print("\n---------- Student Registration ----------")
        sid = input("Student id : ")
        name = input("Name : ")
        standard = input("Standard : ")
        roll = input("Roll No. : ")
        attendance = float(input("Attendance : "))

        student = {
            "id": sid,
            "name": name,
            "standard": standard,
            "roll": roll,
            "attendance": attendance
        }

        students.append(student)
        print("Student Registered successfully!\n")

    # 2️⃣ Student profile
    elif choice == "2":
        sid = input("Enter student id to view profile: ")
        found = False
        for s in students:
            if s["id"] == sid:
                print("\n------ Student Profile ------")
                print(f"ID         : {s['id']}")
                print(f"Name       : {s['name']}")
                print(f"Standard   : {s['standard']}")
                print(f"Roll No.   : {s['roll']}")
                print(f"Attendance : {s['attendance']}%\n")
                found = True
                break
        if not found:
            print("Student not found!\n")

    # 3️⃣ Delete student
    elif choice == "3":
        sid = input("Enter student id to delete: ")
        for s in students:
            if s["id"] == sid:
                students.remove(s)
                print("Student deleted successfully!\n")
                break
        else:
            print("Student not found!\n")

    # 4️⃣ List all students sorted by standard
    elif choice == "4":
        print("\n------ All Students (Sorted by Standard) ------")
        if not students:
            print("No students available.\n")
        else:
            sorted_list = sorted(students, key=lambda x: x["standard"])
            for s in sorted_list:
                print(f"{s['id']} | {s['name']} | Std: {s['standard']} | Roll: {s['roll']} | Attendance: {s['attendance']}%")
            print()

    # 5️⃣ List students of a particular standard
    elif choice == "5":
        std = input("Enter standard: ")
        print(f"\n------ Students of Standard {std} ------")
        found = False
        for s in students:
            if s["standard"] == std:
                print(f"{s['id']} | {s['name']} | Roll: {s['roll']} | Attendance: {s['attendance']}%")
                found = True
        if not found:
            print("No students found in this standard.\n")

    # 6️⃣ List students with attendance > 50%
    elif choice == "6":
        print("\n------ Students with Attendance > 50% (Standard Wise) ------")
        if not students:
            print("No students available.\n")
        else:
            standards = sorted(set(s["standard"] for s in students))
            for std in standards:
                print(f"\nStandard: {std}")
                count = 0
                for s in students:
                    if s["standard"] == std and s["attendance"] > 50:
                        print(f"  {s['id']} | {s['name']} | Roll: {s['roll']} | Attendance: {s['attendance']}%")
                        count += 1
                if count == 0:
                    print("  No student has attendance > 50% in this standard.")
            print()

    else:
        print("Invalid choice! Please try again.\n")
