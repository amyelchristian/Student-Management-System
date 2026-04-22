students = {}

while True:
    print("\n--- STUDENT MANAGEMENT SYSTEM ---")
    print("1. ADD STUDENT")
    print("2. SHOW ALL STUDENTS")
    print("3. FIND TOPPER")
    print("4. SEARCH STUDENT")
    print("5. EXIT..")

    choice = int(input("ENTER YOUR CHOICE: "))

    #01 ADD A STUDENT
    if choice == 1:
        student_name = input("ENTER STUDENT NAME: ")
        student_marks = int(input("ENTER STUDENT MARKS: "))
        students[student_name] = student_marks
        print("STUDENT ADDED SUCCESSFULLY...")

    #02 SHOW ALL STUDENTS
    elif choice == 2:
        if len(students) == 0:
            print("NO STUDENTS FOUND...")
        else:
            for name, marks in students.items():
                result = "PASS" if marks >= 50 else "FAIL"
                print(f"{name}: {marks} ({result})")

    #03 FIND TOPPER
    elif choice == 3:
        if len(students) == 0:
            print("NO STUDENTS FOUND...")
        else:
            topper_name = ''
            topper_marks = -1

            for student_name, student_marks in students.items():
                if student_marks > topper_marks:
                    topper_marks = student_marks
                    topper_name = student_name

            print("TOPPER:", topper_name)
            print("MARKS:", topper_marks)

    #04 SEARCH STUDENT
    elif choice == 4:
        student_name = input("ENTER THE STUDENT NAME: ")
        if student_name in students:
            student_marks = students[student_name]
            print("MARKS:", student_marks)
            if student_marks >= 50:
                print("PASS")
            else:
                print("FAIL")
        else:
            print("STUDENT NOT FOUND...")

    #05 EXIT
    elif choice == 5:
        print("EXITING PROGRAM...")
        break

    else:
        print("INVALID CHOICE. TRY AGAIN...")
