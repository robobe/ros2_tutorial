---
title: URDF and XACRO
tags:
 - urdf
 - xacro
 - launch
---
# URDF and XACRO
- Using URDF 
- Launch nodel from cli
- Launch gazebo and spawn model


## Prerequisite
```
sudo apt install ros-foxy-urdf
sudo apt install ros-foxy-xacro
```

### Create pkg
```
ros2 pkg create --build-type ament_cmake mulecar_description
```

### Launch and Spawn
#### cli
- launch gazebo
```
ros2 launch gazebo_ros gazebo.launch.py
```

- spawn model
```
ros2 run gazebo_ros spawn_entity.py -entity my_robot1 -file <>/basic.urdf
```

- entity: model name  
- file: file location  

&nbsp;  
&nbsp;  
&nbsp;  
### URDF minimal
```xml
---8<--- "src/mulecar_description/urdf/basic.urdf"
```

### inertial
[online calculator](https://amesweb.info/inertia/mass-moment-of-inertia-cylinder.aspx)

![](inertia_online_cal.png)

&nbsp;  
&nbsp;  
## Launch and Spawn
using ROS2 launch file to launch gazebo and spawn model

- launch file 

```python linenums="1" hl_lines="25 27 36"
---8<--- "src/mulecar_sim/launch/gz_launch_spawn.launch.py"
```

1.  :libgazebo_ros_init:
2.  :libgazebo_ros_factory:
3.  :spawn robot from file:

&nbsp;  
&nbsp;  
&nbsp;  
# XACRO
```
sudo apt install ros-foxy-xacro
```

## macro file
- inertia macro file
```xml
---8<--- "src/mulecar_description/urdf/macros.xacro"
```

## xacro file
```xml  linenums="1" hl_lines="3 8"
---8<--- "src/mulecar_description/urdf/basic.urdf.xacro"
```

### cli usage
`xacro` installed as a part of `ros-foxy-xacro` package
```
xacro basic.urdf.xacro
```

### launch
```python linenums="1" hl_lines="20-22 35-39"
---8<--- "src/mulecar_sim/launch/gz_launch_xacro.launch.py"
```

