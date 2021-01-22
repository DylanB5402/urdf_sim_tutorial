#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64
import math

# type of setpoint is either angle (rad) or angular velocity (rad/s) as specified by the controller type in head.yaml
def go_to_setpoint(setpoint):
    setpoint_publisher = rospy.Publisher("/turret_controller/command", Float64, queue_size=10)
    rospy.init_node('head_setpoint', anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        rospy.loginfo(setpoint)
        setpoint_publisher.publish(setpoint)
        rate.sleep()


if __name__ == '__main__':
    try:
        go_to_setpoint(0.7)
    except rospy.ROSInterruptException:
        pass