import numpy as np
import cv2 as cv

img = cv.imread(r'C:\Users\USER\OpenCV\OpenCV\Core_Operations\starry_night.jpg')

px = img[100,100]
print(px)

blue = img[100,100,0] # B G R
print(blue)

img[100,100] = [255,255,255]
print(img[100,100])

print(img.item(10,10,2))

img.itemset((10,10,2),100)
img.item(10,10,2)

print( img.shape )

print(img.size)

print(img.dtype)

ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

cv.imshow("img",img)
cv.waitKey(0)

