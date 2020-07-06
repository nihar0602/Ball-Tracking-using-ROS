# Ball-Tracking-using-ROS


  <b> Personal Project </b>
</p>

<img src="results.gif" alt="result" width="1024" height="500"> <br>

### Ball Tracking using ROS and OpenCV:
<img src="include/bar.jpg" alt="bar.jpg" width="1100" height="3"> <br>

**Problem:** 
`Ball Tracking` :The goal of this project was to write a an alogrithm for ball detection and tracking using Robotic Operating System(ROS) and OpenCV library.

Initially, the project was offered in one of the online MOOC course offered by Prof.Anis Koubaa.

**Approach:**
* The camera output is converted into HSV format.
* Color Filtering is done. 
* Edge detection using Color Filtering. 
* Once Edge detected, draw contour around it. 
* Process the contour like calculating the area,perimeter of the contour. 
* `Disadvantage:` It is not robust to lighting condition because of color filtering.

## How to run: 
<img src="include/bar.jpg" alt="bar.jpg" width="1100" height="3"> <br>

* Download all the files in one folder and name in `topic03_opencv`
* Copy and paste the folder in your catkin workspace. (e.g `..\catkin_ws\src\`)
* Once completed, go into catkin workspace. (`..\catkin_ws\`)
* Open the terminal in the current directory(`..\catkin_ws\`) and compile the file using:
> catkin_ws
* Once done, open another terminal and run `roscore`
* To run the USB_CAM, run: 
> rosrun usb_cam usb_cam_node _pixel_format:= yuyv
* Then run the `tennis_ball_usb_cam_tracker.py` file
* To run:
> rosrun topic03_opencv tennis_ball_usb_cam_tracker.py


## Requirements:
<img src="include/bar.jpg" alt="bar.jpg" width="1100" height="3"> <br>
 * ROS MELODIC.
 * UBUNTU 18.04 LTS.
 * OPENCV 3.4.2 or later version.
 * USB_CAM ROS PACKAGE.


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

