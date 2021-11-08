# Spawn entity

## Run gazebo
```
gazebo --verbose -s libgazebo_ros_factory.so
```

```bash
ros2 service list -t
#
/delete_entity [gazebo_msgs/srv/DeleteEntity]
/gazebo/describe_parameters [rcl_interfaces/srv/DescribeParameters]
/gazebo/get_parameter_types [rcl_interfaces/srv/GetParameterTypes]
/gazebo/get_parameters [rcl_interfaces/srv/GetParameters]
/gazebo/list_parameters [rcl_interfaces/srv/ListParameters]
/gazebo/set_parameters [rcl_interfaces/srv/SetParameters]
/gazebo/set_parameters_atomically [rcl_interfaces/srv/SetParametersAtomically]
/get_model_list [gazebo_msgs/srv/GetModelList]
/spawn_entity [gazebo_msgs/srv/SpawnEntity]
```
&nbsp;  
&nbsp;  
## Spawn
Spawn box into world using:  
- spawn_entity.py Node  
- using service call `/spawn_entity`, `/delete_entity`  
- using custom node wrap `spawn_entity` service  
    + aaa


### spawn_entity.py
```
ros2 run gazebo_ros spawn_entity.py -entity myentity -x 1 -y 1 -z 0 -file /home/user/ros2_tutorial/src/m2wr_description/models/box/box.sdf
```

### service call
- Check msg structure
  
```bash
ros2 interface show gazebo_msgs/srv/DeleteEntity 
#
string name                       # Name of the Gazebo entity to be deleted. This can be either
                                  # a model or a light.
---
bool success                      # Return true if deletion is successful.
string status_message             # Comments if available.

```

- Call Service
  
```
ros2 service call /delete_entity 'gazebo_msgs/DeleteEntity' '{name: "myentity"}'
```

!!! Note
    Space between key value in message is mandatory


&nbsp;  
&nbsp;  
### custom node
- Create node that spawn entity

```python
--8<-- "src/m2wr_motion/m2wr_motion/spawn_box.py"
```
&nbsp;  
&nbsp;  
&nbsp;  
## Reference
- [Spawn and delete](https://github.com/ros-simulation/gazebo_ros_pkgs/wiki/ROS-2-Migration:-Spawn-and-delete)
- [Make a model](http://gazebosim.org/tutorials?tut=build_model)