import cv2
import numpy

#***************************#

def rotate(img, teta):
	rows , cols = img.shape[:2]
	M = cv2.getRotationMatrix2D((cols/2,rows/2),teta,1)
	return cv2.warpAffine(img,M,(cols,rows))
def mirror(img):
	return cv2.flip(img, 1)

#***************************#

img = cv2.imread('phoenix.jpg',1)

#cv2.imshow('Phoenix',rotate(img,45))
#cv2.imshow('Phoenix',mirror(img))
#cv2.imwrite('phoenix_rotate.jpg',rotate(img,45))
#cv2.imwrite('phoenix_mirror.jpg',mirror(img))

cv2.waitKey(0)

cv2.destroyAllWindows()


