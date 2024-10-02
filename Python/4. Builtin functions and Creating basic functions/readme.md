# <div align="center"> 🔰 Level 4 Built in Functions & Creating Basic Functions </div>

## 📌 Table of Contents
<hr>
<br><br>

## 📚 Built-in Functions
- **abs()** - Returns the absolute value of a number.
    ```python
    a = -5
    print(abs(a)) # Output: 5
    ```
- **min()** - Returns the smallest item in an iterable.
    ```python
    a = 5
    b = 1
    c = 3
    print(min(a)) # Output: 1
    ```
- **max()** - Returns the largest item in an iterable.
    ```python
    a = 5
    b = 1
    c = 3
    print(max(a)) # Output: 5
    ```
- **round()** - Rounds a number to a specified number of decimal places.
    ```python
    a = 5.678
    print(round(a)) # Output: 6
    ```

<br><br>

## 📚 Creating Basic Functions
```python
def name_func():
    name = input("Enter your name: ")
    print("Your name is " + name)

name_func()
```
**Output:**
```
Enter your name: John
Your name is John
```

<br><br>

## 📚 Function with Parameters
```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result) # Output: 8
```

<br><br>

## 📚 Function with Default Parameters
```python
def add(a, b=3):
    return a + b

result = add(5)
print(result) # Output: 8
```
<hr>