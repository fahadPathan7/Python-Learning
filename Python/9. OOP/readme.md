# <div align="center"> 🔰 Level 9 OOP </div>

## 📌Table of Contents
- [ 🔰 Level 9 OOP ](#--level-9-oop-)
  - [📌Table of Contents](#table-of-contents)
  - [📚 class](#-class)
  - [📚 Inheritance](#-inheritance)
  - [📚 Encapsulation](#-encapsulation)
  - [📚 Polymorphism](#-polymorphism)
  - [📚 Magic Dunder method](#-magic-dunder-method)
  - [📚 Composition](#-composition)
  - [📚 Inheritance vs Composition](#-inheritance-vs-composition)
  - [📚 Aggregation](#-aggregation)
<hr>
<br><br>

## 📚 class
- class is a blueprint for creating objects (a particular data structure), providing initial values for state (member variables or attributes), and implementations of behavior (member functions or methods).
- The user-defined objects are created using the class keyword.

```python
class MyClass:
    x = 5

# also can use ()
class MyClass():
    x = 5

var = MyClass()
print(var.x) # Output: 5
```

- The `__init__()` function is called automatically every time the class is being used to create a new object.
- The `self` parameter is a reference to the current instance of the class and is used to access variables that belong to the class.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)
print(p1.name) # Output: John
print(p1.age) # Output: 36
```

- We can modify the object's properties after it is created.

```python
p1.age = 40
print(p1.age) # Output: 40
```

- class has two types of members:
    - **Class members**: These are shared by all instances of the class.
    - **Instance members**: These are unique to each instance of the class.

```python
class Dog:
    kind = 'canine' # class variable shared by all instances

    def __init__(self, name):
        self.name = name # instance variable unique to each instance

a = Dog('Fido')
b = Dog('Buddy')
print(a.kind) # Output: canine
print(b.kind) # Output: canine
print(a.name) # Output: Fido
print(b.name) # Output: Buddy
```

<br><br>

## 📚 Inheritance
- Inheritance allows us to define a class that inherits all the methods and properties from another class.
- The class that inherits the properties is called the child class, and the class that is being inherited from is called the parent class.

```python
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    pass # pass keyword is used when a statement is required syntactically but we do not want any command or code to execute.

x = Student("Mike", "Olsen")
x.printname() # Output: Mike Olsen
```

<br><br>

## 📚 Encapsulation
- Encapsulation is one of the fundamental concepts in object-oriented programming (OOP). It describes the idea of wrapping data and the methods that work on data within one unit.
- This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data.
- To prevent accidental change, an object's variable can only be changed by an object's method. Those types of variables are known as private variables.

```python
class Computer:
    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell() # Output: Selling Price: 900

c.__maxprice = 1000 # This will not change the price because __maxprice is a private variable.
c.sell() # Output: Selling Price: 900 (private variable is not changed)

c.setMaxPrice(1000)
c.sell() # Output: Selling Price: 1000
```

<br><br>

## 📚 Polymorphism
- Polymorphism is an important concept in programming, which allows objects to be treated in a generic way.
- Polymorphism means "many forms", and it occurs when we have many classes that are related to each other by inheritance.
- Polymorphism uses those methods to perform different tasks. This allows us to perform a single action in different ways.

```python
class Parrot:
    def fly(self):
        print("Parrot can fly")

class Penguin:
    def fly(self):
        print("Penguin can't fly")

def flying_test(bird):
    bird.fly()

parrot = Parrot()
penguin = Penguin()

flying_test(parrot) # Output: Parrot can fly
flying_test(penguin) # Output: Penguin can't fly
```

- method overriding: In Python, the method overriding is an ability of a class to change the implementation of a method provided by one of its base classes.

```python
# parent class
class Bird:
    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("Most of the birds can fly but some cannot.")

# child class
class Sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")

obj = Sparrow()
obj.intro() # Output: There are many types of birds.
obj.flight() # Output: Sparrows can fly.
```

- method overloading: Python does not support method overloading. We may overload the methods but can only use the latest defined method.

<br><br>

## 📚 Magic Dunder method
- Dunder methods are special methods with double underscores at the beginning and end of their names.
- They are also called magic methods.
- Dunder methods let us emulate the behavior of built-in types.

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return "Employee Name: {}, Salary: {}".format(self.name, self.salary)

    def __add__(self, other):
        return self.salary + other.salary

emp1 = Employee("John", 1000)
emp2 = Employee("Doe", 2000)

print(emp1) # Output: Employee Name: John, Salary: 1000
print(emp1 + emp2) # Output: 3000
```

- `__str__`: This method is called when we use the print() function on an object.
- `__add__`: This method is called when we use the + operator on an object.
- `__len__`: This method is called when we use the len() function on an object.
- `__getitem__`: This method is called when we access an item from an object.
- `__setitem__`: This method is called when we set the value of an item in an object.
- `__delitem__`: This method is called when we delete an item from an object.

<br><br>

## 📚 Composition
- Composition is a concept that models a has a relationship.
- It enables creating complex types by combining objects of other types.
- This means that a class Composite can contain an object of another class Component.

```python
class Salary:
    def __init__(self, pay):
        self.pay = pay

    def get_total(self):
        return self.pay

class Employee:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus
        self.obj_salary = Salary(self.pay) # creating an object of the Salary class.

    def get_total_salary(self):
        return self.obj_salary.get_total() + self.bonus

emp = Employee(1000, 500)
print(emp.get_total_salary()) # Output: 1500
```

<br><br>

## 📚 Inheritance vs Composition
- Inheritance is an "is a" relationship, while composition is a "has a" relationship.
- Inheritance is a mechanism of extending the base class, whereas composition is a mechanism of creating a complex type using simple types.
- Inheritance is a top-down mechanism, whereas composition is a bottom-up mechanism.

<br><br>

## 📚 Aggregation
- Aggregation is a concept that models a has a relationship.
- It is a more specialized version of the association relationship.
- It is a way to design a relationship between objects.

```python
class Salary:
    def __init__(self, pay):
        self.pay = pay

    def get_total(self):
        return self.pay

class Employee:
    def __init__(self, pay, bonus):
        self.pay = pay # instance of Salary class.
        self.bonus = bonus

    def get_total_salary(self):
        return self.pay.get_total() + self.bonus # calling the get_total() method of the Salary class.

sal = Salary(1000)
emp = Employee(sal, 500) # sal is an object of Salary class. It is passed as an argument to the Employee class.
print(emp.get_total_salary()) # Output: 1500
```
<hr>



