import cv2

image = cv2.imread('cat.jpg')

# 픽셀 수 및 이미지 크기 확인
print(image.shape)
print(image.size)

# 이미지 Numpy 객체의 특정 위치(X축, Y축) 픽셀을 가르킴
px = image[300, 100]

# B, G, R 순서로 출력됨
# 단, Gray Scale인 경우에는 오직 흑백에 대한 정보만 담고
# 있기 때문에 B, G, R로 구분되지 않음
print(px)

# R 값만 출력하기
print(px[2])

# 특정 범위 픽셀 변경
import time
image1 = cv2.imread('cat.jpg')

## for문 이용 픽셀 직접 접근
start_time = time.time()
for i in range(0, 100):
    for j in range(0, 100):
        image1[i, j] = [255, 255, 255]
print('--- %s second ---' % (time.time() - start_time))

## 범위 지정 변경 (실행속도 약 30배 빠름)
start_time = time.time()
image1[0:100, 0:100] = [0, 0, 0]
print('--- %s second ---' % (time.time() - start_time))

cv2.imshow('Image Calculation', image1)
cv2.waitKey(0)
cv2.destroyAllWindows()
# ROI(Region of Interest) 추출 및 복사
image2 = cv2.imread('cat.jpg')

# Numpy Slicing: ROI 처리 가능
roi = image2[200:350, 50:200]

# ROI 단위로 이미지 복사하기
image2[0:150, 0:150] = roi

cv2.imshow('ROI', image2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 픽셀별로 색상 다루기
image3 = cv2.imread('cat.jpg')
image3[:, :, 2] = 0

cv2.imshow('pixel managing', image3)
cv2.waitKey(0)
cv2.destroyAllWindows()