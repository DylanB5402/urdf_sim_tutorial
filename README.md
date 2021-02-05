# urdf_sim_tutorial
See the tutorials over at http://wiki.ros.org/urdf_tutorial

Modified Version of the above ROS tutorial

Working on a controllable mecanum model which can be extended for future Triton Robotics projects, currently contains the differential drive model provided in the tutorial.

Note to self: add execuatable with 

chmod +x file.py

if gazebo doesn't run or doesn't open the urdf model, or the urdf model shows up bad in rosviz but works with display.launch

killall gzclient
killall gzserver

bixi urdf from https://github.com/ron1818/Project_Bixi
