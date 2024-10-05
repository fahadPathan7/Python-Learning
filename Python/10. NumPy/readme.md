# <div align="center"> 🔰 Level 10 NumPy </div>

## 📌Table of Contents
- [ 🔰 Level 10 NumPy ](#--level-10-numpy-)
  - [📌Table of Contents](#table-of-contents)
  - [📚 Introduction](#-introduction)
  - [📚 Installation](#-installation)
  - [📚 Import NumPy](#-import-numpy)
  - [📚 NumPy Arrays](#-numpy-arrays)
  - [📚 Array Attributes](#-array-attributes)
  - [📚 Basic Array Operations](#-basic-array-operations)
  - [📚 Array Shape Modification](#-array-shape-modification)
  - [📚 Array Concatenating](#-array-concatenating)
  - [📚 Array Generation](#-array-generation)
  - [📚 Vectorization](#-vectorization)
  - [📚 Condition](#-condition)
  - [📚 Handling Missing Data](#-handling-missing-data)
  - [📚 Handling Files](#-handling-files)
<hr>
<br><br>

## 📚 Introduction
- NumPy is a **general-purpose array-processing package**. It provides a high-performance multidimensional array object and tools for working with these arrays.
- It is the fundamental package for scientific computing with Python.
- It contains among other things:
    - A powerful N-dimensional array object
    - Sophisticated (broadcasting) functions
    - Tools for integrating C/C++ and Fortran code
    - Useful linear algebra, Fourier transform, and random number capabilities
    - Besides its obvious scientific uses, NumPy can also be used as an efficient multi-dimensional container of generic data.

<br><br>

## 📚 Installation
- NumPy can be installed using pip.
- To install NumPy, run the following command:
```bash
pip install numpy
```

<br><br>

## 📚 Import NumPy
- To use NumPy, we need to import the module.
```python
import numpy as np # can use any name instead of np. It is a convention to use np.
```

<br><br>

## 📚 NumPy Arrays
- NumPy arrays are a bit like Python lists, but still very much different at the same time.
- NumPy arrays are faster and more memory efficient than Python lists.
- NumPy arrays are a central data structure of the NumPy library.
- NumPy arrays are stored at **one continuous place** in memory unlike lists, so processes can access and manipulate them very efficiently.
- NumPy arrays can be created using the `array()` function.
    ```python
    arr = np.array([1, 2, 3, 4, 5])
    print(arr) # Output: [1 2 3 4 5]
    ```
- NumPy arrays are **homogeneous**. All elements in a NumPy array have to be of the same data type. If we try to assign a value of a different data type to an element in a NumPy array, it will be upcasted to the highest data type. **char (1 byte) -> short (2 bytes) -> int (4 bytes) -> float (4 bytes) -> double (8 bytes)**
    ```python
    arr = np.array([1, 2, 3, 4])
    print(arr.dtype) # Output: int32

    arr = np.array([1, 2, 3, 4.0])
    print(arr.dtype) # Output: float64
    ```
- NumPy arrays can be multidimensional.
    ```python
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    print(arr) # Output: [[1 2 3]
               #          [4 5 6]]
    ```

<br><br>

## 📚 Array Attributes
- NumPy arrays have the following attributes:
    - **ndim**: Number of dimensions.
    - **shape**: Tuple of integers indicating the size of the array in each dimension.
    - **size**: Number of elements in the array.
    - **dtype**: Data type of the elements in the array.
    - **itemsize**: Size in bytes of each element of the array.
    - **data**: Buffer containing the actual elements of the array.
    ```python
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    print(arr.ndim) # Output: 2
    print(arr.shape) # Output: (2, 3)
    print(arr.size) # Output: 6
    print(arr.dtype) # Output: int32
    print(arr.itemsize) # Output: 4
    print(arr.data) # Output: <memory at 0x0000021E3D3A3D00>
    ```

<br><br>

## 📚 Basic Array Operations
- **Arithmetic operations** on NumPy arrays apply **elementwise**.
    ```python
    arr1 = np.array([1, 2, 3, 4])
    arr2 = np.array([5, 6, 7, 8])
    print(arr1 + arr2) # Output: [ 6  8 10 12]
    print(arr1 - arr2) # Output: [-4 -4 -4 -4]
    print(arr1 * arr2) # Output: [ 5 12 21 32]
    print(arr1 / arr2) # Output: [0.2        0.33333333 0.42857143 0.5       ]
    print(arr1 ** arr2) # Output: [    1    64  2187 65536]
    print(arr2 % arr1) # Output: [0 0 1 0]
    ```
- **Comparison operations** on NumPy arrays apply **elementwise**.
    ```python
    arr1 = np.array([1, 2, 3, 4])
    arr2 = np.array([5, 6, 7, 8])
    print(arr1 > arr2) # Output: [False False False False]
    print(arr1 < arr2) # Output: [ True  True  True  True]
    print(arr1 == arr2) # Output: [False False False False]
    ```
- **Matrix multiplication** can be done using the `dot()` function. Dimensions of the two matrices must be compatible for matrix multiplication. (m x n) * (n x p) = (m x p)
    ```python
    arr1 = np.array([[1, 2], [3, 4]])
    arr2 = np.array([[5, 6], [7, 8]])
    print(np.dot(arr1, arr2)) # Output: [[19 22]
                              #          [43 50]]
    print(arr1.dot(arr2)) # Output: [[19 22]
                          #          [43 50]]
    print(arr1 @ arr2) # Output: [[19 22]
                       #          [43 50]]
    ```
- **Elementwise multiplication** can be done using the `multiply()` function. Dimensions of both arrays should be the same. concept: (a11 * a12) (b11 * b12) = (a11 * b11) (a12 * b12)
    ```python
    arr1 = np.array([[1, 2], [3, 4]])
    arr2 = np.array([[5, 6], [7, 8]])
    print(np.multiply(arr1, arr2)) # Output: [[ 5 12]
                                   #          [21 32]]
    ```
- **Transpose** of a matrix can be found using the `transpose()` function. It flips the matrix over its diagonal.
    ```python
    arr = np.array([[1, 2], [3, 4]])
    print(np.transpose(arr)) # Output: [[1 3]
                             #          [2 4]]
    print(arr.T) # Output: [[1 3]
                #          [2 4]]
    ```
- **Sum** of all elements in a NumPy array can be found using the `sum()` function.
    ```python
    arr = np.array([[1, 2], [3, 4]])
    print(np.sum(arr)) # Output: 10
    ```
- **Minimum** and **maximum** elements in a NumPy array can be found using the `min()` and `max()` functions.
    ```python
    arr = np.array([[1, 2], [3, 4]])
    print(np.min(arr)) # Output: 1
    print(np.max(arr)) # Output: 4
    ```
- **Square root** of all elements in a NumPy array can be found using the `sqrt()` function.
    ```python
    arr = np.array([[1, 4], [9, 16]])
    print(np.sqrt(arr)) # Output: [[1. 2.]
                        #          [3. 4.]]
    ```
- **Mean** and **median** of all elements in a NumPy array can be found using the `mean()` and `median()` functions.
    ```python
    arr = np.array([[1, 2], [3, 4]])
    print(np.mean(arr)) # Output: 2.5
    print(np.median(arr)) # Output: 2.5
    ```
- **Standard deviation** and **variance** of all elements in a NumPy array can be found using the `std()` and `var()` functions.
    ```python
    arr = np.array([[1, 2], [3, 4]])
    print(np.std(arr)) # Output: 1.118033988749895
    print(np.var(arr)) # Output: 1.25
    ```

<br><br>

## 📚 Array Shape Modification
- **Reshape** a NumPy array using the `reshape()` function. The new **shape should be compatible** with the original shape.
    ```python
    arr = np.array([1, 2, 3, 4, 5, 6])
    print(arr.reshape(2, 3)) # Output: [[1 2 3]
                             #          [4 5 6]]
    print(arr.reshape(3, 3)) # Output: ValueError: cannot reshape array of size 6 into shape (3,3)
    ```
- **Resize** a NumPy array using the `resize()` function. It changes the shape and size of the array in-place. If the new size is larger than the original size, the new array will be filled with zeros.
    ```python
    arr = np.array([1, 2, 3, 4, 5, 6])
    arr.resize(2, 3)
    print(arr) # Output: [[1 2 3]
              #          [4 5 6]]
    arr.resize(3, 3)
    print(arr) # Output: [[1 2 3]
              #          [4 5 6]
              #          [0 0 0]]
    ```
- **Flatten** a NumPy array using the `flatten()` function. It returns a copy of the array collapsed into one dimension.
    ```python
    arr = np.array([[1, 2], [3, 4]])
    print(arr.flatten()) # Output: [1 2 3 4]
    print(arr) # Output: [[1 2]
              #          [3 4]]
    ```
- **Ravel** a NumPy array using the `ravel()` function. It returns a view of the original array collapsed into one dimension. It is **faster** than `flatten()` as it does not create a copy of the array. It is a **view** of the original array. If we modify the ravelled array, the original array will also be modified.
    ```python
    arr = np.array([[1, 2], [3, 4]])
    print(arr.ravel()) # Output: [1 2 3 4]
    print(arr) # Output: [[1 2]
              #          [3 4]]
    ```

<br><br>

## 📚 Array Concatenating
- **Concatenate** NumPy arrays using the `concatenate()` function. It concatenates the arrays along the specified axis. Axis 0 is the vertical axis, and axis 1 is the horizontal axis. The default axis is 0.
    ```python
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    print(np.concatenate((arr1, arr2))) # Output: [1 2 3 4 5 6]
    arr1 = np.array([[1, 2], [3, 4]])
    arr2 = np.array([[5, 6], [7, 8]])
    print(np.concatenate((arr1, arr2), axis=0)) # Output: [[1 2]
                                                #          [3 4]
                                                #          [5 6]
                                                #          [7 8]]
    print(np.concatenate((arr1, arr2), axis=1)) # Output: [[1 2 5 6]
                                                #          [3 4 7 8]]
    ```
- **Stack** NumPy arrays vertically using the `vstack()` function.
    ```python
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    print(np.vstack((arr1, arr2))) # Output: [[1 2 3]
                                   #          [4 5 6]]
    arr1 = np.array([[1, 2], [3, 4]])
    arr2 = np.array([[5, 6], [7, 8]])
    print(np.vstack((arr1, arr2))) # Output: [[1 2]
                                   #          [3 4]
                                   #          [5 6]
                                   #          [7 8]]
    ```
- **Stack** NumPy arrays horizontally using the `hstack()` function.
    ```python
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    print(np.hstack((arr1, arr2))) # Output: [1 2 3 4 5 6]
    arr1 = np.array([[1, 2], [3, 4]])
    arr2 = np.array([[5, 6], [7, 8]])
    print(np.hstack((arr1, arr2))) # Output: [[1 2 5 6]
                                   #          [3 4 7 8]]
    ```

<br><br>

## 📚 Array Generation
- **Arrange** elements in a NumPy array using the `arange()` function. It returns an array with evenly spaced elements as per the interval.
    ```python
    print(np.arange(10)) # Output: [0 1 2 3 4 5 6 7 8 9]
    print(np.arange(1, 10, 2)) # Output: [1 3 5 7 9]
    ```
- **Linspace** elements in a NumPy array using the `linspace()` function. It returns an array with evenly spaced elements over a specified interval.
    ```python
    print(np.linspace(1, 10, 5)) # Output: [ 1.    3.25  5.5   7.75 10.  ]
    ```
- **Zeros** elements in a NumPy array using the `zeros()` function. It returns an array of zeros with the specified shape.
    ```python
    print(np.zeros((2, 3))) # Output: [[0. 0. 0.]
                           #          [0. 0. 0.]]
    ```
- **Ones** elements in a NumPy array using the `ones()` function. It returns an array of ones with the specified shape.
    ```python
    print(np.ones((2, 3))) # Output: [[1. 1. 1.]
                          #          [1. 1. 1.]]
    ```
- **Identity** matrix using the `eye()` function. It returns a 2-D array with ones on the diagonal and zeros elsewhere.
    ```python
    print(np.eye(3)) # Output: [[1. 0. 0.]
                    #          [0. 1. 0.]
                    #          [0. 0. 1.]]
    ```
- **Random** elements in a NumPy array using the `random.rand()` function. It returns an array of random numbers with the specified shape.
    ```python
    # random numbers between 0 and 1
    print(np.random.rand(2, 3)) # Output: [[0.5488135  0.71518937 0.60276338]
                                #          [0.54488318 0.4236548  0.64589411]]
    # random integers between a range
    print(np.random.randint(1, 10, (2, 3))) # Output: [[6 1 1]
                                            #          [2 8 7]]
    # random numbers from a normal distribution
    print(np.random.randn(2, 3)) # Output: [[-0.80227727  0.16116006  0.83345688]
                                 #          [ 1.10342127  0.09707755  0.96864499]]
    # random choice from a list
    print(np.random.choice([1, 2, 3, 4, 5], (2, 3))) # Output: [[3 4 2]
                                                      #          [5 4 3]]
    ```

<br><br>

## 📚 Vectorization
- **Vectorization** is the process of converting an algorithm from operating on a single value at a time to operating on a set of values (vector) at one time.
- NumPy functions are vectorized. It means that they can operate on the entire array without the need for loops.
- Vectorized operations in NumPy are implemented via **broadcasting**.
- **Broadcasting** is a powerful mechanism that allows NumPy to work with arrays of different shapes when performing arithmetic operations.
```python
def calc(x, y):
    if x > y:
        return x - y
    else:
        return x + y

output = np.vectorize(calc)
print(output([1, 2, 3, 4], [5, 6, 7, 8])) # Output: [6 8 10 12]
```

<br><br>

## 📚 Condition
- **Condition** is a powerful mechanism that allows NumPy to work with arrays of different shapes when performing arithmetic operations.
```python
arr = np.array([1, 2, 10, 45, 60, 95, 56, 78, 89])
print(arr[arr > 50]) # Output: [60 95 56 78 89]
print(arr[arr % 2 == 0]) # Output: [ 2 10 60 56 78]
print(arr[(arr > 50) & (arr % 2 == 0)]) # Output: [60 56 78]
print(arr[(arr > 50) | (arr % 2 == 0)]) # Output: [ 2 10 45 60 95 56 78 89]
```
- Using the `where()` function, we can return elements chosen from `x` or `y` depending on the condition.
```python
arr = np.array([1, 2, 3, 4, 5])
print(np.where(arr % 2 == 0, arr, -1)) # Output: [-1  2 -1  4 -1] # if even, return element, else return -1
print(np.where(arr % 2 == 0, arr, arr * 2)) # Output: [ 2  2  6  4 10] # if even, return element, else return element * 2
print(np.where(arr % 2 == 0, arr, np.where(arr % 3 == 0, arr * 3, arr * 4))) # Output: [ 4  2  9  4 20] # if even, return element, else if divisible by 3, return element * 3, else return element * 4
```

<br><br>

## 📚 Handling Missing Data
- **Missing data** is a common problem in real-world data. It is important to handle missing data properly before we start building models.
- NumPy provides the `nan` constant to represent missing data. It is a special floating-point value that is used to represent missing or undefined data. Its value tends to infinity.
- We can use the `isnan()` function to check for missing data.
    ```python
    arr = np.array([1, 2, np.nan, 4, 5])
    print(np.isnan(arr)) # Output: [False False  True False False]
    ```
- We can use the `nan_to_num()` function to replace missing data with a specific value.
    ```python
    arr = np.array([1, 2, np.nan, 4, 5])
    print(np.nan_to_num(arr, nan=-1)) # Output: [ 1.  2. -1.  4.  5.]
    print(np.nan_to_num(arr, nan=0)) # Output: [1. 2. 0. 4. 5.]
    ```
- We can use the `nanmean()` and `nanmedian()` functions to calculate the mean and median of an array with missing data.
    ```python
    arr = np.array([1, 2, np.nan, 4, 5])
    print(np.nanmean(arr)) # Output: 3.0
    print(np.nanmedian(arr)) # Output: 3.0

    # fill missing data with mean
    arr[np.isnan(arr)] = np.nanmean(arr)
    print(arr) # Output: [1. 2. 3. 4. 5.]

    # fill missing data with median
    arr = np.array([1, 2, np.nan, 4, 5])
    arr[np.isnan(arr)] = np.nanmedian(arr)
    ```
- We can use the `nanstd()` and `nanvar()` functions to calculate the standard deviation and variance of an array with missing data.
    ```python
    arr = np.array([1, 2, np.nan, 4, 5])
    print(np.nanstd(arr)) # Output: 1.5811388300841898
    print(np.nanvar(arr)) # Output: 2.5
    ```
- We can use the `nansum()` and `nanprod()` functions to calculate the sum and product of an array with missing data.
    ```python
    arr = np.array([1, 2, np.nan, 4, 5])
    print(np.nansum(arr)) # Output: 12.0
    print(np.nanprod(arr)) # Output: 40.0
    ```
- We can use the `nanargmax()` and `nanargmin()` functions to find the index of the maximum and minimum values in an array with missing data.
    ```python
    arr = np.array([1, 2, np.nan, 4, 5])
    print(np.nanargmax(arr)) # Output: 4
    print(np.nanargmin(arr)) # Output: 0
    print(arr[np.nanargmax(arr)]) # Output: 5.0
    print(arr[np.nanargmin(arr)]) # Output: 1.0
    print(np.max(arr)) # Output: nan # returns nan if there is a missing value
    ```
- We can use the `nanmax()` and `nanmin()` functions to find the maximum and minimum values in an array with missing data.
    ```python
    arr = np.array([1, 2, np.nan, 4, 5])
    print(np.nanmax(arr)) # Output: 5.0
    print(np.nanmin(arr)) # Output: 1.0
    ```
- Forwards and backwards filling of missing data can be done using the `roll()` function. It shifts the elements of an array by a specified number of positions. **It is useful for filling missing data when the data has a pattern.**
    ```python
    arr = np.array([1, 2, np.nan, 4, 5])
    print(np.roll(arr, 1)) # Output: [ 5.  1.  2. nan  4.]
    print(np.roll(arr, -1)) # Output: [ 2. nan  4.  5.  1.]

    # forwards filling
    arr[np.isnan(arr)] = np.roll(arr, 1)[np.isnan(arr)]
    print(arr) # Output: [1. 2. 2. 4. 5.]

    # backwards filling
    arr = np.array([1, 2, np.nan, 4, 5])
    arr[np.isnan(arr)] = np.roll(arr, -1)[np.isnan(arr)]
    print(arr) # Output: [1. 2. 4. 4. 5.]
    ```

<br><br>

## 📚 Handling Files
- **NumPy** provides functions to handle files.
- **Save** a NumPy array to a file using the `save()` function. It saves the array to a binary file with the `.npy` extension.
    ```python
    arr = np.array([1, 2, 3, 4, 5])
    np.save('arr.npy', arr)

    arr = np.array([[1, 2], [3, 4]])
    np.save('arr1.npy', arr)
    ```
- **Load** a NumPy array from a file using the `load()` function. It loads the array from a binary file with the `.npy` extension.
    ```python
    arr = np.load('arr.npy')
    print(arr) # Output: [1 2 3 4 5]

    arr = np.load('arr1.npy')
    print(arr) # Output: [[1 2]
               #          [3 4]]
    ```
- **Save text** a NumPy array to a text file using the `savetxt()` function. It saves the array to a text file with the specified delimiter. (delimiter is something that separates the values)
    ```python
    arr = np.array([1, 2, 3, 4, 5])
    np.savetxt('arr.txt', arr, delimiter=',')

    arr = np.array([[1, 2], [3, 4]])
    np.savetxt('arr1.txt', arr, delimiter=' ')
    ```
- **Load text** a NumPy array from a text file using the `loadtxt()` function. It loads the array from a text file with the specified delimiter.
    ```python
    arr = np.loadtxt('arr.txt', delimiter=',')
    print(arr) # Output: [1. 2. 3. 4. 5.]

    arr = np.loadtxt('arr1.txt', delimiter=' ')
    print(arr) # Output: [[1. 2.]
               #          [3. 4.]]
    ```
- **Save compressed** a NumPy array to a compressed file using the `savez()` function. It saves the array to a compressed file with the `.npz` extension. It saves multiple arrays in a single file. The arrays are saved as key-value pairs. We can access the arrays using the keys.
    ```python
    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.array([[1, 2], [3, 4]])
    np.savez('arr.npz', arr1=arr1, arr2=arr2)
    ```
- **Load compressed** a NumPy array from a compressed file using the `load()` function. It loads the array from a compressed file with the `.npz` extension.
    ```python
    data = np.load('arr.npz')
    print(data['arr1']) # Output: [1 2 3 4 5]
    print(data['arr2']) # Output: [[1 2]
                        #          [3 4]]
    ```

<hr>