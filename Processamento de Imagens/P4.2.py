import cv2
import numpy as np

img = cv2.imread('MULHERES.jpg')

height, width = img.shape[:2]
res = cv2.resize(img, (4*width, 4*height), interpolation=cv2.INTER_CUBIC)
res = cv2.resize(img, None, fx=0.2, fy=0.2, interpolation=cv2.INTER_CUBIC)
cv2.imshow('imagem', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
