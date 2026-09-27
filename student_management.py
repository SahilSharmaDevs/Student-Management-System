students = {}

try:
    with open("students.txt", "r", encoding="utf-8") as file:
        for line in file:
            data = line.strip().split(",")
            if len(data) != 8:
                continue

            name = data[0]
            student_class = data[1]
            marksENG = int(data[2])
            marksMATH = int(data[3])
            marksPHY = int(data[4])
            marksCH = int(data[5])
            marksCS = int(data[6])
            total = int(data[7])

            students[name] = {
                "class": student_class,
                "english": marksENG,
                "maths": marksMATH,
                "physics": marksPHY,
                "chemistry": marksCH,
                "computer science": marksCS,
                "total": total,
            }
except FileNotFoundError:
    pass

print("Welcome to Student Management System")

while True:
    print("1. Add Student")
    print("2. View Student")
    print("3. Check Result")
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        if name in students:
            print("Student already exists. Try a different name.")
            print()
            continue

        student_class = input("Enter class: ")
        try:
            marksENG = int(input("Enter mark in English: "))
            marksMATH = int(input("Enter mark in Maths: "))
            marksPHY = int(input("Enter mark in Physics: "))
            marksCH = int(input("Enter mark in Chemistry: "))
            marksCS = int(input("Enter mark in Computer Science: "))
        except ValueError:
            print("Invalid datatype. Please enter integer marks.")
            print()
            continue

        total = marksENG + marksMATH + marksPHY + marksCH + marksCS
        students[name] = {
            "class": student_class,
            "total": total,
            "english": marksENG,
            "maths": marksMATH,
            "physics": marksPHY,
            "chemistry": marksCH,
            "computer science": marksCS,
        }

        with open("students.txt", "a", encoding="utf-8") as file:
            file.write(
                f"{name},{student_class},{marksENG},{marksMATH},{marksPHY},{marksCH},{marksCS},{total}\n"
            )

        print("Student added successfully")

    elif choice == "2":
        name = input("Enter name of student to view: ")
        if name in students:
            print("Class:", students[name]["class"])
            print("Total marks:", students[name]["total"])
            print("English:", students[name]["english"])
            print("Maths:", students[name]["maths"])
            print("Physics:", students[name]["physics"])
            print("Chemistry:", students[name]["chemistry"])
            print("Computer Science:", students[name]["computer science"])
        else:
            print("Student not found")

    elif choice == "3":
        name = input("Enter name of student to check result: ")
        if name in students:
            total = students[name]["total"]
            if total >= 125:
                print("Pass")
            else:
                print("Fail")
        else:
            print("Student not found")

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")

    print()
    
