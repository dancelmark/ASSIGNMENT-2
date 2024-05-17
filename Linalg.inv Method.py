# linalg.inv method
import numpy as np
from numpy.linalg import inv

#Example 1
arrayX1 = np.array([[2.75, 3], [4.25, 5]])

result = inv(arrayX1)

print(f'Example 1:{result}')

#Example 2
arrayX2 = np.array([[1, 2], [3, 4]])

result = inv(arrayX2)

print(f'Example 2:{result}')

#Example 3
arrayX3 = np.array([[2, 3], [1,3]])

result = inv(arrayX3)

print(f'Example 3:{result}')