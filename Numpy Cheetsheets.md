## Numpy cheatsheet 

### Creating Arrays:

```python
a = np.array([1, 2, 3])                  # 1D array
b = np.array([[1, 2], [3, 4]])           # 2D array
c = np.zeros((2, 2))                     # 2x2 array of zeros
d = np.ones((2, 2))                      # 2x2 array of ones
e = np.full((2, 2), 7)                   # 2x2 array filled with 7
f = np.eye(3)                            # 3x3 identity matrix
g = np.random.random((2, 2))             # 2x2 array with random values
h = np.arange(0, 10, 2)                  # Array with values from 0 to 9 with step 2
i = np.linspace(0, 1, 5)                 # Array of 5 values from 0 to 1
```

### Aggregations:

```python
print(np.sum(x))                         # Sum of all elements
print(np.mean(x))                        # Mean of all elements
print(np.std(x))                         # Standard deviation of all elements
print(np.var(x))                         # Variance of all elements
print(np.min(x))                         # Minimum element
print(np.max(x))                         # Maximum element
print(np.argmin(x))                      # Index of minimum element
print(np.argmax(x))                      # Index of maximum element
```

### Reshaping and Slicing:

```python
print(a.shape)                          # (3, 3)
print(a.reshape((1, 9)))                # Reshape to 1x9 array
print(a[0, 1])                          # Access element at row 0, column 1
print(a[:, 1])                          # Access all elements in column 1
print(a[1, :])                          # Access all elements in row 1
print(a[0:2, 0:2])                      # Access subarray from row 0 to 1 and column 0 to 1
```

### Linear Algebra:

```python
print(np.linalg.inv(A))                 # Inverse of A
print(np.linalg.det(A))                 # Determinant of A
print(np.linalg.eig(A))                 # Eigenvalues and eigenvectors of A
```

### Saving and Loading:

```python
np.save('array.npy', a)                 # Save array to a binary file in .npy format
b = np.load('array.npy')                # Load array from .npy file

np.savetxt('array.txt', a)              # Save array to a text file
c = np.loadtxt('array.txt')             # Load array from a text file
```

