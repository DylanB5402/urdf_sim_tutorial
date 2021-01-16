# urdf_sim_tutorial
See the tutorials over at http://wiki.ros.org/urdf_tutorial

Modified Version of the above ROS tutorial

Working on a controllable mecanum model which can be extended for future Triton Robotics projects, currently contains the differential drive model provided in the tutorial.

Note to self: add execuatable with 

chmod +x file.py

What I've done so far:
- figure out how to work with the model robot in the example (r2d2)
    - python scripts to drive the robot and move its head
- make joints in urdf file and move those joints with python scripts 
- move around URDF models in gazebo through ROS nodes

What I can do/am doing right now:
- writing a mecanum drive model using kinematics and stuff 
- get that model to respond to inputs and move accordingly in gazebo
    - this model would only move around, physics wouldn't be very realistic and i'm not sure how useful it would be 
    - model wouldn't properly interact with the simulated world
        - if the model drove into a wall, it would just keep going forward through it 
- summary:
    - this approach takes an input velocity to all wheels of the robot, calculates the position/angle of the robot based off of that, and tells the gazebo model of the robot to go to that pose

What I need/could use going forward
- a proper URDF model 
    - mecanum wheel with the proper joints on the casters so they function properly in sim
    - this will let gazebo handle the physics properly
    - summary:
        - this approach takes an input velocity to all wheels of the robot and applies that velocity to the wheels of the robot model in Gazebo. Gazebo handles the physics and makes sure the robot moves realistically 
    - not sure if other teams have good urdfs of their robots, need to look into making urdfs of our own robots too (solidworks to URDF plug-in exists iirc)
