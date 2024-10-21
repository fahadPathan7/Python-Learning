# <div align="center"> 🔰 Python Generator </div>

## 📌 Table of Contents
- [ 🔰 Python Generator ](#--python-generator-)
  - [📌 Table of Contents](#-table-of-contents)
  - [📚 Python Generator](#-python-generator)
  - [📚 Generator Expression](#-generator-expression)
  - [📚 Generator Function](#-generator-function)
  - [📚 Advantages of Generators](#-advantages-of-generators)
  - [📚 Pipeline of Data](#-pipeline-of-data)
<hr>
<br><br>

## 📚 Python Generator
- **Generators** are simple functions that return an iterable set of items, one at a time, in a special way.
```python
def my_gen():
    n = 1
    print('This is printed first') # This is printed first
    yield n # value of n is returned

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n

a = my_gen() # a is a generator object
print(next(a)) # This is printed first 1
print(next(a)) # This is printed second 2
print(next(a)) # This is printed at last 3
```

<br><br>

## 📚 Generator Expression
- **Generator Expression** is a simple way to create a generator object.
```python
my_list = [1, 2, 3, 4, 5]
gen = (x**2 for x in my_list)
print(next(gen)) # 1
print(next(gen)) # 4
print(next(gen)) # 9
print(next(gen)) # 16
print(next(gen)) # 25
```

<br><br>

## 📚 Generator Function
- **Generator Function** is a function that returns an iterator object.
```python
def my_gen(n):
    for i in range(n):
        yield i

a = my_gen(3)
print(next(a)) # 0
print(next(a)) # 1
print(next(a)) # 2
```

<br><br>

## 📚 Advantages of Generators
- **Memory Efficient**: A normal function to return a sequence will create the entire sequence in memory before returning the result. This is an overkill if the number of items in the sequence is very large. Generator implementation of such sequence is memory friendly and is preferred since it only produces one item at a time. (even infinite loop will not crash the system!)
- **Represent Infinite Stream**: Generators are excellent mediums to represent an infinite stream of data. Infinite streams cannot be stored in memory and since generators produce only one item at a time, it can represent infinite stream of data.
- **Pipeline of Data**: Generators can be used to pipeline a series of operations. This is best illustrated using an example.

<br><br>

## 📚 Pipeline of Data
- **Pipeline of Data** is a series of operations that are executed one after the other.
```python
def square_numbers(nums):
    for i in nums:
        yield i*i

def negative_numbers(nums):
    for i in nums:
        yield -i

my_nums = square_numbers([1, 2, 3, 4, 5])
my_nums = negative_numbers(my_nums)
for num in my_nums:
    print(num)
```
- The above code will print the square of the negative numbers of the given list.
- The pipeline of data is created by passing the generator object to the next function.
- The code will crash if we use return instead of yield in the above functions.

---