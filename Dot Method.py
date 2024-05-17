# dot method
import numpy as np

#Example 1
arrayX1 = np.array([[2.5, 3.7], [4.9, 5.1]])
arrayY1 = np.array([[1, 2], [3, 4]])

result = np.dot(arrayX1,arrayY1)

print(f'Example 1:{result}')

#Example 2
arrayX2 = np.array([[1, 2], [3, 4]])
arrayY2 = np.array([[5, 6], [7, 8]])

result = np.dot(arrayX2, arrayY2)

print(f"Example 2: {result}")

#Example 3
arrayX3 = np.array([[1, 2], [3, 4]])
arrayY3 = np.array([5, 6])

result = np.dot(arrayX3, arrayY3)

print(f"Example 3: {result}")