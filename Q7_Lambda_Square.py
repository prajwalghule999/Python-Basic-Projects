# Q7: Lambda + Range + Lists + Exception Handling

try:
    # Lambda function to find square
    square = lambda x: x * x

    # Store squares of numbers from 1 to 20
    squares = []

    for i in range(1, 21):
        squares.append(square(i))

    print("Squares of numbers from 1 to 20:")
    print(squares)

    print("\nEven Squares:")
    for num in squares:
        if num % 2 == 0:
            print(num)

except Exception as e:
    print("Error:", e)