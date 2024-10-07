# <div align="center"> 🔰 Level 11 Pandas & Polars </div>

## 📌 Table of Contents
- [ 🔰 Level 11 Pandas \& Polars ](#--level-11-pandas--polars-)
  - [📌 Table of Contents](#-table-of-contents)
  - [📚 Pandas](#-pandas)
  - [📚 Polars](#-polars)
  - [📚 Pandas vs Polars](#-pandas-vs-polars)
  - [📚 Basic use](#-basic-use)
    - [🔖 Install and Import](#-install-and-import)
    - [🔖 Read files](#-read-files)
    - [🔖 Shape \& Schema](#-shape--schema)
    - [🔖 Show basic \& statistical data](#-show-basic--statistical-data)
    - [🔖 Filter rows](#-filter-rows)
    - [🔖 Series](#-series)
    - [🔖 Accessing data attributes](#-accessing-data-attributes)
    - [🔖 DataFrame operations](#-dataframe-operations)
    - [🔖 Handling missing data](#-handling-missing-data)
    - [🔖 Map](#-map)
    - [🔖 Merging \& Joining](#-merging--joining)
    - [🔖 Strings](#-strings)
    - [🔖 Data visualization](#-data-visualization)
<hr>
<br><br>

## 📚 Pandas
- Pandas is a fast, powerful, flexible and easy to use open-source data analysis and data manipulation library built on top of the Python programming language.
- It is a popular data manipulation library that is built on top of Python.
- It offers data structures and operations for manipulating numerical tables and time series.

<br><br>

## 📚 Polars
- Polars is a blazingly fast data manipulation library built in Rust and designed for speed and safety.

<br><br>

## 📚 Pandas vs Polars
| Description | Pandas | Polars |
| --- | --- | --- |
| Language | Python | Rust |
| Speed | Slower | Faster |
| Memory | High | Low |
| Safety | Low | High |
| Flexibility | High | Low |
| Ease of use | High | Low |

<br><br>

## 📚 Basic use

### 🔖 Install and Import
| Description | Pandas | Polars |
| --- | --- | --- |
| Install | `pip install pandas` | `pip install polars` |
| Import | `import pandas as pd` | `import polars as pl` |

### 🔖 Read files
| Description | Pandas | Polars |
| --- | --- | --- |
| Read CSV | `pd_data = pd.read_csv('data.csv')` | `pl_data = pl.read_csv('data.csv')` |
| Read Parquet. (Parquet is a columnar storage file format) | `pd_data = pd.read_parquet('data.parquet')` | `pl_data = pl.read_parquet('data.parquet')` |
| Read JSON | `pd_data = pd.read_json('data.json')` | `pl_data = pl.read_json('data.json')` |
| Read Excel | `pd_data = pd.read_excel('data.xlsx')` | `pl_data = pl.read_excel('data.xlsx')` |

### 🔖 Shape & Schema
| Description | Pandas | Polars |
| --- | --- | --- |
| Print shape | `print(pd_data.shape)` <br> output: (rows, columns) | `print(pl_data.shape)` <br> output: (rows, columns) |
| Print schema. (Column names and data types) | `print(pd_data.dtypes)` | `print(pl_data.schema)` |

### 🔖 Show basic & statistical data
| Description | Pandas | Polars |
| --- | --- | --- |
| Print first 5 rows | `print(pd_data.head())` | `print(pl_data.head())` |
| Print few first rows | `print(pd_data.head(10))` | `print(pl_data.head(10))` |
| Print last 5 rows | `print(pd_data.tail())` | `print(pl_data.tail())` |
| Print few last rows | `print(pd_data.tail(10))` | `print(pl_data.tail(10))` |
| Print summary statistics | `print(pd_data.describe())` <br> output: count, mean, std, min, 25%, 50%, 75%, max | `print(pl_data.describe())` <br> output: count, null_count, mean, std, min, 25%, 50%, 75%, max |
| Print Info (Column names, data types, non-null values) | `print(pd_data.info())` <br> or: `print(pd_data.info(verbose=False))` | `print(pl_data.info())` |
| Print column names | `print(pd_data.columns)` | `print(pl_data.columns)` |
| Print unique values in a column | `print(pd_data['column_name'].unique())` <br> output: [value1, value2, ...] | `print(pl_data['column_name'].unique())` <br> output: [value1, value2, ...] |
| Print number of unique values in a column | `print(pd_data['column_name'].nunique())` <br> output: number | `print(pl_data['column_name'].n_unique())` <br> output: number |
| loc[idx] (Access a group of rows and columns by labels) | `print(pd_data.loc[0])` <br> `print(pd_data.loc[0:5])` <br> output: data of row 0 <br> data of rows 0 to 5 | `print(pl_data.loc[0])` <br> `print(pl_data.loc[0:5])` <br> output: data of row 0 <br> data of rows 0 to 5 |
| iloc[idx] (Purely integer-location based indexing for selection by position) | `print(pd_data.iloc[0])` <br> `print(pd_data.iloc[0:5])` <br> output: data of row 0 <br> data of rows 0 to 5 | `print(pl_data.iloc[0])` <br> `print(pl_data.iloc[0:5])` <br> output: data of row 0 <br> data of rows 0 to 5 |

### 🔖 Filter rows
| Description | Pandas | Polars |
| --- | --- | --- |
| Filter rows | `print(pd_data[pd_data['column_name'] == 'value'])` | `print(pl_data.filter(pl.col('column_name') == 'value'))` |
| Filter rows with multiple conditions | `print(pd_data[(pd_data['column_name1'] == 'value1') & (pd_data['column_name2'] == 'value2')])` | `print(pl_data.filter((pl.col('column_name1') == 'value1') & (pl.col('column_name2') == 'value2')))` |
| Filter rows with multiple conditions | `print(pd_data[(pd_data['column_name1'] == 'value1') \| (pd_data['column_name2'] == 'value2')])` | `print(pl_data.filter((pl.col('column_name1') == 'value1') \| (pl.col('column_name2') == 'value2')))` |

### 🔖 Series
- A series is a one-dimensional array that can hold any data type such as integers, floats, and strings.

| Description | Pandas | Polars |
| --- | --- | --- |
| Create a series | `pd_series = pd.Series([1, 2, 3, 4, 5])` <br> `pd_series = pd.Series('name', index=['a', 'b', 'c', 'd', 'e'])` | `pl_series = pl.Series([1, 2, 3, 4, 5])` <br> `pl_series = pl.Series('name', ['a', 'b', 'c', 'd', 'e'])` |
| Slicing series | `print(pd_series[1:3])` | `print(pl_series.slice(1, 3))` |
| Print series | `print(pd_series)` | `print(pl_series)` |
| Print series values | `print(pd_series.values)` | `print(pl_series.to_numpy())` |
| Print series index | `print(pd_series.index)` | `print(pl_series.to_numpy())` <br> In polars, series index is not directly accessible. |

### 🔖 Accessing data attributes
| Description | Pandas | Polars |
| --- | --- | --- |
| Data type | `print(pd_data.dtypes)` | `print(pl_data.schema)` <br> `print(pl_data.dtypes)` <br> difference between schema and dtypes is that schema is a method and dtypes is an attribute but both return the same output. |
| Shape | `print(pd_data.shape)` <br> output: (rows, columns) | `print(pl_data.shape)` <br> output: (rows, columns) |
| Name | `print(pd_data.name)` <br> output: name of the dataframe | `print(pl_data.name)` <br> output: name of the dataframe |
| Length | `print(len(pd_data))` <br> output: number of rows | `print(len(pl_data))` <br> output: number of rows |
| Sum | `print(pd_data.sum())` <br> output: sum of all columns. <br> `print(pd_data['column_name'].sum())` <br> output: sum of a column | `print(pl_data.sum())` <br> output: sum of all columns. <br> `print(pl_data['column_name'].sum())` <br> output: sum of a column |
| Mean | `print(pd_data.mean())` <br> output: mean of all columns. <br> `print(pd_data['column_name'].mean())` <br> output: mean of a column | `print(pl_data.mean())` <br> output: mean of all columns. <br> `print(pl_data['column_name'].mean())` <br> output: mean of a column |
| Median | `print(pd_data.median())` <br> output: median of all columns. <br> `print(pd_data['column_name'].median())` <br> output: median of a column | `print(pl_data.median())` <br> output: median of all columns. <br> `print(pl_data['column_name'].median())` <br> output: median of a column |
| Mode | `print(pd_data.mode())` <br> output: mode of all columns. <br> `print(pd_data['column_name'].mode())` <br> output: mode of a column | `print(pl_data.mode())` <br> output: mode of all columns. <br> `print(pl_data['column_name'].mode())` <br> output: mode of a column |
| Standard deviation | `print(pd_data.std())` <br> output: standard deviation of all columns. <br> `print(pd_data['column_name'].std())` <br> output: standard deviation of a column | `print(pl_data.std())` <br> output: standard deviation of all columns. <br> `print(pl_data['column_name'].std())` <br> output: standard deviation of a column |
| Minimum | `print(pd_data.min())` <br> output: minimum of all columns. <br> `print(pd_data['column_name'].min())` <br> output: minimum of a column | `print(pl_data.min())` <br> output: minimum of all columns. <br> `print(pl_data['column_name'].min())` <br> output: minimum of a column |
| Maximum | `print(pd_data.max())` <br> output: maximum of all columns. <br> `print(pd_data['column_name'].max())` <br> output: maximum of a column | `print(pl_data.max())` <br> output: maximum of all columns. <br> `print(pl_data['column_name'].max())` <br> output: maximum of a column |
| Count | `print(pd_data.count())` <br> output: count of all columns. <br> `print(pd_data['column_name'].count())` <br> output: count of a column | `print(pl_data.count())` <br> output: count of all columns. <br> `print(pl_data['column_name'].count())` <br> output: count of a column |
| Unique | `print(pd_data['column_name'].unique())` <br> output: unique values in a column <br> `print(pd_data['column_name'].nunique())` <br> output: number of unique values in a column | `print(pl_data['column_name'].unique())` <br> output: unique values in a column <br> `print(pl_data['column_name'].n_unique())` <br> output: number of unique values in a column |

### 🔖 DataFrame operations
| Description | Pandas | Polars |
| --- | --- | --- |
| Set index | `pd_data.set_index('column_name')` | `pl_data.set_column('column_name')` |
| Reset index | `pd_data.reset_index()` | `pl_data.reset_index()` |
| Select columns (it will show only the selected columns) | `print(pd_data[['column_name1', 'column_name2']])` | `print(pl_data.select(['column_name1', 'column_name2']))` |
| Filter columns (it will show all columns except the selected columns or condition) | `print(pd_data.filter(['column_name1', 'column_name2']))` | `print(pl_data.filter(pl_data['column_name1'] > 100))` |
| Drop columns (it will remove the selected columns) | `print(pd_data.drop(['column_name1', 'column_name2'], axis=1))` <br> axis 1 is for columns | `print(pl_data.drop(['column_name1', 'column_name2']))` |
| Drop rows (it will remove the selected rows) | `print(pd_data.drop([0, 1, 2], axis=0)` <br> axis 0 is for rows | `print(pl_data.drop([0, 1, 2]))` |
| Drop duplicates | `print(pd_data.drop_duplicates())` | `print(pl_data.drop_duplicates())` |
| Sort values | `print(pd_data.sort_values('column_name', ascending=False))` <br> ascending=False for descending order | `print(pl_data.sort('column_name', reverse=True))` <br> reverse=True for descending order |

### 🔖 Handling missing data
| Description | Pandas | Polars |
| --- | --- | --- |
| Check for missing values (it will show True for missing values) | `print(pd_data.isnull())` | `print(pl_data.is_null())` |
| Drop missing values (it will remove rows with missing values) | `print(pd_data.dropna())` | `print(pl_data.drop_nulls())` |
| Fill missing values (fill missing values with a specific value) | `print(pd_data.fillna(0))` | `print(pl_data.fill_null(0))` |
| Interpolate missing values (fill missing values with the mean of the column) | `print(pd_data.interpolate())` | `print(pl_data.interpolate())` |
| Fill missing values (fill missing values with the mean of the column. This way mode, median, and other methods can be used) | `print(pd_data.fillna(pd_data.mean()))` | `print(pl_data.fill_null(pl_data.mean()))` |

### 🔖 Map
- Map is a function that applies a function to all the items in an input_list.
- It is a convenient way to apply a function to every item in the list.
- It is a built-in function in Python.

| Description | Pandas | Polars |
| --- | --- | --- |
| Apply a function to a column | `print(pd_data['column_name'].map(lambda x: x * 2))` | `print(pl_data['column_name'].apply(lambda x: x * 2))` |
| Transform a column | `print(pd_data['column_name'].transform(lambda x: x * 2))` | `print(pl_data['column_name'].apply(lambda x: x * 2))` |

- Transform & Map are the same in Polars.

### 🔖 Merging & Joining
- Merging is a process of bringing two data frames together into one, and aligning the rows based on one or more keys.
- Joining is a process of combining two data frames based on the columns.

| Description | Pandas | Polars |
| --- | --- | --- |
| Merge data frames | `pd_data = pd.merge(data1, data2, on='column_name' how='inner')` | `pl_data = data1.join(data2, on='column_name', how='inner')` |
| Join data frames | `pd_data = pd_data1.join(data2, on='column_name', how='inner')` | `pl_data = data1.join(data2, on='column_name', how='inner')` |

- In Polars, join is used for both merge and join operations.
- inner: Use intersection of keys from both frames. Show only the rows that have matching keys in both data frames.
- outer: Use union of keys from both frames. Show all rows from both data frames.
- left: Use keys from the left data frame only. Show all rows from the left data frame. but when there is no match, show NaN from the right data frame.
- right: Use keys from the right data frame only. Show all rows from the right data frame. but when there is no match, show NaN from the left data frame.

### 🔖 Strings
- lower(): Converts all characters in the string to lowercase. (other methods: upper(), title() etc. can also be used)
  ```python
  print(pd_data['column_name'].str.lower())
  print(pl_data['column_name'].to_lower())
  ```
- multiple string operations can be performed using the str attribute in pandas and the str module in polars.
  ```python
  print(pd_data['column_name'].str.lower().str.replace(' ', '_'))
  print(pl_data['column_name'].str().to_lower().replace(" ", "_"))
  ```

### 🔖 Data visualization
- Pandas has built-in data visualization capabilities.
- Polars does not have built-in data visualization capabilities.
- Polars is a data manipulation library and not a data visualization library.
- Polars can be used with other data visualization libraries such as Matplotlib, Seaborn, Plotly, etc.

```python
pd_data['column_name'].plot(kind='hist')
```

kind:
- line: line plot
- bar: vertical bar plot
- barh: horizontal bar plot
- hist: histogram
- box: boxplot
- kde: Kernel Density Estimation plot
- density: same as kde
- area: area plot
- pie: pie plot
- scatter: scatter plot
- hexbin: hexbin Plot

<hr>





