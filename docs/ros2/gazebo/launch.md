# ROS2 Gazebo simple demo
- Create package for simulation
- Create package for project plugins
- 
- Launch gazebo world that include
  - project model
  - project plugin

```bash
# simulation package
ros2 pkg create --build-type ament_cmake mulecar_sim

#plugins package
ros2 pkg create --build-type ament_cmake mulecar_plugins
```

```
├── launch
├── models
├── worlds
├── CMakeLists.txt
└── package.xml
```