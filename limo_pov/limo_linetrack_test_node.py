#!/usr/bin/env python
import rospy, numpy
from sensor_msgs.msg import *
#import matplotlib.pyplot as plt
import cv2
from cv_bridge import *
from geometry_msgs.msg import Twist

img =cv2.imread('road.jpg')

print(img.shape)

h, w, d = img.shape
search_top = 3*h/4
search_bot = 3*h/4 + 30
search_left = 3*w/21
search_right = 3*w/21 + 185
img[0:search_top, 0:w] = 0
img[search_bot:h, 0:w] = 0

img[0:h, 0:search_left] = 0
img[0:h, search_right:w] = 0

cv2.imshow("output", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
