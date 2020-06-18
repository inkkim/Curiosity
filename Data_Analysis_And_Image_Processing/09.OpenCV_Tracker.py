# Tracker 사용 방법 / Tracker를 생성하는 함수
# cv2.createTrackbar(track_bar_name, window_name, value, count, on_change)
## value : 초기값
## count : Max값 (Min:0)
## on_change : 값이 변경될 때 호출되는 Callback 함수

import cv2
import numpy as np

# 각 Trackbar가 가지는 값(R, G, B)을 받아와서
# 전체 이미지 영역에 받아온 값을 ((B, G, R)-OpneCV는 BGR순서) 순서로 수정

def change_color(x):
    r = cv2.getTrackbarPos("R", "Image")
    g = cv2.getTrackbarPos("G", "Image")
    b = cv2.getTrackbarPos("B", "Image")
    image[:] = [b, g, r]
    cv2.imshow('Image', image)

# 임의의 사이즈 이미지 생성
image = np.zeros((600, 400, 3), np.uint8)

# 이미지가 출력될 수 있는 윈도우 생성
cv2.namedWindow("Image")

# 3가지 Trackbar를 Image 윈도우에 달아준다
## 각각의 Trackbar는 0 - 255 값으로 수정할 수 있다.
## 수정 후 change_color()를 실행
cv2.createTrackbar("R", "Image", 0, 255, change_color)
cv2.createTrackbar("G", "Image", 0, 255, change_color)
cv2.createTrackbar("B", "Image", 0, 255, change_color)

cv2.imshow('Image', image)
cv2.waitKey(0)


