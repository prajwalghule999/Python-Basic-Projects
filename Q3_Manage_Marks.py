# Function to manage marks
def manage_marks():
    marks = []

    try:
        # Take 5 subject marks as input
        for i in range(5):
            mark = float(input("Enter marks of subject " + str(i + 1) + ": "))
            marks.append(mark)

        # Calculate average
        average = sum(marks) / len(marks)

        # Print highest and lowest marks
        print("\nAverage Marks:", average)
        print("Highest Marks:", max(marks))
        print("Lowest Marks:", min(marks))

        # Sort in descending order
        marks.sort(reverse=True)
        print("Marks in Descending Order:", marks)

    except ValueError:
        print("Invalid input! Please enter only numbers.")

# Function call
manage_marks()