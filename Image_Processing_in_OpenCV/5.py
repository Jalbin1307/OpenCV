import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread(r'/Users/hongjin-u/git_project/OpenCV/j.png',0)
kernel = np.ones((5,5),np.uint8)
erosion = cv.erode(img,kernel,iterations = 1)
dilation = cv.dilate(img,kernel, iterations =1)
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)
blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)


plt.subplot(331), plt.imshow(img), plt.title('Orignal')
plt.xticks([]), plt.yticks([])

plt.subplot(332), plt.imshow(erosion), plt.title('erosion')
plt.xticks([]),plt.yticks([])

plt.subplot(333), plt.imshow(dilation), plt.title('dilation')
plt.xticks([]),plt.yticks([])

plt.subplot(334), plt.imshow(opening), plt.title('dilation')
plt.xticks([]),plt.yticks([])

plt.subplot(335), plt.imshow(gradient), plt.title('gradient')
plt.xticks([]),plt.yticks([])

plt.subplot(336), plt.imshow(tophat), plt.title('tophat')
plt.xticks([]),plt.yticks([])

plt.subplot(337), plt.imshow(blackhat), plt.title('blackhat')
plt.xticks([]),plt.yticks([])

plt.show()