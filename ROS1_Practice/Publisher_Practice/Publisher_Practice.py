#Allows use of ROS functionalities such as interactions with topics
import rospy

#Imports the class twist which is the class used to command the turtle in the turtle sim node.
from geometry_msgs.msg import Twist

if __name__ == '__main__':
    #names and initialises the node
    rospy.init_node("draw_circle")
    #Outputs "Node has been started." to the console
    rospy.loginfo("Node has been started.") 
    
    # establishes pub as the Publiser rospy method, and outline the topic, class and queue size
    pub = rospy.Publisher("/turtle1/cmd_vel",Twist, queue_size = 10)
    
    # establishes the rate of 2 hertz and assigns it to variable rate
    rate = rospy.Rate(2)

    #Creates a while loop that is active while this node is running
    while not rospy.is_shutdown():
       
        # assigns Twist class to "msg"
        msg = Twist()
        #Uses twist methods to set the desired linear and angular velocity of the turtle
        msg.linear.x = 2.0
        msg.angular.z = 1.0
        # uses the publish method to send the msg twist class to the /turtle1/cmd_vel topic.
        pub.publish(msg)
        #pauses the loop for 2Hz
        rate.sleep
