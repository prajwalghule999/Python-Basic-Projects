# Q2

def analyze_string(s):
    # Print length of the string
    print("\nLength of the string:", len(s))

    # Print reversed string
    print("Reversed string:", s[::-1])

    # Count vowels
    vowels = "aeiouAEIOU"
    count = 0

    for ch in s:
        if ch in vowels:
            count += 1

    print("Number of vowels:", count)

    # Print each character with positive and negative index

    for i in range(len(s)):
        print("Character:", s[i])
        print("Positive Index:", i)
        print("Negative Index:", i - len(s))
        print()


# Main Program
try:
    string = input("Enter a string: ")

    if string == "":
        print("Error: Empty string is not allowed.")
    else:
        analyze_string(string)

except Exception as e:
    print("Error:", e)