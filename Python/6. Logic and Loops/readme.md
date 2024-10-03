# <div align="center"> 🔰  Level 6 Logic and Loops </div>

## 📌 Table of Contents
- [ 🔰  Level 6 Logic and Loops ](#---level-6-logic-and-loops-)
  - [📌 Table of Contents](#-table-of-contents)
  - [📚 formatting and slicing](#-formatting-and-slicing)
  - [📚 if, elif, else](#-if-elif-else)
  - [📚 match, case](#-match-case)
  - [📚 for loop](#-for-loop)
  - [📚 while loop](#-while-loop)
<hr>
<br><br>

## 📚 formatting and slicing
- formatting is used to format a string to a specific format.
- slicing is used to extract a part of a string, list, or tuple.

```python
name = "John"
age = 36
txt = "My name is {} and I am {}"
print(txt.format(name, age)) # Output: My name is John and I am 36
print(f"My name is {name} and I am {age}") # Output: My name is John and I am 36

a = "Hello, World!"
print(a[1]) # Output: e
print(a[2:5]) # Output: llo
print(a[:5]) # Output: Hello
print(a[2:]) # Output: llo, World!
print(a[-5:-2]) # Output: orl (negative indexing)
```

<br><br>

## 📚 if, elif, else
- `if` statement is used to check a condition: if the condition is true, we run a block of statements (called the if-block), else we process another block of statements (called the else-block).
- `elif` is short for else if. It allows us to check for multiple expressions.
- `else` is used to run a block of code if the condition is false.

```python
a = 33
b = 200
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
```

and, or, not
- `and` is a logical operator that combines two or more boolean expressions and returns true only if all the expressions are true.
- `or` is a logical operator that combines two or more boolean expressions and returns true if at least one of the expressions is true.
- `not` is a logical operator that returns the opposite of the boolean value of the expression.

```python
a = 200
b = 33
c = 500

if a > b and c > a:
  print("Both conditions are True")

if a > b or a > c:
    print("At least one of the conditions is True")

if not a > b:
    print("a is not greater than b")
```

<br><br>

## 📚 match, case
- `match` statement is used to compare the value of an expression to a sequence of values and execute the corresponding block of code. (it is similar to switch in other languages)
- `case` is used to compare the value of the expression to the value of the case and execute the block of code. If a case matches, the corresponding block of code is executed and the match statement is exited. **No need for a break statement like in switch**.

```python
def func(x):
    match x:
        case 1:
            print("one")
        case 2:
            print("two")
        case _: # default case
            print("other")
```

<br><br>

## 📚 for loop
- `for` loop is used to iterate over a sequence (list, tuple, string) or other iterable objects.

```python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) # Output: apple, banana, cherry (each on a new line)
```

<br><br>

## 📚 while loop
- `while` loop is used to execute a block of statements repeatedly until a given condition is true.

```python
i = 1
while i < 6:
  print(i)
  i += 1
  if i == 3:
    break # Exit the loop when i is 3
```

implementing do-while loop in python:
```python
i = 1
while True:
    print(i)
    i += 1
    if i == 6:
        break
```
<hr>


