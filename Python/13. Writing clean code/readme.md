# <div align="center"> 🔰 Writing clean and efficient code </div>

## 📌 Table of contents
<hr>
<br><br>

## 📚 Naming variables
- **Use meaningful names**: Choose variable names that are descriptive and easy to understand. Avoid using single-letter variable names like `x` or `y`, unless they are used as loop counters.
- **Use camelCase**: Use camelCase for variable names, starting with a lowercase letter. For example, `myVariable` or `myFunction`.
- **Use underscores for constants**: Use underscores to separate words in constant names. For example, `MAX_SIZE` or `PI`.
- **start with `is` for boolean variables**: Start boolean variable names with `is` or `has` to make their purpose clear. For example, `isActive` or `hasPermission`.

```python
# Bad
x = 10
y = 20

# Good
total_students = 10
total_classes = 20
is_active = True
hoursInDay = 24
```

<br><br>

## 📚 Documentation
- **Use comments**: We should use comments to explain the purpose of the code, especially for complex or non-obvious logic. Comments should be clear, concise, and to the point.
- **Use docstrings**: Use docstrings to document functions, classes, and modules. Docstrings should describe what the function does, what arguments it takes, and what it returns.

```python
# Bad
total = price * quantity

# Good
# Calculate the total price.
total = price * quantity
```

```python
# Bad
def add(x, y):
    return x + y

# Good
def add(x, y):
    """
    Add two numbers.

    Args:
        x: The first number.
        y: The second number.

    Returns:
        The sum of x and y.
    """
    return x + y
```

<br><br>

## 📚 Functions
- **Use descriptive names**: Choose function names that describe what the function does. Avoid generic names like `doSomething` or `processData`.
- **Keep functions short**: Functions should be short and focused on a single task. If a function is too long, consider breaking it up into smaller functions.
- **Avoid side effects**: Functions should not have side effects, such as modifying global variables or printing output. Functions should take input and return output.

```python
# Bad
def process_data(data):
    # Do something
    return result

# Good
def calculate_total(data):
    # Calculate the total
    return total
```

<hr>