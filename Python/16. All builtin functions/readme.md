# <div align="center"> 🔰 All built-in functions </div>

## 📌 Table of contents
- [ 🔰 All built-in functions ](#--all-built-in-functions-)
  - [📌 Table of contents](#-table-of-contents)
  - [📚 abs()](#-abs)
  - [📚 all()](#-all)
  - [📚 any()](#-any)
  - [📚 ascii()](#-ascii)
  - [📚 bin()](#-bin)
  - [📚 bool()](#-bool)
  - [📚 bytearray()](#-bytearray)
  - [📚 bytes()](#-bytes)
  - [📚 callable()](#-callable)
  - [📚 chr()](#-chr)
  - [📚 classmethod()](#-classmethod)
  - [📚 compile()](#-compile)
  - [📚 complex()](#-complex)
  - [📚 delattr()](#-delattr)
  - [📚 dict()](#-dict)
  - [📚 dir()](#-dir)
  - [📚 divmod()](#-divmod)
  - [📚 enumerate()](#-enumerate)
  - [📚 eval()](#-eval)
  - [📚 exec()](#-exec)
  - [📚 filter()](#-filter)
  - [📚 float()](#-float)
  - [📚 format()](#-format)
  - [📚 iter()](#-iter)
  - [📚 len()](#-len)
  - [📚 list()](#-list)
  - [📚 map()](#-map)
  - [📚 max()](#-max)
  - [📚 min()](#-min)
  - [📚 pow()](#-pow)
  - [📚 reversed()](#-reversed)
  - [📚 round()](#-round)
  - [📚 range()](#-range)
  - [📚 set()](#-set)
  - [📚 slice()](#-slice)
  - [📚 sorted()](#-sorted)
  - [📚 sum()](#-sum)
  - [📚 tuple()](#-tuple)
  - [📚 type()](#-type)
  - [📚 zip()](#-zip)
<hr>
<br><br>

## 📚 abs()
- **Description**: The abs() function returns the absolute value of a number. The absolute value of a number is its distance from zero.
- **Syntax**: `abs(x)`

```python
x = -10
result = abs(x)
print(result)  # Output: 10
```

<br><br>

## 📚 all()
- **Description**: The all() function returns True if all elements of an iterable are true. If the iterable is empty, it returns True. (iterable: list, tuple, dictionary, etc.)
- **Syntax**: `all(iterable)`

```python
numbers = [1, 2, 3, 4, 5]
result = all(numbers)
print(result)  # Output: True
```

<br><br>

## 📚 any()
- **Description**: The any() function returns True if any element of an iterable is true. If the iterable is empty, it returns False.
- **Syntax**: `any(iterable)`

```python
numbers = [0, 0, 0, 1, 0]
result = any(numbers)
print(result)  # Output: True (since 1 is true)
```

<br><br>

## 📚 ascii()
- **Description**: The ascii() function returns a string containing a printable representation of an object. It escapes the non-ASCII characters in the string using \x, \u, or \U escapes.
- **Syntax**: `ascii(object)`

```python
string = "Hello, World!"
result = ascii(string)
print(result)  # Output: 'Hello, World!'
```

<br><br>

## 📚 bin()
- **Description**: The bin() function converts an integer number to a binary string prefixed with "0b".
- **Syntax**: `bin(number)`

```python
number = 10
result = bin(number)
print(result)  # Output: 0b1010
```

<br><br>

## 📚 bool()
- **Description**: The bool() function returns the boolean value of an object. It returns False if the object is False, 0, None, or an empty sequence. Otherwise, it returns True.
- **Syntax**: `bool(object)`

```python
result = bool(0)
print(result)  # Output: False
```

<br><br>

## 📚 bytearray()
- **Description**: The bytearray() function returns a new array of bytes. It can be used to convert a string to a byte array.
- **Syntax**: `bytearray([source[, encoding[, errors]]])`

```python
string = "Hello, World!"
result = bytearray(string, "utf-8")
print(result)  # Output: bytearray(b'Hello, World!')
```

<br><br>

## 📚 bytes()
- **Description**: The bytes() function returns a new bytes object. It can be used to convert a string to a byte object.
- **Syntax**: `bytes([source[, encoding[, errors]]])`

```python
string = "Hello, World!"
result = bytes(string, "utf-8")
print(result)  # Output: b'Hello, World!'
```

<br><br>

## 📚 callable()
- **Description**: The callable() function returns True if the object appears callable (i.e., it can be called as a function). Otherwise, it returns False.
- **Syntax**: `callable(object)`

```python
def my_function():
    return 10

result = callable(my_function)
print(result)  # Output: True
```

<br><br>

## 📚 chr()
- **Description**: The chr() function returns a character (a string) from an integer (ASCII value).
- **Syntax**: `chr(number)`

```python
number = 65
result = chr(number)
print(result)  # Output: 'A'
```

<br><br>

## 📚 classmethod()
- **Description**: The classmethod() function returns a class method for the given function. A class method receives the class as the first argument, instead of the instance.
- **Syntax**: `@classmethod`
- **Parameters**: `cls` (class)

```python
class MyClass:
    @classmethod
    def my_method(cls):
        print("Hello, World!")

MyClass.my_method()  # Output: Hello, World!
```

<br><br>

## 📚 compile()
- **Description**: The compile() function compiles the source into a code or AST object. It can be used to execute dynamically created code.
- **Syntax**: `compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)`

```python
source = "print('Hello, World!')"
code = compile(source, "hello.py", "exec")
exec(code)  # Output: Hello, World!
```

<br><br>

## 📚 complex()
- **Description**: The complex() function returns a complex number with the value real + imag*1j or converts a string or number to a complex number.
- **Syntax**: `complex(real, imag)`

```python
result = complex(1, 2)
print(result)  # Output: (1+2j)
```

<br><br>

## 📚 delattr()
- **Description**: The delattr() function deletes the named attribute from an object. It is the same as the del statement.
- **Syntax**: `delattr(object, name)`

```python
class MyClass:
    x = 10

obj = MyClass()
delattr(obj, "x")
print(obj.x)  # Raises AttributeError
```

<br><br>

## 📚 dict()
- **Description**: The dict() function creates a new dictionary. It can be used to convert a sequence of key-value pairs into a dictionary.
- **Syntax**: `dict(**kwargs)`

```python
result = dict(a=1, b=2, c=3)
print(result)  # Output: {'a': 1, 'b': 2, 'c': 3}
```

<br><br>

## 📚 dir()
- **Description**: The dir() function returns a list of valid attributes for the given object. If no object is provided, it returns the list of names in the current local scope.
- **Syntax**: `dir([object])`

```python
result = dir()
print(result)  # Output: ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'result']
```

<br><br>

## 📚 divmod()
- **Description**: The divmod() function returns a tuple containing the quotient and remainder of the division of two numbers.
- **Syntax**: `divmod(x, y)`

```python
result = divmod(10, 3)
print(result)  # Output: (3, 1)
```

<br><br>

## 📚 enumerate()
- **Description**: The enumerate() function adds a counter to an iterable and returns it as an enumerate object.
- **Syntax**: `enumerate(iterable, start=0)`

```python
numbers = [10, 20, 30, 40, 50]
result = enumerate(numbers)
print(list(result))  # Output: [(0, 10), (1, 20), (2, 30), (3, 40), (4, 50)]
```

<br><br>

## 📚 eval()
- **Description**: The eval() function evaluates the specified expression and returns the result.
- **Syntax**: `eval(expression, globals=None, locals=None)`

```python
result = eval("10 + 20")
print(result)  # Output: 30
```

<br><br>

## 📚 exec()
- **Description**: The exec() function executes the specified Python code.
- **Syntax**: `exec(object, globals=None, locals=None)`

```python
code = "print('Hello, World!')"
exec(code)  # Output: Hello, World!
```

<br><br>

## 📚 filter()
- **Description**: The filter() function constructs an iterator from elements of an iterable for which a function returns true.
- **Syntax**: `filter(function, iterable)`

```python
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5]
result = filter(is_even, numbers)
print(list(result))  # Output: [2, 4]
```

<br><br>

## 📚 float()
- **Description**: The float() function returns a floating-point number from a number or string.
- **Syntax**: `float([x])`

```python
result = float(10)
print(result)  # Output: 10.0
```

<br><br>

## 📚 format()
- **Description**: The format() function formats a value based on the format specifier.
- **Syntax**: `format(value, format_spec)`

```python
result = format(10, "d")
print(result)  # Output: 10
```

- **Format Specifiers**:
  - `d`: Decimal
  - `b`: Binary
  - `o`: Octal
  - `x`: Hexadecimal
  - `f`: Floating-point
  - `e`: Exponential

<br><br>

## 📚 iter()
- **Description**: The iter() function returns an iterator object for the given object.
- **Syntax**: `iter(object, sentinel)`

```python
numbers = [1, 2, 3, 4, 5]
result = iter(numbers)
print(next(result))  # Output: 1
```

<br><br>

## 📚 len()
- **Description**: The len() function returns the length (number of items) of an object.
- **Syntax**: `len(s)`

```python
numbers = [1, 2, 3, 4, 5]
result = len(numbers)
print(result)  # Output: 5
```

<br><br>

## 📚 list()
- **Description**: The list() function creates a new list. It can be used to convert a sequence to a list.
- **Syntax**: `list([iterable])`

```python
result = list((1, 2, 3, 4, 5))
print(result)  # Output: [1, 2, 3, 4, 5]
```

<br><br>

## 📚 map()
- **Description**: The map() function applies a given function to each item of an iterable (list, tuple, etc.) and returns a list of the results.
- **Syntax**: `map(function, iterable)`

```python
def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
result = map(square, numbers)
print(list(result))  # Output: [1, 4, 9, 16, 25]
```

<br><br>

## 📚 max()
- **Description**: The max() function returns the largest item in an iterable or the largest of two or more arguments.
- **Syntax**: `max(iterable, *[, key, default])`

```python
numbers = [10, 20, 30, 40, 50]
result = max(numbers)
print(result)  # Output: 50
```

<br><br>

## 📚 min()
- **Description**: The min() function returns the smallest item in an iterable or the smallest of two or more arguments.
- **Syntax**: `min(iterable, *[, key, default])`

```python
numbers = [10, 20, 30, 40, 50]
result = min(numbers)
print(result)  # Output: 10
```

<br><br>

## 📚 pow()
- **Description**: The pow() function returns the value of x to the power of y.
- **Syntax**: `pow(x, y)`

```python
result = pow(2, 3)
print(result)  # Output: 8
```

<br><br>

## 📚 reversed()
- **Description**: The reversed() function returns a reverse iterator for an iterable.
- **Syntax**: `reversed(sequence)`

```python
numbers = [1, 2, 3, 4, 5]
result = reversed(numbers)
print(list(result))  # Output: [5, 4, 3, 2, 1]
```

<br><br>

## 📚 round()
- **Description**: The round() function returns a floating-point number rounded to the specified number of decimal places.
- **Syntax**: `round(number[, ndigits])`

```python
result = round(10.12345, 2)
print(result)  # Output: 10.12
```

<br><br>

## 📚 range()
- **Description**: The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
- **Syntax**: `range(start, stop, step)`

```python
result = range(5)
print(list(result))  # Output: [0, 1, 2, 3, 4]
```

```python
result = range(1, 5)
print(list(result))  # Output: [1, 2, 3, 4]
```

```python
result = range(1, 10, 2)
print(list(result))  # Output: [1, 3, 5, 7, 9]
```

<br><br>

## 📚 set()
- **Description**: The set() function creates a new set. It can be used to convert a sequence to a set.
- **Syntax**: `set([iterable])`

```python
result = set([1, 2, 3, 4, 5])
print(result)  # Output: {1, 2, 3, 4, 5}
```

<br><br>

## 📚 slice()
- **Description**: The slice() function returns a slice object representing the set of indices specified by range(start, stop, step).
- **Syntax**: `slice(start, stop, step)`

```python
numbers = [1, 2, 3, 4, 5]
s = slice(1, 4)
result = numbers[s]
print(result)  # Output: [2, 3, 4]

s = slice(1, 4, 2) # Start, Stop, Step
result = numbers[s]
print(result)  # Output: [2, 4]
```

<br><br>

## 📚 sorted()
- **Description**: The sorted() function returns a sorted list of the specified iterable object.
- **Syntax**: `sorted(iterable, key=None, reverse=False)`

```python
numbers = [5, 2, 3, 1, 4]
result = sorted(numbers)
print(result)  # Output: [1, 2, 3, 4, 5]
```

```python
numbers = [5, 2, 3, 1, 4]
result = sorted(numbers, reverse=True)
print(result)  # Output: [5, 4, 3, 2, 1]
```

```python
numbers = [5, 2, 3, 1, 4]
result = sorted(numbers, key=lambda x: x % 2) # Sort by even and odd numbers
print(result)  # Output: [2, 4, 5, 1, 3]
```

<br><br>

## 📚 sum()
- **Description**: The sum() function returns the sum of all items in an iterable.
- **Syntax**: `sum(iterable, start=0)`

```python
numbers = [1, 2, 3, 4, 5]
result = sum(numbers)
print(result)  # Output: 15
```

```python
numbers = [1, 2, 3, 4, 5]
result = sum(numbers, 10) # Add 10 to the sum
print(result)  # Output: 25
```

<br><br>

## 📚 tuple()
- **Description**: The tuple() function creates a new tuple. It can be used to convert a sequence to a tuple.
- **Syntax**: `tuple([iterable])`

```python
result = tuple([1, 2, 3, 4, 5])
print(result)  # Output: (1, 2, 3, 4, 5)
```

<br><br>

## 📚 type()
- **Description**: The type() function returns the type of the specified object.
- **Syntax**: `type(object)`

```python
result = type(10)
print(result)  # Output: <class 'int'>
```

```python
result = type("Hello, World!")
print(result)  # Output: <class 'str'>
```

<br><br>

## 📚 zip()
- **Description**: The zip() function returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences.
- **Syntax**: `zip(*iterables)`

```python
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
result = zip(numbers, letters)
print(list(result))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]
```

```python
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
symbols = ['!', '@', '#']
result = zip(numbers, letters, symbols)
print(list(result))  # Output: [(1, 'a', '!'), (2, 'b', '@'), (3, 'c', '#')]
```

<hr>