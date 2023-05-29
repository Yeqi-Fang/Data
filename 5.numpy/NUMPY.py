import numpy as np

# 一维数组
arr1 = np.array([1, 2, 3, 4, 5])

# 二维数组
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

# 三维数组
arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])


arr = np.array([1, 2, 3, 4, 5])

# 使用整数索引访问单个元素
print(arr[0])  # 输出: 1

# 使用切片索引访问多个元素
print(arr[1:4])  # 输出: [2, 3, 4]

# 使用布尔值索引选择满足条件的元素
mask = arr > 3
print(arr[mask])  # 输出: [4, 5]

# 修改数组中的元素
arr[2] = 10
print(arr)  # 输出: [1, 2, 10, 4, 5]
