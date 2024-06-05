
# My Pandas Cheatsheet

## Importing and Exporting Data

```python
import pandas as pd

# Reading data from a CSV file
df = pd.read_csv('file.csv')

# Writing data to a CSV file
df.to_csv('file.csv', index=False)

# Reading data from an Excel file
df = pd.read_excel('file.xlsx')

# Writing data to an Excel file
df.to_excel('file.xlsx', index=False)
```


## Creating DataFrames

```python
# Creating a DataFrame from a dictionary
data = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data)

# Creating a DataFrame from a list of lists
data = [[1, 2], [3, 4]]
df = pd.DataFrame(data, columns=['col1', 'col2'])
```

## Viewing and Inspecting Data

```python
# Displaying the first few rows
print(df.head())

# Displaying the last few rows
print(df.tail())

# Getting a summary of the DataFrame
print(df.info())

# Descriptive statistics
print(df.describe())
```

## Selecting Data

```python
# Selecting a single column
col1 = df['col1']

# Selecting multiple columns
cols = df[['col1', 'col2']]

# Selecting rows by index
row = df.iloc[0]

# Selecting rows by label
row = df.loc[0]

# Boolean indexing
filtered_df = df[df['col1'] > 1]
```

## Data Cleaning

```python
# Handling missing values
df.dropna(inplace=True)     # Drop missing values
df.fillna(0, inplace=True)  # Fill missing values with 0

# Renaming columns
df.rename(columns={'col1': 'new_col1'}, inplace=True)

# Dropping columns
df.drop(columns=['col1'], inplace=True)

# Duplicates
df.drop_duplicates(inplace=True)
```

## Data Manipulation

```python
# Adding a new column
df['new_col'] = df['col1'] + df['col2']

# Applying a function to a column
df['col1'] = df['col1'].apply(lambda x: x * 2)

# Grouping data
grouped = df.groupby('col1').sum()

# Merging DataFrames
merged_df = pd.merge(df1, df2, on='col1')
```

## Sorting and Ordering

```python
# Sorting by column values
df.sort_values(by='col1', ascending=False, inplace=True)

# Sorting by index
df.sort_index(inplace=True)
```

## Date and Time

```python
# Converting a column to datetime
df['date_col'] = pd.to_datetime(df['date_col'])

# Extracting year, month, day
df['year'] = df['date_col'].dt.year
df['month'] = df['date_col'].dt.month
df['day'] = df['date_col'].dt.day
```

## Concatenation

```python
# Concatenating DataFrames
df = pd.concat([df1, df2], axis=0)  # Vertical concatenation
df = pd.concat([df1, df2], axis=1)  # Horizontal concatenation
```

## String Operations

```python
# String methods
df['upper'] = df['text'].str.upper()                        # Convert to uppercase
df['lower'] = df['text'].str.lower()                        # Convert to lowercase
df['is_upper'] = df['text'].str.isupper()                   # Check if the string is uppercase
df['is_lower'] = df['text'].str.islower()                   # Check if the string is lowercase
df['length'] = df['text'].str.len()                         # Get the length of the string
df['starts_with_H'] = df['text'].str.startswith("H")        # Check if the string starts with "H"
df['split'] = df['text'].str.split()                        # Split the string at each space
df['index_of_World'] = df['text'].str.find("World")         # Find the index of the substring "World"
df['stripped'] = df['text'].str.strip()                     # Strip whitespaces from both sides
df['replaced'] = df['text'].str.replace("World", "Python")  # Replace "World" with "Python"
```

## Aggregations

```python
# Aggregation functions
df['col1'].mean()  # Mean
df['col1'].sum()   # Sum
df['col1'].min()   # Minimum
df['col1'].max()   # Maximum
df['col1'].count() # Count
```



