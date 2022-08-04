#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

def waypoint_client1():

   # Create an action client called "move_base" with action definition file "MoveBaseAction"
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
 
   # Waits until the action server has started up and started listening for goals.
    client.wait_for_server()

    goal1 = MoveBaseGoal()
    goal1.target_pose.header.frame_id = "map"
    goal1.target_pose.header.stamp = rospy.Time.now()
   # Move 0.9 meters forward along the x axis of the "map" coordinate frame 
   # Move -0.1 meters forward along the y axis of the "map" coordinate frame 
    goal1.target_pose.pose.position.x = 0.9
    goal1.target_pose.pose.position.y = -0.1
   # LIMO faces front
    goal1.target_pose.pose.orientation.w = 1.0
     

    client.send_goal(goal1)
    wait = client.wait_for_result()
   
    rospy.sleep(1)

def waypoint_client2():
    
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()
    goal2 = MoveBaseGoal()
    goal2.target_pose.header.frame_id = 'map'
    # Move 0.7 meter(s) backwards along the x axis of the "map" coordinate frame from pose 1
    # Move 1 meter(s) upward along the y axis of the "map" coordinate frame from pose 1 
    goal2.target_pose.pose.position.x = 0.2
    goal2.target_pose.pose.position.y = 1.1
    # LIMO faces back
    goal2.target_pose.pose.orientation.z = -1.0
    goal2.target_pose.pose.orientation.w = 0.0

    client.send_goal(goal2)
    wait = client.wait_for_result()

    rospy.sleep(1)

def waypoint_client3():
    
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()
    goal3 = MoveBaseGoal()
    goal3.target_pose.header.frame_id = 'map'
    # Move 1.2 meters forward along the x axis of the "map" coordinate frame from pose 2
    # Move 0.0 meters along the y axis of the "map" coordinate frame from pose 2 
    goal3.target_pose.pose.position.x = 1.4
    goal3.target_pose.pose.position.y = 1.1
    # LIMO faces forward right
    goal3.target_pose.pose.orientation.z =-0.4
    goal3.target_pose.pose.orientation.w = 0.9

    client.send_goal(goal3)
    wait = client.wait_for_result()

    rospy.sleep(1)

def waypoint_client4():
    
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()
    goal4 = MoveBaseGoal()
    goal4.target_pose.header.frame_id = 'map' 
    # Move 0.4 meters forward along the x axis of the "map" coordinate frame from pose 3
    # Move 0.7 meters down along the y axis of the "map" coordinate frame from pose 3  
    goal4.target_pose.pose.position.x = 1.8
    goal4.target_pose.pose.position.y = 0.2
    # LIMO faces right
    goal4.target_pose.pose.orientation.z = -0.7
    goal4.target_pose.pose.orientation.w = 0.7

    client.send_goal(goal4)
    wait = client.wait_for_result()

    rospy.sleep(1)


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
        rospy.init_node('limo_navigator_node')
        result1 = waypoint_client1()
        result2 = waypoint_client2()
        result3 = waypoint_client3()
        result4 = waypoint_client4()
        if result1:
            rospy.loginfo("Waypoint 1 reached!")
        elif result2:
            rospy.loginfo("Waypoint 2 reached!")
        elif result3:
            rospy.loginfo("Waypoint 3 reached!")
        elif result4:
            rospy.loginfo("Waypoint 4 reached!")
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")
