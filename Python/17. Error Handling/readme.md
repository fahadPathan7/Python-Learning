# <div align="center"> 🔰 Error Handling </div>

## 📌 Table of Contents
- [ 🔰 Error Handling ](#--error-handling-)
  - [📌 Table of Contents](#-table-of-contents)
  - [📚 Error Handling](#-error-handling)
  - [📚 Raise an exception](#-raise-an-exception)
  - [📚 Assert](#-assert)
  - [📚 Custom Exceptions](#-custom-exceptions)
  - [📚 Else and Finally](#-else-and-finally)
<hr>
<br><br>

## 📚 Error Handling
- **Error Handling** is the process of responding to the occurrence of exceptions during the execution of a program.
- **Try Block** contains the code that might throw an exception.
- **Except Block** contains the code that handles the exception.
- **Finally Block** contains the code that will be executed regardless of the result of the try and except blocks.
    ```python
    try:
        print(x)
    except NameError: # specifies the type of exception
        print("Variable x is not defined")
    except: # catches all exceptions
        print("Something else went wrong")
    finally:
        print("The 'try except' is finished")
    ```

<br><br>

## 📚 Raise an exception
- **Raise an exception** can be done using the `raise` keyword.
    ```python
    x = -1
    if x < 0:
        raise Exception("Sorry, no numbers below zero")
    ```

<br><br>

## 📚 Assert
- **Assert** is used to check if a condition is True, if not, the program will raise an AssertionError.
    ```python
    x = "hello"
    assert x == "world", "x should be 'world'"
    ```

<br><br>

## 📚 Custom Exceptions
- **Custom Exceptions** can be created by creating a new class that inherits from the `Exception` class.
    ```python
    class MyError(Exception):
        def __init__(self, message):
            self.message = message

    raise MyError("Something went wrong")
    ```

<br><br>

## 📚 Else and Finally
- **Else Block** will be executed if the try block doesn't raise an exception.
    ```python
    try:
        print("Hello")
    except:
        print("Something went wrong")
    else:
        print("Nothing went wrong")
    finally:
        print("The 'try except' is finished")
    ```

<hr>
