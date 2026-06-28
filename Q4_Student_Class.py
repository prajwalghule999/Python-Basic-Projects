# Class to store student details
class Student:

    # Constructor
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks_list = []

    # Method to add marks
    def add_mark(self, mark):
        if mark >= 0 and mark <= 100:
            self.marks_list.append(mark)
        else:
            print("Invalid marks! Marks should be between 0 and 100.")

    # Method to calculate average
    def get_average(self):
        if len(self.marks_list) == 0:
            return 0
        return sum(self.marks_list) / len(self.marks_list)

    # Method to display student details
    def display_info(self):
        print("\nStudent Details")
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Marks:", self.marks_list)
        print("Average Marks:", self.get_average())


# Main Program
try:
    name = input("Enter student name: ")
    roll = int(input("Enter roll number: "))

    student = Student(name, roll)

    n = int(input("How many marks do you want to enter? "))

    for i in range(n):
        mark = float(input("Enter mark " + str(i + 1) + ": "))
        student.add_mark(mark)

    student.display_info()

except ValueError:
    print("Invalid input! Please enter numbers only.")

except Exception as e:
    print("Error:", e)