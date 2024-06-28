import numpy as np


def showArrFeatures(array):
    print(
        f"形状: {array.shape}, 长度: {len(array)}, 维数: {array.ndim}, 大小: {array.size}"
    )


# 一维数组/向量
arr_1ndim = np.array([-3, -2, -1, 0, 1, 2])
showArrFeatures(arr_1ndim)  # 形状: (6,), 长度: 6, 维数: 1, 大小: 6
# 二维数组/矩阵
arr_2ndim_1 = np.array([[-3, -2, -1], [0, 1, 2]])
arr_2ndim_2 = np.array([[-3, -2, -1, 0, 1, 2]])
arr_2ndim_3 = np.array([[-3], [-2], [-1], [0], [1], [2]])
showArrFeatures(arr_2ndim_1)  # 形状: (2, 3), 长度: 2, 维数: 2, 大小: 6
showArrFeatures(arr_2ndim_2)  # 形状: (1, 6), 长度: 1, 维数: 2, 大小: 6
showArrFeatures(arr_2ndim_3)  # 形状: (6, 1), 长度: 6, 维数: 2, 大小: 6
# 三维数组
arr_3ndim = np.array(
    [
        [[-12, -11, -10, -9], [-8, -7, -6, -5], [-4, -3, -2, -1]],
        [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]],
    ]
)
showArrFeatures(arr_3ndim)  # 形状: (2, 3, 4), 长度: 2, 维数: 3, 大小: 24
