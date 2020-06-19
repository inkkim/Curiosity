# 직선 그리기
# cv2.line(image, start, end, color, thickness) 하나의 직선을 그리는 함수
# start : 시작 좌표(2차원)
# end : 종료 좌표(2차원)
# thickness : 선의 두께

import cv2
import numpy as np

image = np.full((512, 512, 3), 255, np.uint8)
image = cv2.line(image, (0 ,0), (255, 255), (255, 0, 0), 3)

cv2.imshow('Figure', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 사각형 그리기
# cv2.rectangle(image, start, end, color, thickness) 하나의 사각형을 그리는 함수
# start : 시작 좌표(2차원)
# end : 종료 좌표(2차원)
# thickness : 선의 두께 (채우기: -1)

image1 = np.full((512, 512, 3), 255, np.uint8)
image1 = cv2.rectangle(image, (20, 20), (255, 255), (0, 0, 255), -1)

cv2.imshow('Square', image1)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 원 그리기
# cv2.circle(image, center, radian, color, thickness) 하나의 원을 그리는 함수
# center : 원의 중심(2차원)
# radina : 반지름
# thickness : 선의 두께 (채우기 : -1)

image2 = np.full((512, 512, 3), 255, np.uint8)
image2 = cv2.circle(image, (255, 255), 30, (125, 255, 0), -1)

cv2.imshow('Circle', image2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 다각형 그리기
# cv2.polylines(image, points, is_closed, color, thickness) 하나의 다각형을 그리는 함수
# points : 꼭지점들
# is_closed : 닫힌 도형 여부
# thickness : 선의 두께 (채우기 : -1)
"""
image3 = np.full((512, 512, 3), 255, np.uint8)
points = np.array([[5, 5], [128, 258], [483, 444], [400, 150]])
image3 = cv2.polylines(image3, [points], True, (0, 0, 255), 4)

cv2.imread('PolyLines',image3)
cv2.waitKey(0)
"""

# 글씨 그리기
# cv2.putText(image, text, position, font_type, font_scale, color) 하나의 텍스트를 그리는 함수
# position : 텍스트가 출력될 위치
# font_type : 글씨체
# font_scale : 글시 크기 가중치

image4 = np.full((512, 512, 3), 255, np.uint8)
image4 = cv2.putText(image4, 'Hello World!', (0, 200), cv2.FONT_ITALIC, 2, (255, 0, 0))

cv2.imshow('Text', image4)
cv2.waitKey(0)