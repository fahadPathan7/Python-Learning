# <div align="center"> 🔰 Level 8 Methods and Advanced Strings </div>

## 📌Table of Contents
<hr>
<br><br>

## 📚 Methods
- **upper()** - Converts a string into upper case
    ```python
    a = "Hello, World!"
    print(a.upper()) # Output: HELLO, WORLD!
    ```
- **lower()** - Converts a string into lower case
    ```python
    a = "Hello, World!"
    print(a.lower()) # Output: hello, world!
    ```
- **replace()** - Returns a string where a specified value is replaced with a specified value
    ```python
    a = "Hello, World!"
    print(a.replace("H", "J")) # Output: Jello, World!
    ```
- **count()** - Returns the number of times a specified value occurs in a string
    ```python
    a = "Hello, World!"
    print(a.count("l")) # Output: 3
    ```
- **isdigit()** - Returns True if all characters in the string are digits
    ```python
    a = "50800"
    print(a.isdigit()) # Output: True
    ```
- **isalpha()** - Returns True if all characters in the string are in the alphabet
    ```python
    a = "CompanyX"
    print(a.isalpha()) # Output: True
    ```
- **isalnum()** - Returns True if all characters in the string are alphanumeric (contains only letters or numbers)
    ```python
    a = "Company12"
    print(a.isalnum()) # Output: True
    ```
- **isspace()** - Returns True if all characters in the string are whitespaces
    ```python
    a = "   "
    print(a.isspace()) # Output: True
    b = "   a   "
    print(b.isspace()) # Output: False
    ```
- **join()** - Joins the elements of an iterable to the end of the string
    ```python
    myTuple = ("John", "Peter", "Vicky")
    x = "#".join(myTuple)
    print(x) # Output: John#Peter#Vicky
    ```
- **strip()** - Returns a trimmed version of the string
    ```python
    a = " Hello, World! "
    print(a.strip()) # Output: Hello, World!
    ```
- **split()** - Splits the string into substrings if it finds instances of the separator
    ```python
    a = "Hello, World!"
    print(a.split(",")) # Output: ['Hello', ' World!']

    b = "a/b/c/d"
    print(b.split("/", 2)) # Output: ['a', 'b', 'c/d']
    ```
- **find()** - Searches the string for a specified value and returns the position of where it was found
    ```python
    a = "Hello, World!"
    print(a.find("o")) # Output: 4
    print(a.find("z")) # Output: -1
    ```
- **index()** - Searches the string for a specified value and returns the position of where it was found
    ```python
    a = "Hello, World!"
    print(a.index("o")) # Output: 4
    print(a.index("z")) # Output: ValueError: substring not found
    ```
- **startswith()** - Returns true if the string starts with the specified value
    ```python
    a = "Hello, World!"
    print(a.startswith("H")) # Output: True
    ```
- **endswith()** - Returns true if the string ends with the specified value
    ```python
    a = "Hello, World!"
    print(a.endswith("!")) # Output: True
    ```
<br>

**difference between find() and index()**<br>
- **find()** - Returns -1 if the value is not found
- **index()** - Returns an error if the value is not found
- **Example**
    ```python
    a = "Hello, World!"
    print(a.find("z")) # Output: -1
    print(a.index("z")) # Output: ValueError: substring not found
    ```

<br><br>

## 📚 Lambda and Map
- **Lambda** - A lambda function is a small anonymous function.
    ```python
    x = lambda a : a + 10
    print(x(5)) # Output: 15
    ```
- **Map** - The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.
    ```python
    def myfunc(n):
        return len(n)

    x = map(myfunc, ('apple', 'banana', 'cherry'))
    print(list(x)) # Output: [5, 6, 6]
    ```
<br>
**combine lambda and map**

```python
print(list(map(lambda x: x + 10, [1, 2, 3, 4, 5]))) # Output: [11, 12, 13, 14, 15]
```

<br><br>

## 📚 Recursion
- **Recursion** - A function that calls itself is called a recursive function.
    ```python
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)

    fib = fibonacci(10)
    print(fib) # Output: 55
    ```
<hr>