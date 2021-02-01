#!/usr/bin/env python

import rospy
from rospy import Publisher, Rate 
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64MultiArray

class MecanumDrive():

    def __init__(self):
        

if __name__ == '__main__':
    try:
        mecanum_drive()
    except rospy.ROSInterruptException:
        pass