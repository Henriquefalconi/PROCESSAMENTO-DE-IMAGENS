import cv2
import numpy as np

img = cv2.imread('MULHERES.jpg', 0)
rows, cols = img.shape

M = np.float32([[1,0,200],[0,1,100]])
dst = cv2.warpAffine(img,M,(cols,rows))
res = cv2.resize(img, None, fx=0.2, fy=0.2, interpolation=cv2.INTER_CUBIC)

cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
