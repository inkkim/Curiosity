## image 안에서 특정한 사물의 테두리를 얻을 수 있는 함수 Contour
# Contour의 사각형 외각 찾기
# cv2.boundingRect(contour) Contour를 포함하는 사각형을 그림
# 사각형의 X, Y 좌표와 너비, 높이를 반환

import cv2
image = cv2.imread('digit.jpg')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(image_gray, 130, 255, 0)
#thresh = cv2.bitwise_not(thresh)

cv2.imshow('blackwhite',thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]
image = cv2.drawContours(image, contours, -1, (0, 0, 255), 4)

cv2.imshow('contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

contour = contours[0]
x, y, w, h = cv2.boundingRect(contour)
print(x, y, w, h)
image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 3)

cv2.imshow('tangle contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

contour = contour[0]
hull = cv2.convexHull(contour, True )
image = cv2.drawContours(image, [hull], 0, (255, 0, 0), 4)

cv2.imshow('hull', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# cv2.approxPolyDP(curve, epsilon, closed) 근사치 Contour를 구한다.
## curve : Contour
## epsilon : 최대 거리 (클수록 Point 개수 감소)
## closed : 폐곡선 여부

contour = contours[0]
# epsilon 값이 작아질수록 적절한 다각형을 그릴 수 있다.
epsilon = 0.0001 * cv2.arcLength(contour, True)
approx = cv2.approxPolyDP(contour, epsilon, True)
image = cv2.drawContours(image, [approx], -1, (0, 255, 0), 4)

cv2.imshow('PolyDP', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# cv2.contourArea(contour) Contour의 면적을 구한다.
area = cv2.contourArea(contour)
print(area)

# cv2.arcLength(contour) Contour의 둘레를 구한다.
length = cv2.arcLength(contour, True)
print(length)

# cv2.momnets(contour) Contour의 특징을 추출한다.
M = cv2.moments(contour)
print(M)

cv2.imshow('Final', image)
cv2.waitKey(0)