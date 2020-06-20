# Contour 찾기
# cv2.findContours(image, mode, method) 이미지에서 Contour들을 찾는 함수
# mode : Contour들을 찾는 방법
# RETR_EXTERNAL - 바깥쪽 Line만 찾기
# RETR_LIST - 모든 Line을 찾지만, Hierachy 구성 X
# RETR_TREE - 모든 Line을 찾으며, 모든 Hierachy 구성 O
# method : Contour들을 찾는 근사치 방법
# CHAIN_APPROX_NONE - 모든 Contour 포인트 저장
# CHAIN_APPROX_SIMPLE - Contour Line을 그릴 수 있는 포인트만 저장
## 입력 이미지는 Gray Scale Threshold 전처리 과정이 필요

# Contour 그리기
# cv2.drawContours(image, contours, contour_index, color, thickness) Contour들을 그리는 함수
# contour_index : 그리고자 하는 Contour Line(전체 : -1)

import cv2

image = cv2.imread('123.jpg')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(image_gray, 127, 255, 0)

cv2.imshow('ForContour', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

contours = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0]
image = cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

cv2.imshow('Contours', image)
cv2.waitKey(0)