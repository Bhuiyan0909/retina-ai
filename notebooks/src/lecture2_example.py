# Lecture 2: Strings, Input/Output, and Branching
# Student-style exploratory exercises

# --- STRINGS ---
# Concatenation
first_name = "Ana"
last_name = "Bell"
full_name = first_name + " " + last_name
print("Full name:", full_name)

# Repetition
laugh = "ha" * 3
print("Laughing:", laugh)

# Indexing and slicing
word = "Python"
print("First letter:", word[0])   # P
print("Last letter:", word[-1])   # n
print("Slice 1-4:", word[1:4])    # yth
print("Every 2nd letter:", word[::2])
print("Reversed word:", word[::-1])

# --- INPUT / OUTPUT ---
# Printing multiple items and using f-strings
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello {name}, you are {age} years old!")

# Playing with string input
num_str = input("Enter a number (string test): ")
print("5 times your input (string):", 5 * num_str)

num_int = int(input("Enter a number (int test): "))
print("5 times your input (int):", 5 * num_int)

# --- BRANCHING / DECISIONS ---
# If/elif/else
grade = int(input("Enter your grade: "))

if grade >= 90:
    print("Your grade is: A")
elif grade >= 80:
    print("Your grade is: B")
elif grade >= 70:
    print("Your grade is: C")
else:
    print("You need to improve")

# Small guessing game
secret = 42
guess = int(input("Guess my number: "))

if guess == secret:
    print("You got it!")
elif guess < secret:
    print("Too low!")
else:
    print("Too high!")

# Reflection / comments
# I can see how strings, input/output, and branching all work together.
# Testing little examples step by step really helps me understand Python.
