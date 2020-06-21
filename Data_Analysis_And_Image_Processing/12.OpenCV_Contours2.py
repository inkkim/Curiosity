# Contour의 사각형 외각 찾기
# cv2.boundingRect(contour) Contour를 포함하는 사각형을 그림
# 사각형의 X, Y 좌표와 너비, 높이를 반환

import cv2
image = cv2.imread('horse.png')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(image_gray, 200, 255, 0)
thresh = cv2.bitwise_not(thresh)

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
hull = cv2.convexHull(contour)
image = cv2.drawContours(image, [hull], -1, (255, 0, 0), 4)

cv2.imshow('hull', image)
cv2.waitKey(0)
