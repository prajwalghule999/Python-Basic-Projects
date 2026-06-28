# Q9: Unique Words using Set

import math

try:
    # Take sentence as input
    sentence = input("Enter a sentence: ")

    # Convert sentence into words
    words = sentence.split()

    # Store unique words in a set
    unique_words = set(words)

    # Print unique words in sorted order
    print("\nUnique Words:")
    for word in sorted(unique_words):
        print(word)

    # Count unique words
    count = len(unique_words)

    # Print square of count
    print("\nTotal Unique Words:", count)
    print("Square of Total Unique Words:", math.pow(count, 2))

except Exception as e:
    print("Error:", e)