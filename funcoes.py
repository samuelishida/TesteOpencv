import cv2
import numpy

img = cv2.imread('phoenix.jpg',1)

def rotate(img, teta):
	rows,cols = img.shape
	M = cv2.getRotationMatrix2D((cols/2,rows/2),teta,1)
	return cv2.warpAffine(img,M,(cols,rows))
def mirror(img):
	return cv2.flip(img, 1)

#cv2.imshow('Phoenix',rotate(img,45))
cv2.imshow('Phoenix',mirror(img))

cv2.waitKey(0)

cv2.destroyAllWindows()


