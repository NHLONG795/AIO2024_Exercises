import numpy as np

arr = np.arange(10)
arr[arr % 2 == 1] = -1
# print(arr)

arr1 = np.arange(10).reshape(2, -1)
arr2 = np.repeat(1, 10).reshape(2, -1)
c = np.concatenate([arr1, arr2], axis=1)

arr3 = np.array([2, 6, 1, 9, 10, 3, 27])
index = np.where((arr3 >= 5) & (arr3 <= 10))
print(arr3[index])

arr4 = np.array([5, 7, 9, 8, 6, 4, 5])
arr5 = np.array([6, 3, 4, 8, 9, 7, 1])

print(np.where(arr4 < arr5, arr5, arr4))
