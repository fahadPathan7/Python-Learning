# <div align="center"> 🔰 Mojo </div>

## 📌 Table of contents
<hr>
<br><br>

## 📚 Introduction
Mojo is a programming language designed for high-performance computing, particularly in the context of machine learning and artificial intelligence. It aims to combine the ease of use of Python with the performance of lower-level languages like C++.

<br><br>

## 📚 Features
- **Ease of use**: Mojo is designed to be easy to learn and use, with a syntax that is similar to Python.
- **Performance**: Mojo is designed to be fast, with performance comparable to C++.
- **Interoperability**: Mojo can be used with other languages like Python, C++, and Java.
- **Scalability**: Mojo is designed to scale to large datasets and complex algorithms.
- **Flexibility**: Mojo is designed to be flexible, with support for a wide range of data types and algorithms.
- **Extensibility**: Mojo is designed to be extensible, with support for custom data types and algorithms.

<br><br>

## 📚 Variables
`var`, `let`, and `alias` are used to declare variables in Mojo. `var` is used to declare a variable that can be reassigned, `let` is used to declare a variable that cannot be reassigned, and `alias` is used to declare an alias for a variable.

```mojo
var x = 10
let y = 20
alias z = x
```

<br><br>

## 📚 Data types
Mojo supports a wide range of data types, including integers, floats, strings, arrays, and dictionaries.

```mojo
var x: int = 10
var y: float = 10.5
var z: string = "hello"
var a: array[int] = [1, 2, 3]
var b: dict[string, int] = {"a": 1, "b": 2, "c": 3}
```

<br><br>

## 📚 Condition
Mojo supports `if`, `elif`, and `else` statements for conditional execution. (same as Python)

```mojo
var x = 10
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")
```

<br><br>

## 📚 Loops
Mojo supports `for` and `while` loops for iteration. (same as Python)

```mojo
for i in range(5):
    print(i)

var i = 0
while i < 5:
    print(i)
    i += 1
```

<br><br>

## 📚 Functions
Mojo supports functions with optional arguments and return values.

```mojo
func add(x: int, y: int) -> int:
    return x + y

var result = add(10, 20)
print(result)
```

<br><br>

## 📚 Classes
Mojo supports classes with methods and properties.

```mojo
class Point:
    var x: int
    var y: int

    func __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    func distance(self, other: Point) -> float:
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

var p1 = Point(0, 0)
var p2 = Point(3, 4)
var d = p1.distance(p2)
print(d)
```

<br><br>

## 📚 Error Handling
Mojo supports `try`, `except`, and `finally` blocks for error handling.

```mojo
try:
    var x = 1 / 0
except:
    raise Error("Error")
finally:
    print("Done")
```

<br><br>

## 📚 Inout, Borrowed, Owned
Mojo supports `inout`, `borrowed`, and `owned` references for memory management.

- `inout` is used for mutable references.
```mojo
func add(x: inout int, y: int):
    x += y

var x = 10
add(x, 20)
print(x) # 30
```

- `borrowed` is used for immutable references.
```mojo
func add(x: borrowed int, y: int) -> int:
    return x + y

var x = 10
var y = add(x, 20)
print(y)
```

- `owned` is used for transferring ownership.
```mojo
func create() -> owned int:
    return 10

var x = create()
print(x)
```

<hr>