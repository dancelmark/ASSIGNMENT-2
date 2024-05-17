# linalg.det method
import numpy as np
from numpy.linalg import det

#Example 1
arrayX1 = np.array([[4, 6], [3, 9]])

result = det(arrayX1)

print(f'Example 1:{result}')

#Example 2
arrayX2 = np.array([[7, 3], [4, 9]])

result = det(arrayX2)
print(f'Example 2:{result}')

#Example 3
arrayX3 = np.array([[8, 3, 9], [0, 4, 6], [2, 7, 9]])

result = det(arrayX3)
print(f'Example 3:{result}')