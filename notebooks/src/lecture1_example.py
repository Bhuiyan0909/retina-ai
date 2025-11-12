# Lecture 1: Example Python Code
# Student-style exploratory exercises

# Hello World!
print("Hello, Retina AI!")  # First thing I learned in Python

# Variables and types
pi = 3.14          # storing a number
age = 18           # storing an integer
is_happy = True    # boolean variable

#this just prints inthe terminal

print("pi:", pi)
print("age:", age)
print("is_happy:", is_happy)

# Checking types
print("Type of pi:", type(pi))
print("Type of age:", type(age))
print("Type of is_happy:", type(is_happy))

# Expressions and operators
a = 5
b = 2
sum_ab = a + b
product_ab = a * b
division_ab = a / b

print("Sum:", sum_ab)
print("Product:", product_ab)
print("Division:", division_ab)

#using while loops which is really easy to learn but is used in top notch work
# Simple algorithm: guessing square roots
number = 16
guess = number / 2  # initial guess

tolerance = 0.001
while abs(guess**2 - number) > tolerance:
    guess = (guess + number / guess) / 2  # improving the guess

print(f"Approximate square root of {number} is {guess}")

# Reflection / comment
# I can see how this algorithm follows a clear set of steps, just like the lecture described
