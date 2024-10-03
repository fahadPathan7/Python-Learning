# <div align="center"> 🔰 Level 7 More Data Types Tuple, Dictionary and Set </div>

## 📌 Table of Contents
- [ 🔰 Level 7 More Data Types Tuple, Dictionary and Set ](#--level-7-more-data-types-tuple-dictionary-and-set-)
  - [📌 Table of Contents](#-table-of-contents)
  - [📚 Tuple Data Type](#-tuple-data-type)
  - [📚 Dictionary Data Type](#-dictionary-data-type)
  - [📚 Set Data Type](#-set-data-type)
  - [📚 list vs tuple vs dictionary Vs set](#-list-vs-tuple-vs-dictionary-vs-set)
<hr>
<br><br>

## 📚 Tuple Data Type
- is a collection which is **ordered and unchangeable**. Allows duplicate members.
- Tuples are written with round brackets.
    ```python
    thistuple = ("apple", "banana", "cherry")
    print(thistuple) # Output: ('apple', 'banana', 'cherry')
    ```
- Access Items
    ```python
    thistuple = ("apple", "banana", "cherry")
    print(thistuple[1]) # Output: banana
    ```
- Add Items (tricky way)
    ```python
    thistuple = ("apple", "banana", "cherry")
    y = list(thistuple)
    y.append("orange")
    thistuple = tuple(y)
    print(thistuple) # Output: ('apple', 'banana', 'cherry', 'orange')
    ```
- Remove Items (tricky way)
    ```python
    thistuple = ("apple", "banana", "cherry")
    y = list(thistuple)
    y.remove("apple")
    thistuple = tuple(y)
    print(thistuple) # Output: ('banana', 'cherry')
    ```
- index() Method
    ```python
    thistuple = ("apple", "banana", "cherry")
    print(thistuple.index("cherry")) # Output: 2
    ```
- count() Method
    ```python
    thistuple = ("apple", "banana", "cherry", "apple")
    print(thistuple.count("apple")) # Output: 2
    ```

<br><br>

## 📚 Dictionary Data Type
- is a collection which is **unordered, changeable and indexed**. No duplicate members (keys). (it is like a hash table or a map in other languages)
- Dictionaries are written with curly brackets, and they have keys and values.
    ```python
    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    print(thisdict) # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
    ```
- Accessing Items
    ```python
    x = thisdict["model"]
    print(x) # Output: Mustang
    ```
- Change Values
    ```python
    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    thisdict["year"] = 2018
    print(thisdict) # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2018}
    ```
- Adding Items
    ```python
    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    thisdict["color"] = "red"
    print(thisdict) # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}
    ```
- Delete Items
    ```python
    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    thisdict.pop("model")
    print(thisdict) # Output: {'brand': 'Ford', 'year': 1964}
    ```
- Delete Dictionary
    ```python
    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    del thisdict
    print(thisdict) # Output: NameError: name 'thisdict' is not defined
    ```
- Clear Dictionary
    ```python
    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    thisdict.clear()
    print(thisdict) # Output: {}
    ```
- Loop Through a Dictionary
    ```python
    for x in thisdict:
        print(x)
    ```
    Loop through both keys and values
    ```python
    for x, y in thisdict.items():
        print(x, y)
    ```
    loop through keys
    ```python
    for x in thisdict.keys():
        print(x)
        print(thisdict[x])
    ```

<br><br>

## 📚 Set Data Type
- is a collection which is **unordered and unindexed**. No duplicate members.
- Sets are written with curly brackets.
    ```python
    thisset = {"apple", "banana", "cherry"}
    print(thisset) # Output: {'apple', 'banana', 'cherry'}

    thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
    print(thisset) # Output: {'apple', 'banana', 'cherry'}

    thisset = set(["apple", "banana", "cherry"]) # note the single square-brackets
    print(thisset) # Output: {'apple', 'banana', 'cherry'}
    ```
- Access Items
    ```python
    thisset = {"apple", "banana", "cherry"}
    for x in thisset:
        print(x)
    ```
- Add Items
    ```python
    thisset = {"apple", "banana", "cherry"}
    thisset.add("orange")
    print(thisset) # Output: {'apple', 'banana', 'cherry', 'orange'}
    ```
- Delete Items
    ```python
    thisset = {"apple", "banana", "cherry"}
    thisset.remove("banana")
    print(thisset) # Output: {'apple', 'cherry'}

    # using pop() method
    thisset = {"apple", "banana", "cherry"}
    thisset.pop() # Output: 'apple'. Note: Sets are unordered, so when using the pop() method, we will not know which item that gets removed.
    print(thisset) # Output: {'banana', 'cherry'}
    ```
- Clear Items
    ```python
    thisset = {"apple", "banana", "cherry"}
    thisset.clear()
    print(thisset) # Output: set()
    ```
- Join Two Sets
    ```python
    set1 = {"a", "b", "c"}
    set2 = {1, 2, 3}
    set3 = set1.union(set2)
    print(set3) # Output: {1, 2, 3, 'a', 'b', 'c'}
    ```
- Difference (Return a set that contains the items that only exist in set1, and not in set2)
    ```python
    set1 = {"apple", "banana", "cherry"}
    set2 = {"google", "microsoft", "apple"}
    set3 = set1.difference(set2)
    print(set3) # Output: {'banana', 'cherry'}
    ```
- Intersection (Return a set that contains the items that exist in both set1, and set2)
    ```python
    set1 = {"apple", "banana", "cherry"}
    set2 = {"google", "microsoft", "apple"}
    set3 = set1.intersection(set2)
    print(set3) # Output: {'apple'}
    ```

<br><br>

## 📚 list vs tuple vs dictionary Vs set
| List | Tuple | Dictionary | Set |
| --- | --- | --- | --- |
| Ordered | Ordered | Unordered | Unordered |
| Changeable | Unchangeable | Changeable | Changeable |
| Allows duplicate members | Allows duplicate members | No duplicate members | No duplicate members |

<hr>




