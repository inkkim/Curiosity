import numpy as np
"""
list_data = [1, 2, 3]
array = np.array(list_data)

print(array.size)
print(array.dtype)
print(array[1])

# 0부터 3까지의 배열 만들기
array1 = np.arange(4)
print(array1)

# n x n 배열 모든 값 0으로 초기화 후 데이터타입은 실수로 가진다
array2 = np.zeros((4, 4), dtype=float)
print(array2)

# n x n 배열 모든 값 1로 초기화 후 데이터타입은 문자열로 가진다.
array3 = np.ones((3, 3), dtype=str)
print(array3)

# 0부터 9까지 랜덤하게 초기화 된 배열 생성
array4 = np.random.randint(0, 10, (3, 3))
print(array4)

# 통계적으로 특정 분포를 따르는 데이터 생성
# 평균이 0이고, 표준편차가 1인 표준 정규를 띄는 배열
array5 = np.random.normal(0, 1, (3, 3))
print(array5)

# 배열 합치기
sum_array1 = np.array([1, 2, 3])
sum_array2 = np.array([4, 5, 6])
sum_array3 = np.concatenate([sum_array1,sum_array2])

print(sum_array3.shape)
print(sum_array3)

# 배열 형태 바꾸기
reshape_array4 = sum_array3.reshape(3, 2)
print(reshape_array4)

# 배열 세로 축으로 합치기
comb_array1 = np.arange(4).reshape(1, 4)
comb_array2 = np.arange(8).reshape(2, 4)

print(comb_array1)
print(comb_array2)

comb_array3 = np.concatenate([comb_array1, comb_array2], axis = 0)
print(comb_array3)"""

# 배열 나누기
split_array1 = np.arange(8).reshape(2, 4)
left, right = np.split(split_array1, [2], axis=1)
print(split_array1)
print(left.shape)
print(right.shape)

# 커밋돼라
