# <div align="center"> 🔰 Level 5 The List Data Type and the Sum Function </div>

## 📌 Table of Contents
- [ 🔰 Level 5 The List Data Type and the Sum Function ](#--level-5-the-list-data-type-and-the-sum-function-)
  - [📌 Table of Contents](#-table-of-contents)
  - [📚 List Data Type](#-list-data-type)
  - [📚 The `sum()` Function](#-the-sum-function)
<hr>
<br><br>

## 📚 List Data Type
- is a collection which is ordered and changeable. Allows duplicate members.
- Lists are written with square brackets.
    ```python
    thislist = ["apple", "banana", "cherry"]
    print(thislist) # Output: ['apple', 'banana', 'cherry']
    ```
- Access Items
    ```python
    thislist = ["apple", "banana", "cherry"]
    print(thislist[1]) # Output: banana
    ```
- Change Item Value
    ```python
    thislist = ["apple", "banana", "cherry"]
    thislist[1] = "blackcurrant"
    print(thislist) # Output: ['apple', 'blackcurrant', 'cherry']
    ```
- Loop Through a List
    ```python
    thislist = ["apple", "banana", "cherry"]
    for x in thislist:
        print(x)
    ```
- Check if Item Exists
    ```python
    thislist = ["apple", "banana", "cherry"]
    if "apple" in thislist:
        print("Yes, 'apple' is in the fruits list")
    ```
- List Length
    ```python
    thislist = ["apple", "banana", "cherry"]
    print(len(thislist)) # Output: 3
    ```
- Add Items
    ```python
    thislist = ["apple", "banana", "cherry"]
    thislist.append("orange")
    print(thislist) # Output: ['apple', 'banana', 'cherry', 'orange']
    ```
- Remove Item
    ```python
    thislist = ["apple", "banana", "cherry"]
    thislist.remove("banana")
    print(thislist) # Output: ['apple', 'cherry']
    ```
- Remove Specified Index
    ```python
    thislist = ["apple", "banana", "cherry"]
    thislist.pop(1)
    print(thislist) # Output: ['apple', 'cherry']
    ```
- Clear List
    ```python
    thislist = ["apple", "banana", "cherry"]
    thislist.clear()
    print(thislist) # Output: []
    ```
- Copy a List
    ```python
    thislist = ["apple", "banana", "cherry"]
    mylist = thislist.copy()
    # mylist = thislist[:] # Another way to copy a list
    # mylist = list(thislist) # Another way to copy a list
    # mylist = thislist # This will not copy the list, it will only create a reference to the original list
    print(mylist) # Output: ['apple', 'banana', 'cherry']
    ```
- Join Two Lists
    ```python
    list1 = ["a", "b", "c"]
    list2 = [1, 2, 3]
    list3 = list1 + list2
    print(list3) # Output: ['a', 'b', 'c', 1, 2, 3]
    ```
- 2D List
    ```python
    thislist = [["apple", "banana", "cherry"], ["orange", "lemon", "pineapple"]]
    print(thislist) # Output: [['apple', 'banana', 'cherry'], ['orange', 'lemon', 'pineapple']]
    ```

<br><br>

## 📚 The `sum()` Function
- The `sum()` function adds the items of an **iterable** and returns the sum.
    ```python
    numbers = [1, 2, 3, 4, 5]
    print(sum(numbers)) # Output: 15
    ```
- The `sum()` function can also be used on a **range**.
    ```python
    numbers = range(1, 6) # 1, 2, 3, 4, 5 (6 is not included)
    print(sum(numbers)) # Output: 15
    ```
<hr>