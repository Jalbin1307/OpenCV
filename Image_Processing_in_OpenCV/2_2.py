import numpy as np
import cv2 as cv

img = cv.imread(r'C:\Users\USER\OpenCV\OpenCV\starry_night.jpg',0)
rows, cols = img.shape

M = np.float32([[1,0,200],[0,1,100]])
dst = cv.warpAffine(img,M,(cols,rows))

cv.imshow('img',dst)
cv.imshow('main',img)
cv.waitKey(0)
cv.destroyAllWindows()