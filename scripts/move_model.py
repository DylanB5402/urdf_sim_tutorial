#!/usr/bin/env python

from rospy import Publisher
import rospy
from gazebo_msgs.msg import ModelState
from geometry_msgs.msg import Pose, Twist

def set_pose(x, y, angular_z):
    state_publisher = Publisher("/gazebo/set_model_state", ModelState, queue_size=10)
    rospy.init_node("model_state_setter", anonymous = True)
    new_pose = Pose()
    new_pose.position.x = x
    new_pose.position.y = y
    new_pose.orientation.z = angular_z
    new_state = ModelState()
    new_state.pose = new_pose
    new_state.model_name = "robot"
    new_state.reference_frame = "ground_plane"
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        rospy.loginfo(new_state)
        state_publisher.publish(new_state)
        rate.sleep()

def set_velocity(x, y):
    state_publisher = Publisher("/gazebo/set_model_state", ModelState, queue_size=10)
    rospy.init_node("model_state_setter", anonymous = True)
    new_vel = Twist()
    new_vel.linear.x = x
    new_vel.linear.y = y
    new_state = ModelState()
    new_state.twist = new_vel
    new_state.model_name = "robot"
    new_state.reference_frame = "ground_plane"
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        rospy.loginfo(new_state)
        state_publisher.publish(new_state)
        rate.sleep()

if __name__ == '__main__':
    try:
        set_velocity(1, 0)
    except rospy.ROSInterruptException:
        pass
