cmake_minimum_required(VERSION 3.0.2)
project(urdf_sim_tutorial)

find_package(catkin REQUIRED COMPONENTS 
 rospy
  geometry_msgs)

catkin_package()
add_executable(drive scripts/drive.py)

catkin_python_setup()




install(DIRECTORY config launch urdf
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
  
catkin_install_python(PROGRAMS scripts/drive.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)