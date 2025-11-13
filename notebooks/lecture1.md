What I Learned from MIT OCW Python Course (Fall 2022)


# Lecture 1: What I Learned About Knowledge and Programming...

## Two Types of Knowledge
While going through this lecture, I learned that there are basically **two kinds of knowledge**:

- **Declarative Knowledge**: Facts and statements, like “2+2=4”.  
- **Imperative Knowledge**: Step-by-step recipes for how to do things.

It seems like **programming is all about these recipes**—we’re telling the computer exactly what steps to follow to produce facts or results.

## Algorithms = Computer Recipes
An algorithm is just a clear set of instructions that has:

- Simple steps to follow  
- Rules for what to do next  
- A way to know when to stop  

I found a cool example in the lecture: **finding square roots by guessing and improving**.

Steps I understood:  
1. Start with a guess.  
2. Check if guess × guess is close enough to the number.  
3. If not, make a better guess by averaging the guess with (number/guess).  
4. Repeat until it’s close enough.

It’s simple but makes sense how computers follow these recipes so precisely.

## How Computers Work
Computers are kind of amazing but also a little “dumb”:  

- They can do **super fast calculations** (billions per second!)  
- They **remember everything** we tell them  
- They only do **exactly what we program them to do**  

They store programs in memory, just like we store data, which is why every instruction has to be correct.

## Starting with Python

### Programming Language Rules
I learned that programming languages have some rules:  

- **Syntax**: Grammar rules (like “cat dog boy” doesn’t work in English)  
- **Static Semantics**: Makes sure things make sense (can’t add words to numbers)  
- **Semantics**: What the program actually does—it’s always deterministic but sometimes not what we intended!  

### Basic Python Stuff
**Objects and Types**:  
- Everything in Python is an object with a type  
- `int` = whole numbers (5, -100)  
- `float` = decimal numbers (3.14, 2.0)  
- `bool` = True or False  
- I can check types using `type()`  

**Expressions**:  
- Combine values using operators: `3 + 2`, `5 / 3`  
- Python follows the usual math order of operations  

**Variables**:  
- `=` means “store this value in this name”  
- Example: `pi = 3.14` means “pi now represents 3.14”  
- You can change what the variable stores later  
- Important: Code runs **line by line, in order**  

### Key Things I Realized
- Computers **only do what we tell them**  
- Code runs **top to bottom**  
- Good variable names and comments make understanding easier  
- Programming is basically writing **clear recipes** for the computer  

so this is how the first lecture passed by.
