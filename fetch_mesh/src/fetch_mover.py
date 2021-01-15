#!/usr/bin/env python
import sys, rospy, actionlib
from control_msgs.msg import PointHeadAction, PointHeadGoal
import time

# stuff to add:
# add in something to recognize that the head controller has finished the joint trajectory
# before starting up the point_head
# Should only have to point the head once to focus on the goal target point, since it is relative to base_link
# What happens if base_link is changed to "map"
if __name__ == '__main__':
    time.sleep(20)
    rospy.loginfo("Pointing the camera towards the cubes...")
    rospy.init_node('look_at_cubes')
    head_client = actionlib.SimpleActionClient("head_controller/point_head",
                                               PointHeadAction)
    while not rospy.is_shutdown():
        head_client.wait_for_server()
        goal = PointHeadGoal()
        goal.target.header.stamp = rospy.Time.now()
        goal.target.header.frame_id = "base_link"
        goal.target.point.x = 0
        goal.target.point.y = 2
        goal.target.point.z = 0
        goal.min_duration = rospy.Duration(1)
        head_client.send_goal(goal)
        head_client.wait_for_result()