# ROS2 Gazebo 

Run gazebo with ros2 functionality

### gazebo_ros_factory
```
gazebo --verbose -s libgazebo_ros_factory.so
```

```bash
ros2 service list
#
/delete_entity
/gazebo/describe_parameters
/gazebo/get_parameter_types
/gazebo/get_parameters
/gazebo/list_parameters
/gazebo/set_parameters
/gazebo/set_parameters_atomically
/get_model_list
/spawn_entity
```

### gazebo_ros_init
```
gazebo --verbose -s libgazebo_ros_init.so
```

```bash
ros2 service list
#
/pause_physics
/reset_simulation
/reset_world
/spawn_entity
/unpause_physics
```

### gazebo_ros_properties

```xml
--8<-- "src/ros2_workshop/worlds/empty.world"
```

```
/get_joint_properties
/get_light_properties
/get_link_properties
/get_model_properties
/properties/describe_parameters
/properties/get_parameter_types
/properties/get_parameters
/properties/list_parameters
/properties/set_parameters
/properties/set_parameters_atomically
/set_joint_properties
/set_light_properties
/set_link_properties
```

