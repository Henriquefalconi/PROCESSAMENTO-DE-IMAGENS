import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('MULHERES.jpg')
rows,cols,ch = img.shape

pts1 = np.float32([[10,50],[20,70],[100,200]])
pts2 = np.float32([[10,100],[150,50],[100,300]])

M = cv2.getAffineTransform(pts1,pts2)

dst = cv2.warpAffine(img,M,(cols,rows))

plt.subplot(121),plt.imshow(img),plt.title('Antes')
plt.subplot(122),plt.imshow(dst),plt.title('Depois')
plt.show()
