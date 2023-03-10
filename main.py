import cv2

#영상소스열기
src1 = cv2.imread('c:/images/picture27.jpg')

##영상처링 알고리즘
dst1 = cv2.cvtColor(src1, cv2.COLOR_RGB2GRAY)

#영상 디스플레이
cv2.imshow('src1', src1)
cv2.imshow('dst1', dst1)

#마무리
cv2.waitKey(0)
cv2.destroyAllWindows()
