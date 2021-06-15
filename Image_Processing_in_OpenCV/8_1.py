import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread(r'/Users/hongjin-u/git_project/OpenCV/messi5.jpg')

lower_reso1 = cv.pyrDown(img)
lower_reso2 = cv.pyrDown(lower_reso1)
higher_reso1 = cv.pyrUp(img)
higher_reso2 = cv.pyrUp(lower_reso1)

cv.imshow("img", img)
cv.imshow("lower_reso1", lower_reso1) 
cv.imshow("lower_reso2", lower_reso2) 
cv.imshow("higher_reso1",higher_reso1)
cv.imshow("higher_reso2",higher_reso2)
cv.waitKey(0)
cv.destroyAllWindows()
