# 이미지를 합치는 두가지 방법
## 1. cv2.add(): Saturation 연산을 수행합니다.
## 0보다 작으면 0, 255보다 크면 255로 표현 (clip)
## 2. np.add(): Modulo(나머지를 의미) 연산을 수행합니다.
## 256은 0, 257은 1로 표현 [(256 % 256 = 0), (257 % 256 = 1)]
### !! 연산을 시작하기 전에 합치려는 두 이미지의 사이즈가 같아야 함 !!
import cv2

image_1 = cv2.imread('catz.jpg')
image_2 = cv2.imread('123.jpg')

# cv2 method, Saturation 연산
result = cv2.add(image_1, image_2)
cv2.imshow('Result of Saturation', result)
cv2.waitKey()
cv2.destroyAllWindows()

# Numpy 기본 연산, Modulo
## 특정한 픽셀에 대해 값이 255가 넘어가면 다시 0부터 출발하므로
## 이상하게 보일 수 있음
result = image_1 + image_2
cv2.imshow('Result of Modulo', result)
cv2.waitKey()
cv2.destroyAllWindows()