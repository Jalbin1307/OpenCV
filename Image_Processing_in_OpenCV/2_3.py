import numpy as np
import cv2 as cv

img = cv.imread(r'C:\Users\USER\OpenCV\OpenCV\starry_night.jpg',0)
rows, cols = img.shape

M = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)
dst = cv.warpAffine(img,M,(cols,rows))


cv.imshow('main',dst)
cv.waitKey(0)
cv.destroyAllWindows()