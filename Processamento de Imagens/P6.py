import cv2

img = cv2.imread('MULHERES.jpg',0)
rows,cols = img.shape

M = cv2.getRotationMatrix2D((cols/2,rows/2),170,1)
dst = cv2.warpAffine(img,M,(cols,rows))
res = cv2.resize(img, None, fx=0.1, fy=0.1, interpolation=cv2.INTER_CUBIC)
cv2.imshow('img',res)
cv2.waitKey(0)
cv2.destroyAllWindows()
