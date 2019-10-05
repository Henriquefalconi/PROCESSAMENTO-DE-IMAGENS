import cv2

im = cv2.imread('MULHERES.jpg')
img = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
cv2.imshow('imagem',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
