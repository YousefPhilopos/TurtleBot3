#!/usr/bin/env python3

import rospy
#Allows use of ROS functionalities such as interactions with topics

from geometry_msgs.msg import Twist
#Imports the class twist which is the class used to command the turtle in the turtle sim node.

if __name__ == '__main__':
    rospy.init_node("draw_circle")
    #names and initialises the node
    rospy.loginfo("Node has been started.")
    #Outputs "Node has been started." to the console

    pub = rospy.Publisher("/turtle1/cmd_vel",Twist, queue_size = 10)
    # establishes pub as the Publiser rospy method, and outline the topic, class and queue size

    rate = rospy.Rate(2)
    # establishes the rate of 2 hertz and assigns it to variable rate

    while not rospy.is_shutdown():
        #Creates a while loop that is active while this node is running
        
        msg = Twist()
        # assigns Twist class to "msg"
        msg.linear.x = 2.0
        msg.angular.z = 1.0
        #Uses twist methods to set the desired linear and angular velocity of the turtle
        pub.publish(msg)
        # uses the publish method to send the msg twist class to the /turtle1/cmd_vel topic.
        rate.sleep
        #pauses the loop for 2Hz
        
