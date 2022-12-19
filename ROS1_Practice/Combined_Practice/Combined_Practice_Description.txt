This is the code I used to understand how to write a node that involves both a Subscribers and Publishers in a closed loop. It also implements a service from the turtlesim node.
The purpose of this node is to automate the movement of the turtle in the turtlesim node and to make it turn when it approaches a wall. 
It does this by using a subscriber to get the position of the turtle and when it crosses a boundry that is undesired.
Then the publisher will publish the change of angular and linear velocity of the turtle until it is out of danger from reaching the edge.
The service is used to change the colour of the pen when the turtle crosses a boundry.
