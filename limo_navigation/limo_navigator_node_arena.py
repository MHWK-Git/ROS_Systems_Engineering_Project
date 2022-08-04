#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

def waypoint_z1():

   # Create an action client called "move_base" with action definition file "MoveBaseAction"
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
 
   # Waits until the action server has started up and started listening for goals.
    client.wait_for_server()

    goalz1 = MoveBaseGoal()
    goalz1.target_pose.header.frame_id = "map"
    goalz1.target_pose.header.stamp = rospy.Time.now()
    goalz1.target_pose.pose.orientation.z = 0.0
    goalz1.target_pose.pose.orientation.w = 1.0
    #rospy.sleep(2)
    goalz1.target_pose.pose.position.x = 0.52
    goalz1.target_pose.pose.position.y = -1.634
    #rospy.sleep(2)
    client.send_goal(goalz1)
    wait = client.wait_for_result()
    rospy.sleep(1)

def waypoint1():
    # Create an action client called "move_base" with action definition file "MoveBaseAction"
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
 
   # Waits until the action server has started up and started listening for goals.
    client.wait_for_server()
    goal1 = MoveBaseGoal()
    goal1.target_pose.header.frame_id = "map"
    goal1.target_pose.header.stamp = rospy.Time.now()
    goal1.target_pose.pose.orientation.z = 0.31
    goal1.target_pose.pose.orientation.w = 0.95
    goal1.target_pose.pose.position.x = 1.26
    goal1.target_pose.pose.position.y = -1.634
    client.send_goal(goal1)
    wait = client.wait_for_result()

def waypoint_z2_mid1():
    # Create an action client called "move_base" with action definition file "MoveBaseAction"
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
 
   # Waits until the action server has started up and started listening for goals.
    client.wait_for_server()
    goalz2m1 = MoveBaseGoal()
    goalz2m1.target_pose.header.frame_id = "map"
    goalz2m1.target_pose.header.stamp = rospy.Time.now()
    goalz2m1.target_pose.pose.orientation.z = -0.96
    goalz2m1.target_pose.pose.orientation.w = 0.28
    goalz2m1.target_pose.pose.position.x = -0.681
    goalz2m1.target_pose.pose.position.y = -1.81
    client.send_goal(goalz2m1)
    wait = client.wait_for_result()

def waypoint_z2_mid2():
    # Create an action client called "move_base" with action definition file "MoveBaseAction"
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
 
   # Waits until the action server has started up and started listening for goals.
    client.wait_for_server()
    goalz2m2 = MoveBaseGoal()
    goalz2m2.target_pose.header.frame_id = "map"
    goalz2m2.target_pose.header.stamp = rospy.Time.now()
    goalz2m2.target_pose.pose.orientation.z = 1.0
    goalz2m2.target_pose.pose.orientation.w = 0.0
    goalz2m2.target_pose.pose.position.x = -1.13
    goalz2m2.target_pose.pose.position.y = -1.81
    client.send_goal(goalz2m2)
    wait = client.wait_for_result()

def waypoint_z2():
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()
    goalz2 = MoveBaseGoal()
    goalz2.target_pose.header.frame_id = "map"
    goalz2.target_pose.pose.orientation.z = -0.7
    goalz2.target_pose.pose.orientation.w = -0.7
    goalz2.target_pose.pose.position.x = -1.66
    goalz2.target_pose.pose.position.y = -1.65
    rospy.sleep(2)

    client.send_goal(goalz2)
    wait = client.wait_for_result()

def waypoint_z2_mid2():
    # Create an action client called "move_base" with action definition file "MoveBaseAction"
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
 
   # Waits until the action server has started up and started listening for goals.
    client.wait_for_server()
    goalz2m2 = MoveBaseGoal()
    goalz2m2.target_pose.header.frame_id = "map"
    goalz2m2.target_pose.header.stamp = rospy.Time.now()
    goalz2m2.target_pose.pose.orientation.z = -0.91
    goalz2m2.target_pose.pose.orientation.w = -0.42
    goalz2m2.target_pose.pose.position.x = -1.64
    goalz2m2.target_pose.pose.position.y = 0.05
    client.send_goal(goalz2m2)
    wait = client.wait_for_result()

def waypoint2():
    # Create an action client called "move_base" with action definition file "MoveBaseAction"
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
 
   # Waits until the action server has started up and started listening for goals.
    client.wait_for_server()
    goal2 = MoveBaseGoal()
    goal2.target_pose.header.frame_id = "map"
    goal2.target_pose.header.stamp = rospy.Time.now()
    goal2.target_pose.pose.orientation.z = -0.70
    goal2.target_pose.pose.orientation.w = 0.70
    goal2.target_pose.pose.position.x = -1.81
    goal2.target_pose.pose.position.y = 1.71
    client.send_goal(goal2)
    wait = client.wait_for_result()

