
# Lecture 2: Strings, Input/Output, and Branching

## Strings - Working with Text

### What I Learned About Strings
Strings are basically sequences of characters—letters, numbers, spaces, symbols… everything counts!  
You can make them with quotes like `"hello"` or `'world'`.

Some things I tried:

- **Concatenation** – joining strings with `+`  
```python
name = "Ana" + " " + "Bell"  # becomes "Ana Bell"
````

* **Repetition** – repeating strings with `*`

```python
laugh = "ha" * 3  # becomes "hahaha"
```

### String Indexing and Slicing

This part was tricky at first but fun once I got it:

* **Indexing**: pick one character with `[position]`

  * Positions start at 0! `"abc"[0]` gives `"a"`
  * Negative numbers count from the end: `-1` is the last character

* **Slicing**: grab a substring with `[start:stop:step]`

```python
s = "abcdefgh"
s[3:6]    # "def" (positions 3,4,5)
s[::2]    # "aceg" (every 2nd character)
s[::-1]   # "hgfedcba" (reverses the string)
```

**Tip I learned:** Strings are *immutable*—you can’t change them directly; you create new strings instead.

---

## Input and Output

### Printing Stuff

* `print()` shows things in the console
* Can print multiple things separated by commas
* **f-strings** make formatting much cleaner:

```python
name = "Alex"
age = 20
print(f"{name} is {age} years old")  # looks nice and clean
```

### Getting User Input

* `input("prompt")` asks the user for text
* Important: input always returns a string, even if they type numbers
* Convert to `int()` or `float()` for math:

```python
# Without conversion, this is string repetition
num1 = input("Enter a number: ")
print(5 * num1)

# With conversion, math works as expected
num2 = int(input("Enter a number: "))
print(5 * num2)
```

---

## Branching - Making Decisions in Code

### Comparison Operators

* `==`, `!=`, `>`, `<`, `>=`, `<=`
* Combine conditions with `and`, `or`, `not`

### If/Else Statements

The computer can make decisions based on conditions. Example I tried:

```python
grade = 85

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B") 
elif grade >= 70:
    print("C")
else:
    print("Need to improve")
```

#### Things I Learned the Hard Way:

* Indentation is super important (spaces vs tabs can cause errors!)
* Conditions are checked in order
* Only one block runs in an if-elif-else chain

**Common mistakes I made:**

* Forgetting colons after `if`, `elif`, `else`
* Using `=` instead of `==`
* Not converting input to numbers when needed

---

## Putting It All Together

I tried making a simple **guessing game** to combine everything I learned:

```python
secret = 42
guess = int(input("Guess my number: "))

if guess == secret:
    print("You got it!")
elif guess < secret:
    print("Too low!")
else:
    print("Too high!")
```

**Big takeaway:** test code as you go! Don’t write the whole program at once. Python Tutor helped me see what each line does step by step.

> This lecture made me realize how programs can interact with users and make decisions. Way more fun than just doing math!

```

---


