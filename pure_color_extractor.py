#!/usr/bin/env python

import cv2

image = cv2.imread('colour_test_img.png')

#define colour boundaries

#Red
m1 = cv2.inRange(image, (0, 0, 50), (50, 50, 255))

#Blue
m2 = cv2.inRange(image, (50, 0, 0), (255, 50, 50))

#Green
m3 = cv2.inRange(image, (0, 50, 0), (50, 255, 50))

#Cyan
m4 = cv2.inRange(image, (50, 50, 0), (255, 255, 50))

#Yellow
m5 = cv2.inRange(image, (0, 50, 50), (50, 255, 255))

#Magenta
m6 = cv2.inRange(image, (50, 0, 50), (255, 50, 255))


mask = cv2.bitwise_or(m1, m1)
target1 = cv2.bitwise_and(image, image, mask = mask)

mask = cv2.bitwise_or(m2, m2)
target2 = cv2.bitwise_and(image, image, mask = mask)

mask = cv2.bitwise_or(m3, m3)
target3 = cv2.bitwise_and(image, image, mask = mask)

mask = cv2.bitwise_or(m4, m4)
target4 = cv2.bitwise_and(image, image, mask = mask)

mask = cv2.bitwise_or(m5, m5)
target5 = cv2.bitwise_and(image, image, mask = mask)

mask = cv2.bitwise_or(m6, m6)
target6 = cv2.bitwise_and(image, image, mask = mask)

cv2.imshow('Image',image)
cv2.imshow('Red', target1)
cv2.imshow('Blue', target2)
cv2.imshow('Green', target3)
cv2.imshow('Cyan', target4)
cv2.imshow('Yellow', target5)
cv2.imshow('Magenta', target6)
cv2.waitKey(0)
cv2.destroyAllWindows()