def waypoint_z3():
    # Create an action client called "move_base" with action definition file "MoveBaseAction"
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
 
   # Waits until the action server has started up and started listening for goals.
    client.wait_for_server()
    goalz3 = MoveBaseGoal()
    goalz3.target_pose.header.frame_id = "map"
    goalz3.target_pose.header.stamp = rospy.Time.now()
    goalz3.target_pose.pose.orientation.z = -0.7
    goalz3.target_pose.pose.orientation.w = 0.7
    goalz3.target_pose.pose.position.x = -1.64
    goalz3.target_pose.pose.position.y = 0.05
    client.send_goal(goalz3)
    wait = client.wait_for_result()

def waypoint3():
    # Create an action client called "move_base" with action definition file "MoveBaseAction"
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
 
   # Waits until the action server has started up and started listening for goals.
    client.wait_for_server()
    goal3 = MoveBaseGoal()
    goal3.target_pose.header.frame_id = "map"
    goal3.target_pose.header.stamp = rospy.Time.now()
    goal3.target_pose.pose.orientation.z = 0.0
    goal3.target_pose.pose.orientation.w = 1
    goal3.target_pose.pose.position.x = -1.66
    goal3.target_pose.pose.position.y = -1.65
    client.send_goal(goal3)
    wait = client.wait_for_result()

def waypoint_z4():
    # Create an action client called "move_base" with action definition file "MoveBaseAction"
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
 
   # Waits until the action server has started up and started listening for goals.
    client.wait_for_server()
    goalZ4 = MoveBaseGoal()
    goalZ4.target_pose.header.frame_id = "map"
    goalZ4.target_pose.header.stamp = rospy.Time.now()
    goalZ4.target_pose.pose.orientation.z = 1.0
    goalZ4.target_pose.pose.orientation.w = 0.0
    goalZ4.target_pose.pose.position.x = 0.0
    goalZ4.target_pose.pose.position.y = 0.0
    client.send_goal(goalZ4)
    wait = client.wait_for_result()
   
def waypoint4():
    # Create an action client called "move_base" with action definition file "MoveBaseAction"
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
 
   # Waits until the action server has started up and started listening for goals.
    client.wait_for_server()
    goal4 = MoveBaseGoal()
    goal4.target_pose.header.frame_id = "map"
    goal4.target_pose.header.stamp = rospy.Time.now()
    goal4.target_pose.pose.orientation.z = -0.7
    goal4.target_pose.pose.orientation.w = -0.7
    goal4.target_pose.pose.position.x = 1.96
    goal4.target_pose.pose.position.y = -0.06
    client.send_goal(goal4)
    wait = client.wait_for_result()

def almost_there():
    # Create an action client called "move_base" with action definition file "MoveBaseAction"
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
 
   # Waits until the action server has started up and started listening for goals.
    client.wait_for_server()
    goal4 = MoveBaseGoal()
    goal4.target_pose.header.frame_id = "map"
    goal4.target_pose.header.stamp = rospy.Time.now()
    goal4.target_pose.pose.orientation.z = -0.7
    goal4.target_pose.pose.orientation.w = -0.7
    goal4.target_pose.pose.position.x = 1.93
    goal4.target_pose.pose.position.y = 1.03
    client.send_goal(goal4)
    wait = client.wait_for_result()

def final_point():
    # Create an action client called "move_base" with action definition file "MoveBaseAction"
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
 
   # Waits until the action server has started up and started listening for goals.
    client.wait_for_server()
    goal4 = MoveBaseGoal()
    goal4.target_pose.header.frame_id = "map"
    goal4.target_pose.header.stamp = rospy.Time.now()
    goal4.target_pose.pose.orientation.z = -0.7
    goal4.target_pose.pose.orientation.w = -0.7
    goal4.target_pose.pose.position.x = 2.23
    goal4.target_pose.pose.position.y = 2.38
    client.send_goal(goal4)
    wait = client.wait_for_result()


   # If the result doesn't arrive, assume the Server is not available
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
    # Result of executing the action
        return client.get_result()  

if __name__ == '__main__':
    try:
       # Initializes a rospy node to let the SimpleActionClient publish and subscribe
        rospy.init_node('limo_navigator_node_arena')
        resultZ1 = waypoint_z1()
        result1 = waypoint1()
	result_mid1 = waypoint_z2_mid1()
        resultZ2 = waypoint_z2()
	#result_mid2 = waypoint_z2_mid2()
        result2 = waypoint2()
        resultZ3 = waypoint_z3()
        result3 = waypoint3()
        resultZ4 = waypoint_z4()
        result4 = waypoint4()
	result_al = almost_there()
	result_end = final_point()
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")
