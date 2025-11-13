#########################################################
# Python Loops — Examples with Explanations
# Author: Code Alpha
# These are my own examples from when I learned loops.
# Each part has small comments explaining what’s happening.
#########################################################


##############################
# WHILE LOOP EXAMPLES
##############################

# Example 1: Basic while loop
# This keeps asking until I type "left"
where = input("You are in the Lost Forest. Go left or right? ")
while where == "right":           # Loop continues if I say "right"
    where = input("You are still in the forest! Go left or right? ")
print("You got out!")             # When I finally type "left", loop stops


# Example 2: Using counter inside while loop
# I’m adding a counter to track how many times I chose right
where = input("Go left or right? ")
counter = 0
while where == "right":
    counter += 1                  # increases the counter by 1
    if counter > 2:               # after 2 tries, print sad face
        print(":(")
    where = input("Go left or right? ")
print("You got out!")


# Example 3: While loop with countdown
# Prints “x” until n reaches 0
n = int(input("Enter a positive number: "))
while n > 0:
    print("x")
    n -= 1                        # reduces n by 1 each time


# Example 4: Infinite loop (⚠️ Be careful)
# Uncomment to test. Use Ctrl + C to stop it.
# while True:
#     print("nooooooo")


##############################
# FOR LOOP EXAMPLES
##############################

# Example 5: Printing numbers 0–4
# for loops automatically increase the number
for i in range(5):
    print(i)


# Example 6: Factorial using while loop
# Multiply each number up to x
x = 5
i = 1
factorial = 1
while i <= x:
    factorial *= i
    i += 1
print(f"{x} factorial is {factorial}")


# Example 7: Factorial using for loop
# Same thing but easier to write
factorial = 1
for i in range(1, x + 1):
    factorial *= i
print(f"{x} factorial is {factorial}")


# Example 8: Range examples
# Shows how range(start, end, step) works
for i in range(1, 4, 1):
    print(i)          # prints 1, 2, 3
for j in range(1, 4, 2):
    print(j * 2)      # skips by 2 → prints 2, 6
for me in range(4, 0, -1):
    print("$" * me)   # prints reverse pyramid with $


##############################
# SUMMATION EXAMPLES
##############################

# Example 9: Adding numbers from 0–9
mysum = 0
for i in range(10):
    mysum += i
print("Sum from 0 to 9 =", mysum)


# Example 10: Using start and end variables
# I learned to include +1 to make it inclusive
mysum = 0
start = 3
end = 5
for i in range(start, end + 1):
    mysum += i
print(f"Sum from {start} to {end} =", mysum)


##############################
# PRACTICE QUESTIONS
##############################

# Practice 1: Print all numbers up to x divisible by 5
x = 15
print(f"Numbers between 1 and {x} that are divisible by 5:")
for i in range(1, x + 1):
    if i % 5 == 0:
        print(i)


# Practice 2: Sum of digits of a number
# Example: if n = 1234 → total = 1+2+3+4 = 10
n = 1234
total = 0
while True:
    r = n % 10
    total += r
    n = n // 10
    if n == 0:
        break
print("Sum of digits =", total)


#########################################################
# END OF FILE
# These examples helped me understand how loops actually work.
#########################################################
