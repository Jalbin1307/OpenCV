import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread(r'/Users/hongjin-u/git_project/OpenCV/opencv-logo-white.png')

blur = cv.blur(img, (5,5))
# blur = cv.GaussianBlur(img, (5,5), 0)
# median = cv.medianBlur(img, 5)
# blur = cv.bilateralFilter(img, 9, 75, 75)
plt.subplot(121), plt.imshow(img), plt.title('Orignal')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(blur), plt.title('Blurred')
plt.xticks([]),plt.yticks([])
plt.show()

