#!/usr/bin/env python

import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import sys
from ball_detection import * 
bridge = CvBridge()

def image_callback(ros_image):
  print 'got an image'
  global bridge
  #convert ros_image into an opencv-compatible image
  try:
    cv_image = bridge.imgmsg_to_cv2(ros_image, "bgr8")
  except CvBridgeError as e:
      print(e)


  cv2.imshow("Image window", cv_image)
  yellowLower =(30, 150, 100)
  yellowUpper = (50, 255, 255)
  rgb_image = cv_image
  binary_image_mask = filter_color(rgb_image, yellowLower, yellowUpper)
  contours = getContours(binary_image_mask)
  draw_ball_contour(binary_image_mask, rgb_image,contours)
  cv2.waitKey(5)
  
def main(args):
  rospy.init_node('image_converter', anonymous=True)
  #for turtlebot3 waffle
  #image_topic="/camera/rgb/image_raw/compressed"
  #for usb cam
  #image_topic="/usb_cam/image_raw"
  image_sub = rospy.Subscriber("/usb_cam/image_raw",Image, image_callback)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)