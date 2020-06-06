import cv2

# 이미지를 투명을 제외한 컬러영역만 읽고, 보여준다.
img_basic = cv2.imread('cat.jpg', cv2.IMREAD_COLOR)
cv2.imshow('Image Basic', img_basic)
cv2.waitKey(0)
cv2.imwrite('result1.png', img_basic)

# cv2.waitKey(0) 명령을 수행하면 모든 창을 닫는다.
cv2.destroyAllWindows()

# 이미지를 Gary Scale로 변환하고, 보여준다.
img_gray = cv2.cvtColor(img_basic, cv2.COLOR_BGR2GRAY)
cv2.imshow('Image Basic', img_gray)
cv2.waitKey(0)
cv2.imwrite('result2.png', img_gray)