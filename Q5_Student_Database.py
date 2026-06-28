# Function to manage student database
def student_database():
    students = {}

    while True:
        print("\n----- Student Database -----")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Display All Students")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))

            # Add Student
            if choice == 1:
                roll = int(input("Enter Roll Number: "))
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                city = input("Enter City: ")

                students.update({
                    roll: {
                        "Name": name,
                        "Age": age,
                        "City": city
                    }
                })

                print("Student Added Successfully!")

            # Search Student
            elif choice == 2:
                roll = int(input("Enter Roll Number to Search: "))

                student = students.get(roll)

                if student:
                    print("\nStudent Details")
                    print("Name:", student["Name"])
                    print("Age:", student["Age"])
                    print("City:", student["City"])
                else:
                    print("Student Not Found!")

            # Display All Students
            elif choice == 3:
                if len(students) == 0:
                    print("No Records Found!")
                else:
                    print("\nStudent Records")
                    for roll, details in students.items():
                        print("\nRoll Number:", roll)
                        print("Name:", details["Name"])
                        print("Age:", details["Age"])
                        print("City:", details["City"])

            # Exit
            elif choice == 4:
                print("Program Ended.")
                break

            else:
                print("Invalid Choice!")

        except ValueError:
            print("Invalid Input! Please enter numbers only.")

# Function Call
student_database()