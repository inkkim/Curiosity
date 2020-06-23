# 필터링
# 이미지에 커널을 적용하여 이미지를 흐리게(Blurring = Smoothing) 처리할 수 있다.
# 이미지를 흐리게 만들면 노이즈 및 손상을 줄일 수 있다.
# 컨볼루션 계산 ; 특정한 이미지에서 커널을 적용해 컨볼루션을 계산하여 필터링을 수행할 수 있다.
# 원본 이미지에 커널을 각 위치에 맞게 가중치를 곱하고 결과값의 합을 커널의 합으로 나눴을 때의 값을 해당 픽셀의 값으로 씀

# 커널의 종류
## Basic Kernel ; 전부다 같은 가중치를 가진다
## Gaussian Kernel ; 가중치가 정규분포를 따른다. (중간일수록 값이 크다)

import cv2
import numpy as np

image = cv2.imread('123.jpg')
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 사이즈가 커질수록 블러 효과 UP
size = 4
# np.ones(x, y) x * y 사이즈 float 1 값을 가지는 객체
kernel = np.ones((size, size), np.float32) / size ** 2
print(kernel)

# cv2.filter2D ; 모든 픽셀에 대해서 4 * 4크기의 영역을 확인하고 거기서 평균값으로 해당 픽셀의 값을 바꾼다.
dst = cv2.filter2D(image, -1, kernel)
cv2.imshow('Image', dst)
cv2.waitKey(0)


