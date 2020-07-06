#!/usr/bin/env python

import cv2
import numpy as np 
import time 
import rospy 
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

bridge = CvBridge()


def main():
    global bridge

    pub = rospy.Publisher("tennis_ball_image", Image, queue_size=1)
    rospy.init_node('tennis_image_ball',anonymous=True)
    
    # video_capture = cv2.VideoCapture(0)
    video_capture = cv2.VideoCapture('/home/nihar/catkin_ws/src/topic03_opencv/src/video/tennis-ball-video.mp4')
    # ret,frame = video_capture.read()

    # if ret:
    #     rospy.loginfo("Captruing Image Failed")


    rate = rospy.Rate(24)  

    while (True):
        ret,frame = video_capture.read()

        # print frame
        # cv2.imshow("Frame", frame)
        ros_image = bridge.cv2_to_imgmsg(frame, encoding="bgr8")

        try:
            pub.publish(ros_image)
            rospy.loginfo("Publishing IMG")
        except CvBridgeError as e:
            print(e)
        rate.sleep()
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break

    # cv2.waitKey(2)
    # cv2.destroyAllWindows()
    

if __name__ == "__main__":
    main()
