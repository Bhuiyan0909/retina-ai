                         Python Loops — My Practice Notes

These are my own notes from when I practiced loops in Python.


I learned both while and for loops and how they work in different situations.

While Loop

Runs again and again as long as the condition is true.

It’s useful when we don’t know exactly how many times the loop should repeat.

Example: asking for user input until they type something specific.

If the condition never becomes false, it creates an infinite loop.

To stop an infinite loop, press Ctrl + C in the shell.

 Key ideas I learned:


 

Always make sure something changes inside the loop so it doesn’t run forever.

.lower() is useful to handle both upper and lowercase inputs.

I can use a counter variable to count how many times a loop runs.

If I want to stop the loop after certain tries, use an if condition inside the loop.



For Loop





Runs a specific number of times — useful when I already know how many repetitions I need.

Works well with range(), which gives a sequence of numbers.

The syntax looks clean and is easy to control with start, end, and step values.

Key ideas I learned:



range(start, end) includes start but not end.

To include the end number, I have to write range(start, end + 1).

I can also use range(start, end, step) to skip numbers or go backward.

for loops are simpler than while loops when I know the exact count.


Counter and Accumulator



A counter keeps track of how many times something happens.

An accumulator adds up values during the loop (like summing numbers).

Usually starts with 0 and increases using +=.

Used for sums, averages, factorials, etc.


 What I realized:

 

Be careful where I put the += statement — inside or outside of if makes a difference.

For factorials, multiplying inside the loop step by step works well.

Range Function

range() can have 1, 2, or 3 arguments:

range(end) → starts from 0 to end-1

range(start, end) → from start to end-1

range(start, end, step) → skips numbers based on step

Can use negative step to count backward.


 Example ideas:

 

Counting down (range(5, 0, -1))

Skipping numbers (range(1, 10, 2))

Break and Continue

break stops the loop completely.

continue skips the current step and goes to the next.

Helpful when I only want to stop or skip based on a condition.


 Lesson:

 

Use break carefully; sometimes it hides logical mistakes.

Practice Summary (What I Learned)

How to use while loops to repeat user inputs.

How to control loop repetition using counters.

How to use for loops with range().

The difference between inclusive and exclusive ranges.

How to calculate sums and factorials using loops.

Why infinite loops happen and how to stop them.

How to use break and continue properly.
