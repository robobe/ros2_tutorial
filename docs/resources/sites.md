# Sites
- [[RoboCup][V-RoHOW] Hands-on with ROS 2](https://www.youtube.com/watch?v=ZgzsYvne5Gs)
- [ Gazebo model plugin for ROS2
](https://answers.ros.org/question/375249/gazebo-model-plugin-for-ros2/)


```
Without more info it is difficult to know where you're exactly stuck, but for me the trickiest was to get all the paths set up correctly so that everything was loaded correctly.

Note for instance the model path set in the package.xml file of the description package:

  <export>
    <build_type>ament_cmake</build_type>
    <gazebo_ros gazebo_model_path="${prefix}/.." />
  </export>

, which is then picked up in the launch file using GazeboRosPaths:

model_path, plugin_path, media_path = GazeboRosPaths.get_paths()

Most of the complexity is because ${prefix} in package.xml, get_package_share_directory in the launch file, and package:// in the URDF don't all point to the same directory under your installation, especially if you involve Rviz. See especially this commit to see some changes I had to make along the way to get it all to work:

https://gitlab.com/boldhearts/ros2_bo...

Hopefully this helps you in the right direction! Let us know of specific issues/error messages you're getting, so that I can then try to make this answer more specific.
```