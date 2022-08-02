#!/usr/bin/env python
from cv2 import GaussianBlur
import rospy, numpy
from sensor_msgs.msg import *

import cv2
from cv_bridge import *
from geometry_msgs.msg import Twist

class Seeker:     

 def __init__(self):
  self.bridge = CvBridge()
  self.image_sub = rospy.Subscriber('/camera/rgb/image_raw', Image, self.callback)
  self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
  self.Twist = Twist()
  
 def callback(self, mes):
  cv_image = self.bridge.imgmsg_to_cv2(mes, desired_encoding='bgr8')
  hsv = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
  #white
  low = numpy.array([ 0, 0, 250])
  high = numpy.array([ 180, 20, 255])
  #yellow
  #low = numpy.array([ 15, 100, 0])
  #high = numpy.array([ 36, 255, 255])
  #low = numpy.array([ 0, 0, 0])
  #high = numpy.array([ 179, 255, 255])

  mask = cv2.inRange(hsv, low, high)

  h, w, d = cv_image.shape
  search_top = 238
  search_bot = 3*h/4 + 100
  search_left = 187
  search_right = 640 - (search_left * 2) + search_left
  mask[0:search_top, 0:w] = 0
  mask[search_bot:h, 0:w] = 0
  mask[0:h, 0:search_left] = 0
  mask[0:h, search_right:w] = 0

  M = cv2.moments(mask)
  target = cv2.bitwise_and(cv_image, cv_image, mask = mask)
  cx = 128
  cy = 128
  if M['m00'] != 0:
   cx = int(M['m10']/M['m00'])
   cy = int(M['m01']/M['m00'])
  
   err = cx - w/2
   self.Twist.linear.x = 0.1
   self.Twist.angular.z = -float(err) / 590
   #self.Twist.linear.x = 0.00
   #self.Twist.angular.z = 0.00
   self.cmd_vel_pub.publish(self.Twist)

  cv2.imshow("view",cv_image)
  cv2.imshow("output",target)
  cv2.waitKey(3)

while not rospy.is_shutdown():
 rospy.init_node('limo_pov_node', anonymous= False)
 limo_pov_node = Seeker()
 rospy.spin()
