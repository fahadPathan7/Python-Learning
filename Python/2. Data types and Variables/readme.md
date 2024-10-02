# <div align="center"> 🔰 Data types and Variables </div>

## 📌 Table of Contents
- [ 🔰 Data types and Variables ](#--data-types-and-variables-)
  - [📌 Table of Contents](#-table-of-contents)
  - [📚 Variables](#-variables)
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