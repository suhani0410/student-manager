while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        file = open("students.txt", "a")
        name = input("Enter student name: ")
        file.write(name + "\n")
        file.close()
        print("Student added successfully")

    elif choice == "2":
        file = open("students.txt", "r")
        print("\nStudent List:")
        print(file.read())
        file.close()

    elif choice == "3":
        file = open ("students.txt", "r")
        students = file.readlines()
        file.close()

        name = input("Enter name to delete:")

        file = open ("student.txt", "w")
        for student in students:
            if student.strip()!=name:
                file.write (student)

        file.close()
        print("student delete (if existed)")

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice")
