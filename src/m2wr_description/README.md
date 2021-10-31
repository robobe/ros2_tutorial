# M2WR_DESCRIPTION

```
ros2 pkg create --build-type ament_cmake m2wr_descriptionco
```

## apt
```
sudo apt install ros-foxy-joint-state-publisher-gui
sudo apt install ros-foxy-xacro
```

## project structure
```
├── CMakeLists.txt
├── config
├── launch
├── package.xml
├── README.md
└── urdf
    └── m2wr.xacro
```

### tools
#### colcon-cd
A shell function for colcon-core to change current working directory

To enable colcon_cd source `/usr/share/colcon_cd/function`

```
echo "source /usr/share/colcon_cd/function/colcon_cd.sh" >> ~/.bashrc
```

### build
```bash
# from ws root folder
colcon build --packages-select m2wr_description
```

### Part3
[source](https://www.theconstructsim.com/exploring-ros-2-wheeled-robot-part-03-urdf-laser-scan/)


### Other reference
- [two_wheeled_robot_ROS_tutorial ](https://github.com/sulibo/two_wheeled_robot_ROS_tutorial)
- [ROS1 to ROS2 migration](https://github.com/ros-simulation/gazebo_ros_pkgs/wiki)
- [other project to explore](https://bitbucket.org/theconstructcore/box_car/src/foxy/)