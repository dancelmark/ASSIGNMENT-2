# flatten method
import numpy as np

#Example 1
array1X = np.array([[4, 2, 7], [6, 1, 9]])

result = array1X.flatten()
print(f'Example 1:{result}')

#EXAMPLE 2
arrayX2 = np.array([[[7, 9], [3, 2]], [[4, 9], [7, 8]]])

result = arrayX2.flatten()
print(f'Example 2:{result}')

#Example 3
arrayX3 = np.array([[5, 2], [3, 9]])
arrayY3 = np.array([[7, 6], [3, 8]])

z = np.dot(arrayX3, arrayY3)

result = z.flatten()
print(f'Example 3:{result}')