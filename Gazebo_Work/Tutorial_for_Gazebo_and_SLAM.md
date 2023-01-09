For this I used Ubuntu 18.04 on a Rasberry Pi 4, Gazebo was running on ROS noetic. This will use the burger model of the turtlebot 3

This tutorial will cover the installation of ROS, Gazebo and SLAM. Next I will ocver the dependencies and packages. Finally I will go through the set up, mapping and the use of SLAM.

The first step is to install ROS noetic, refer to this guide to install it. http://wiki.ros.org/noetic/Installation/Ubuntu
This installation comes with gazebo and SLAM installed.

The dependencies required are turtlebot3 and turtlebot3_msgs. These should already be installed when ROS is installed

Next type this into the terminal. This clones the turtlebot directory and also creates a catkin_ws in ROS

```
$ cd ~/catkin_ws/src/
$ git clone -b kinetic-devel https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
$ cd ~/catkin_ws && catkin_make
```

in the terminal type this to change the model of the turtlebot

```
export TURTLEBOT3_MODEL=burger
```

A permanent solution is to type this into the console
```source .bashrc
```
in this file type or alter
"export TURTLEBOT3_MODEL = burger"

this sets the model being used

There are 3 command to open gazebo with the turtlebot 3. Each command opens a different world.

```
$ roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch
$ roslaunch turtlebot3_gazebo turtlebot3_world.launch
$ roslaunch turtlebot3_gazebo turtlebot3_house.launch
```

This command greatly increases performance

```
$ gz physics  -s 0.015
```

to begin mapping open the simulated world and in a new console type 

```
roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=gmapping
```

in a new console type, this opens a terminal that lets you move the robot using the keyboard

```
$ roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
```

once you move the robot so that the map is complete in rVIZ save the map using this command

```
$ rosrun map_saver map_saver -f ~/map
```

Finally to open slam so that you can send the turtlebot 3 to a specific point on the map, use this command.

```
$roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/map.yaml
```

from there press the 2D Pose estimate button at the top and drag on the turtlebot 3 which way it is facing, next press the 2D Nav Goal butoon and press and drag where you want the turtlebot to go.




