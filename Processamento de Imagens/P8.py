import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('MULHERES.jpg')
rows,cols,ch = img.shape

pts1 = np.float32([[50,80],[200,70],[20,350],[111,390]])
pts2 = np.float32([[20,40],[500,20],[500,80],[300,100]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(400,450))

plt.subplot(121),plt.imshow(img),plt.title('Antes')
plt.subplot(122),plt.imshow(dst),plt.title('Depois')
plt.show()