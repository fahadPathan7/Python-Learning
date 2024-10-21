# <div align='center'> 🔰 Introduction to Python </div>

## 📌 Table of Contents
- [ 🔰 Introduction to Python ](#--introduction-to-python-)
  - [📌 Table of Contents](#-table-of-contents)
  - [📚 What is Python?](#-what-is-python)
  - [📚 Features of Python](#-features-of-python)
  - [📚 Printing something](#-printing-something)
  - [📚 Taking input](#-taking-input)
<hr>
<br><br>

## 📚 What is Python?
- Python is a high-level, interpreted, interactive and object-oriented scripting language.
- Python is designed to be highly readable.
- It uses English keywords frequently where as other languages use punctuation, and it has fewer syntactical constructions than other languages.

<br><br>

## 📚 Features of Python
- **Easy-to-learn:** Python has few keywords, simple structure, and a clearly defined syntax. This allows the student to pick up the language quickly.
- **Easy-to-read:** Python code is more clearly defined and visible to the eyes.
- **Easy-to-maintain:** Python's source code is fairly easy to maintain.
- **A broad standard library:** Python's bulk of the library is very portable and cross-platform compatible on UNIX, Windows, and Macintosh.
- **Dynamically typed:** Python is dynamically typed. We don't have to declare the type of variables.
- **Interpreted:** Python is processed at runtime by the interpreter. We do not need to compile program before executing it. This is similar to PERL and PHP.
- **Garbage Collection:** Python has an automatic garbage collection. Memory management is done internally and the user does not have to worry about memory management.
- **Asynchronous:** Python is asynchronous, meaning that it can do multiple things at once. It can be achieved by using the `asyncio` module.
    ```python
    import asyncio

    async def main():
        print('Hello')
        await asyncio.sleep(1)
        print('World')

    asyncio.run(main())
    ```
    it will print `Hello` and then after 1 second it will print `World`.

<br><br>

## 📚 Printing something
- To print something in Python, we use the `print()` function.

    ```python
    print("Hello, World!")
    ```

    Output:
    ```
    Hello, World!
    ```
- We can use `,` to print variables.

    ```python
    name = "Fahad"
    age = 20
    print("My name is", name, "and I am", age, "years old.")
    ```

    Output:
    ```
    My name is Fahad and I am 20 years old.
    ```
- We can also use the `+` operator to concatenate strings.

    ```python
    print("Hello, " + "World!")
    ```
    Output:
    ```
    Hello, World!
    ```
- We can also use the `end` parameter to change the default newline character.

    ```python
    print("Hello", end=" ")
    print("World")
    ```
    Output:
    ```
    Hello World
    ```
- We can also use the `sep` parameter to change the default space separator.

    ```python
    print("Hello", "World", sep=", ")
    ```
    Output:
    ```
    Hello, World
    ```
- Printing variables with formatter.

    ```python
    name = "Fahad"
    age = 20
    print("My name is {} and I am {} years old.".format(name, age))
    print(f"My name is {name} and I am {age} years old.")
    ```

    Output:
    ```
    My name is Fahad and I am 20 years old.
    My name is Fahad and I am 20 years old.
    ```

<br><br>

## 📚 Taking input
- To take input from the user, we use the `input()` function.

    ```python
    name = input("Enter your name: ")
    print("Hello", name)
    ```

    Output:
    ```
    Enter your name: Fahad
    Hello Fahad
    ```

- The `input()` function always returns a string. If we want to take an integer input, we can typecast it to an integer.

    ```python
    age = int(input("Enter your age: "))
    print("Your age is", age)
    ```

    Output:
    ```
    Enter your age: 20
    Your age is 20
    ```

- We can also take multiple inputs in a single line.

    ```python
    name, age = input("Enter your name and age: ").split() # taking multiple inputs
    print("Your name is", name, "and your age is", age)
    ```

    Output:
    ```
    Enter your name and age: Fahad 20
    Your name is Fahad and your age is 20
    ```

    ```python
    arr = list(map(int, input("Enter multiple values: ").split())) # taking multiple integer inputs
    print("Values are", arr)
    ```
    Output:
    ```
    Enter multiple values: 1 2 3 4 5
    Values are [1, 2, 3, 4, 5]
    ```

- We can also take fixed and different length of inputs.

    ```python
    a, *b = map(int, input("Enter multiple values: ").split()) # taking multiple integer inputs.
    # a will store the first value and b will store the rest of the values. type(a) will be int and type(b) will be list.
    print("a is", a, "and b is", b)
    ```
    Output:
    ```
    Enter multiple values: 1 2 3 4 5
    a is 1 and b is [2, 3, 4, 5]
    ```

- Output on the same line.

    ```python
    # 1
    print("Hello", end=" ") # default value of end is '\n' (newline). We can change it to any other value space, comma, etc.
    print("World")

    # 2
    print("Hello", end=", ")
    print("World")

    # 3
    print("Hello", end="")
    print("World")
    ```

    Output:
    ```python
    Hello World # 1
    Hello, World # 2
    HelloWorld # 3
    ```

<hr>
