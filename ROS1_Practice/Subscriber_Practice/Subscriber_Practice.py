#Allows use of ROS functionalities such as interactions with topics
import rospy

#Imports the Pose class. This class is imported becasue it is the class that turtlesim publishes that holds the information of the position of the turtle
from turtlesim.msg import Pose

#This function is needed for the subscriber method. it is used to handle the data collected from the secscriber
def pose_callback(msg):
    rospy.loginfo(msg)

    
if __name__ == '__main__':
    #names and initialises the node
    rospy.init_node("turtle_pose_subscriber")
    #This is the subscriber method in rospy. it takes the topic that is publishing the data, The type of the data and the function that handles the data. It then assigns it to sub.
    sub = rospy.Subscriber("/turtle1/pose", Pose, callback = pose_callback)
    
    #Outputs "Node has been started" to the console
    rospy.loginfo("Node has been started")
    
    #spin is a rospy method that prevents the node from exiting until the node is shutdown
    rospy.spin()
