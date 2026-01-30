import json

print("==== WELCOME TO STUDENT RECORD MANAGEMENT SYSTEM ====")

students = []

try:
    with open("students.json", "r") as file:
        students = json.load(file)
except:
    students = []

while True:
    print("\nMenu")
    print("1. Add Student")
    print("2. View all Students")
    print("3. Search Student by Roll Number")
    print("4. Exit")

    choice = int(input("Enter your choice : "))

    if choice == 1:
        name = input("Enter student's name : ")
        roll = input("Enter roll number : ")
        marks = int(input("Enter marks : "))

        student = {
            "Name": name,
            "roll number": roll,
            "marks": marks
        }

        students.append(student)

        with open("students.json", "w") as file:
            json.dump(students, file)

        print("Student added successfully!")

    elif choice == 2:
        if len(students) == 0:
            print("No students found.")
        else:
            print("\nStudent Records:")
            for s in students:
                print(
                    "Name:", s["Name"],
                    "| Roll:", s["roll number"],
                    "| Marks:", s["marks"]
                )

    elif choice == 3:
        search_roll = input("Enter roll number to search : ")
        found = False

        for s in students:
            if s["roll number"] == search_roll:
                print("\nStudent Found!")
                print(
                    "Name:", s["Name"],
                    "| Roll:", s["roll number"],
                    "| Marks:", s["marks"]
                )
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == 4:
        print("Exiting Program. Bye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")

