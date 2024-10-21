# <div align="center"> 🔰 Data types and Variables </div>

## 📌 Table of Contents
- [ 🔰 Data types and Variables ](#--data-types-and-variables-)
  - [📌 Table of Contents](#-table-of-contents)
  - [📚 Variables](#-variables)
  - [📚 Variable Types](#-variable-types)
  - [📚 Accessing global variables](#-accessing-global-variables)
  - [📚 Data types](#-data-types)
  - [📚 Printing type](#-printing-type)
  - [📚 Type conversion](#-type-conversion)
<hr>
<br><br>

## 📚 Variables
- **Variables** are used to store data values.
    ```python
    x = 5 # x is a variable
    y = "Hello" # y is a variable

    print(x) # Output: 5
    print(y) # Output: Hello

    # We can also assign multiple values to multiple variables in one line
    a, b, c = 5, 3.2, "Hello"
    print(a, b, c) # Output: 5 3.2 Hello

    # We can also assign the same value to multiple variables in one line
    d = e = f = "World"
    print(d, e, f) # Output: World World World

    # We can also assign the value of one variable to another variable
    g = 5
    h = g
    print(h) # Output: 5

    # We can also change the value of a variable
    i = 5
    i = 10
    print(i) # Output: 10

    # We can also delete a variable
    j = 5
    del j
    print(j) # Output: NameError: name 'j' is not defined
    ```

<br><br>

## 📚 Variable Types
- **Local Variables** are the variables that are defined inside a function.
    ```python
    def myfunc():
        x = 5 # x is a local variable
        print(x)

    myfunc() # Output: 5
    ```
- **Global Variables** are the variables that are defined outside of a function.
    ```python
    x = 5 # x is a global variable

    def myfunc():
        print(x)

    myfunc() # Output: 5
    ```
- **Nonlocal Variables** are the variables that are defined in the nested function. 
    ```python
    # without nonlocal keyword
    def myfunc():
        x = 5 # x is a local variable
        def myinnerfunc():
            x = 10 # x is a local variable
            print(x) # Output: 10
        myinnerfunc()
        print(x) # Output: 5

    myfunc() # Output: 10 5

    # with nonlocal keyword
    def myfunc():
        x = 5 # x is a local variable
        def myinnerfunc():
            nonlocal x
            x = 10 # x is a nonlocal variable
            print(x) # Output: 10
        myinnerfunc()
        print(x) # Output: 10

    myfunc() # Output: 10 10
    ```

<br><br>

## 📚 Accessing global variables
- **Global variables** are the variables that are defined outside of a function.
    ```python
    x = 5 # x is a global variable

    def myfunc():
        print(x) # We can access the global variable inside a function

    myfunc() # Output: 5
    ```
- If we want to change the value of a global variable inside a function, we can use the `global` keyword.
    ```python
    x = 5 # x is a global variable

    def myfunc():
        global x
        x = 10

    myfunc()
    print(x) # Output: 10
    ```
- If we want to create a global variable inside a function, we can use the `global` keyword.
    ```python
    def myfunc():
        global y
        y = 5

    myfunc()
    print(y) # Output: 5
    ```

<br><br>

## 📚 Data types
- **int** - Integer type
    ```python
    a = 5 # a is an integer
    ```
- **float** - Floating point type
    ```python
    b = 5.0 # b is a float
    ```
- **str** - String type
    ```python
    c = "Hello" # c is a string
    ```
- **bool** - Boolean type
    ```python
    d = True # d is a boolean
    ```

<br><br>

## 📚 Printing type
- To print the type of a variable, we use the `type()` function.
    ```python
    a = 5
    b = 5.0
    c = "Hello"
    d = True
    print(type(a)) # Output: <class 'int'>
    print(type(b)) # Output: <class 'float'>
    print(type(c)) # Output: <class 'str'>
    print(type(d)) # Output: <class 'bool'>
    ```

<br><br>

## 📚 Type conversion
- **Type conversion** is the process of converting the value of one data type to another data type.
    ```python
    a = 5
    b = float(a) # b is a float
    c = str(a) # c is a string
    d = bool(a) # d is a boolean
    print(b, c, d) # Output: 5.0 5 True
    ```
<hr>