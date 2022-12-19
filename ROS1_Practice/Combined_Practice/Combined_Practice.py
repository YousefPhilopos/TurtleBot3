#Allows use of ROS functionalities such as interactions with topics
import rospy
#Imports the Pose class. This class is imported becasue it is the class that turtlesim publishes that holds the information of the position of the turtle
from turtlesim.msg import Pose
#Imports the class twist which is the class used to command the turtle in the turtle sim node.
from geometry_msgs.msg import Twist
#Imports the ROS service that enables a change in color and width of the turtlesim node pen
from turtlesim.srv import SetPen

#Creates the variable "previous_x" that will be used later 
previous_x = 0

#Creates a function that will be used to handle the Pen service. It takes the RBG value, width and of the pen is on or off.
def call_set_pen_service(r, g, b, width, off):
    #Creats a try and except that will take errors in the service calls and print them to the console as warnings
    try:
        #Creates a variable that gets assigned a rospy method ehich calls the service. It is provided the topic and the class that is being called
        set_pen = rospy.ServiceProxy ("/turtle1/set_pen", SetPen)
        #calls the service by assigning it to a variable.
        response = set_pen(r, g, b, width, off)
    except rospy.ServiceServiceException as e:
        rospy.logwarn(e)

#This is the function that handles the information collected by the subscriber method.
def pose_callback(pose: Pose):
    cmd = Twist()
    #If the turtle is outisde of the set boundries it will begin to turn, otherwise it will contintue striaght. This is so taht it doesnt stop at a wall.
    if pose.x > 9.0 or pose.x < 2.0 or pose.y > 9.0 or pose.y < 2.0:
        cmd.linear.x = 1.0
        cmd.angular.z = 1.4
    else:
        cmd.linear.x = 5.0
        cmd.angular.z = 0.0
    #Publish the change in linear and angular velocity
    pub.publish(cmd)
    
    global previous_x
    #If the turtles position crosses the boundry it will turn red or green depending on which side it is on. 
    if pose.x >= 5.5 and previous_x < 5.5:
        rospy.loginfo("Set color to red")
        call_set_pen_service(255, 0, 0, 3, 0)
    elif pose.x < 5.5 and previous_x >= 5.5:
        rospy.loginfo("Set color to green")
        call_set_pen_service(0, 255, 0, 3, 0)
    previous_x = pose.x

if __name__ == '__main__':
    #names and initialises the node
    rospy.init_node("turtle_controller")
    #This method waits for a service to be called before proceeding
    rospy.wait_for_service("/turtle1/set_pen")
    # establishes pub as the Publiser rospy method, and outline the topic, class and queue size
    pub = rospy.Publisher("/turtle1/cmd_vel",Twist, queue_size = 10)
    #This is the subscriber method in rospy. it takes the topic that is publishing the data, The type of the data and the function that handles the data. It then assigns it to sub.
    sub = rospy.Subscriber("/turtle1/pose", Pose, callback = pose_callback)
    #Outputs "Node has been started" to the console
    rospy.loginfo("Node has been started")
    
    #spin is a rospy method that prevents the node from exiting until the node is shutdown
    rospy.spin()
