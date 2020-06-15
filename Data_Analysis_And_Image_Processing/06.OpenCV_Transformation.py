# 이미지 크기 조절
## 이미지를 크게 만들려면 픽셀 수를 임의로 늘려야 하는데,
## 이 픽셀은 어떻게 채울까?
### 1) 보간법 (interpolation); 픽셀 A, B 사이에 값을 적절한 값으로 채우는 방법

import cv2
import numpy as np

# 이미지 원본
image = cv2.imread('123.jpg')
cv2.imshow('Image Transformation', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 이미지 확대 (cv2.resize(이미지 Numpy 변수, Manual Size, x축 비유, y축 비유, 보간법))
expand = cv2.resize(image, None, fx=1.5, fy=1.5, interpolation = cv2.INTER_CUBIC)
cv2.imshow('Image Expand', expand)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 이미지 축소
shrink =cv2.resize(image, None, fx=0.8, fy=0.8, interpolation = cv2.INTER_CUBIC)
cv2.imshow("Image Shrink", shrink)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 이미지 위치 변경 (cv2.warpAffine(image, M, dsize)
## M: 변환행렬 / dsize: Manual Size
## 변환행렬을 어떻게 만들지에 따라서 평행이동과 회전도 가능하다.
### 변환행렬은 2x3 행렬 형태로 정의

height, width = image.shape[:2]

M = np.float32([[1, 0, 50], [0, 1, 10]])
dst = cv2.warpAffine(image, M, (width, height))
cv2.imshow("Image Warp", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 이미지 회전 (cv2.getRotationMatrix2D(center, angle, scale)
## getRotationMatrix2D Method는 WarpAffine의 Parameter인 M(변환행렬)을
## 구하는 Method 이다.
## center: 회전 중심 / angle: 회전 각도 / scale: Scale Factor

image = cv2.imread('123.jpg')
height, width = image.shape[:2]
# center(width/2, height/2) = 회전중심 정중앙
M = cv2.getRotationMatrix2D((width/2, height/2), 90, 0.5)
rot = cv2.warpAffine(image, M, (width, height))
cv2.imshow('Image Rotation', rot)
cv2.waitKey(0)