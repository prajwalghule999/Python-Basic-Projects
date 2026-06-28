# Q6: Sets + Tuples + Modules

import random
import math

try:
    numbers = set()

    # Take 10 numbers as input
    for i in range(10):
        num = int(input("Enter number " + str(i + 1) + ": "))
        numbers.add(num)

    # Convert set to tuple
    num_tuple = tuple(numbers)

    print("\nUnique Numbers:", numbers)
    print("Tuple:", num_tuple)

    # Pick 3 random numbers
    if len(num_tuple) >= 3:
        random_numbers = random.sample(num_tuple, 3)
        print("3 Random Numbers:", random_numbers)
    else:
        print("Not enough unique numbers to select 3.")

    # Find square root of sum
    total = sum(num_tuple)
    print("Sum of Numbers:", total)
    print("Square Root:", math.sqrt(total))

except ValueError:
    print("Invalid Input! Please enter numbers only.")

except Exception as e:
    print("Error:", e)