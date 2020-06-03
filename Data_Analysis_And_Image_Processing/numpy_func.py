#2020.06.03

# numpy 상수 연산 (덧셈, 뺄셈, 곱셈, 나눗셈)
import numpy as np

array = np.random.randint(1, 10, size=4).reshape(2, 2)
print(array)

result1_array = array + 10
result2_array = array - 10
result3_array = array * 10
result4_array = array / 10
print("+ =\n", result1_array)
print("- =\n", result2_array)
print("* =\n", result3_array)
print("/ =\n", result4_array)

# numpy 배열 연산

array1 = np.arange(4).reshape(2, 2) # (2 x 2)
array2 = np.arange(4).reshape(2, 2) # (2 x 2)

array3 = array1 + array2 # +, -, *, / 모두 가능
print("array1 =\n", array1)
print("array2 =\n", array2)
print("array3 =\n", array3)

# numpy 서로 다른 형태의 배열 연산
## 브로드캐스트 : 형태가 다른 배열을 연산할 수 있도록 배열의 형태를 동적으로 변환
array11 = np.arange(8).reshape(2, 4) # (2 x 4)
array22 = np.arange(8).reshape(2, 4) # (2 x 4)
array33 = np.concatenate([array11, array22], axis = 0)
array44 = np.arange(4).reshape(4, 1) # (4 x 1)

print("array33 :\n", array33)
print("array44 :\n", array33 + array44)

# numpy 마스킹 연산
##마스킹 : 각 원소에 대하여 체크함
array111 = np.arange(16).reshape(4, 4) # (4 x 4)
array222 = array111 < 10
print("array222 :\n", array222)

# numpy 마스킹 활용
## 이미지 처리에서 색상이 너무 밝은 픽셀을 선택적으로 수정할 때 활용 가능
## 원소 하나씩 접근하여 수정하는 방법보다 효율적이고 빠른 연산 가능
array111[array222] = 100
print("array111 :\n", array111)

# numpy 집계 함수
array1111 = np.arange(16).reshape(4, 4)

print("최대값: ", np.max(array1111))
print("최소값: ", np.min(array1111))
print("합계: ", np.sum(array1111))
print("평균값: ", np.mean(array1111))

## 특정 축만 선택적으로 연산 가능
print("array1111: \n", array1111)
print("합계 : ", np.sum(array1111, axis = 0))
