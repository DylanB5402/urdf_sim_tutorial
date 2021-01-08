#!/usr/bin/env python

import rospy
from rospy import Publisher, Rate 
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64MultiArray


def tank_drive(leftVel, rightVel):
    vel_publisher = Publisher("/r2d2_mecanum_drive_controller/command", Float64MultiArray, queue_size=10)
    rospy.init_node("drive_velocity_setpoint", anonymous=True)
    vel_array = Float64MultiArray()
    # left front, left_back, right_front right_back
    vel_array.data = [leftVel, -leftVel, -rightVel, rightVel]
    rate = Rate(10)
    while not rospy.is_shutdown():
        rospy.loginfo(vel_array)
        vel_publisher.publish(vel_array)
        rate.sleep()

if __name__ == '__main__':
    try:
        tank_drive(6, 6)
    except rospy.ROSInterruptException:
        pass
        