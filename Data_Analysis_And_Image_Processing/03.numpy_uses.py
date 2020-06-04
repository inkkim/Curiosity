import numpy as np

# numpy 단일 객체 저장 및 불러오기
array = np.arange(0, 10)
np.save('saved.npy', array)

result = np.load('saved.npy')
print(result)

# numpy 복수 객체 저장 및 불러오기
array1 = np.arange(0, 10)
array2 = np.arange(10, 20)
np.savez('saved.npz', array1 = array1, array2 = array2)

data =np.load('saved.npz')
result1 = data['array1']
result2 = data['array2']
print(result1)
print(result2)


# numpy 원소 오름차순 정렬
array11 = np.array([5, 9, 10, 3, 1])
array11.sort()
print(array11)
# numpy 원소 내림차순 정렬
print(array11[::-1])

# numpy 각 열 기준으로 정렬 (더 큰 요소값이 아래 행으로 정렬)
array111 = np.array([[5, 9, 10, 3, 1], [8, 3, 4, 2, 5]])
print(array111)
array111.sort(axis = 0)
print(array111)
# numpy 균일한 간격으로 데이터 생성
array22 = np.linspace(0, 10, 5)
print(array22)

# numpy 난수의 재연 (실행마다 결과 동일) => Machine Learning 모델 학습 때 활용
## np.random.seed() parameter = 0 < int < 2^32, none
np.random.seed(7)
print(np.random.randint(0, 10, (2, 3)))

# numpy 배열 객체 복사
## array44에 array33을 대입한 후 array44의 특정 요소 값을 수정할 경우
## 서로 같은 주소값을 사용하기 때문에 array33의 값도 변경되는 문제가 있음
### 다음과 같이 copy()함수를 이용하면 이러한 문제를 방지할 수 있음
array33 = np.arange(0, 10)
array44 = array33.copy()
array44[0] = 99
print(array33)
print(array44)

# numpy 중복된 원소 제외
array55 = np.array([1, 1, 2, 2, 3, 3, 4])
print(np.unique(array55))


