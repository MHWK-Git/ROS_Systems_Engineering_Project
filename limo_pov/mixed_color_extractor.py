#!/usr/bin/env python


import cv2
import numpy as np

#Read Image
image = cv2.imread('colour_venn_diagram.jpg')

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#define colour boundaries

#Green
mGreen = cv2.inRange(hsv, (40, 40, 40), (70, 255, 255))

#Red
mRed = cv2.inRange(hsv, (0, 100, 20), (10, 255, 255))

#Blue
mBlue = cv2.inRange(hsv, (100, 128, 128), (128, 255, 255))

#Cyan
mCyan = cv2.inRange(hsv, (85, 128, 0), (100, 255, 255))

#Yellow
mYellow = cv2.inRange(hsv, (15, 100, 0), (36, 255, 255))

#Magenta
mMagenta = cv2.inRange(hsv, (140, 160, 0), (170, 255, 255))


#Make a mask of that particular color and it's range
mask = cv2.bitwise_or(mGreen, mGreen)
target1 = cv2.bitwise_and(image, image, mask = mask)

mask = cv2.bitwise_or(mRed, mRed)
target2 = cv2.bitwise_and(image, image, mask = mask)

mask = cv2.bitwise_or(mBlue, mBlue)
target3 = cv2.bitwise_and(image, image, mask = mask)

mask = cv2.bitwise_or(mCyan, mCyan)
target4 = cv2.bitwise_and(image, image, mask = mask)

mask = cv2.bitwise_or(mYellow, mYellow)
target5 = cv2.bitwise_and(image, image, mask = mask)

mask = cv2.bitwise_or(mMagenta, mMagenta)
target6 = cv2.bitwise_and(image, image, mask = mask)

kernel = np.ones((7,7),np.uint8)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)


#Image Output
cv2.imshow('Image',image)
cv2.imshow('Green', target1)
cv2.imshow('Red', target2)
cv2.imshow('Blue', target3)
cv2.imshow('Cyan', target4)
cv2.imshow('Yellow', target5)
cv2.imshow('Magenta', target6)
cv2.waitKey(0)
cv2.destroyAllWindows()
