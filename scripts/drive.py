#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

# linear: x is forward vel in m/s, angular: z is yaw in rad/s
def drive(linear_vel, angular_vel):
    velocity_publisher = rospy.Publisher('/r2d2_diff_drive_controller/cmd_vel', Twist, queue_size=10)
    rospy.init_node('drive', anonymous=True)
    velocity_msg = Twist()
    velocity_msg.linear.x = linear_vel
    velocity_msg.angular.z = angular_vel
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        rospy.loginfo(velocity_msg)
        velocity_publisher.publish(velocity_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        drive(0.4, 0)
    except rospy.ROSInterruptException:
        pass