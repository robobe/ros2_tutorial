# ROS2

- create ws
```
source /opt/ros/foxy/setup.bash
mkdir src
cd src
```
- Create a python package
```
# under src folder run
ros2 pkg create --build-type ament_python my_rotate_bot
# build

```
- build
```bash
# from ws root folder
colcon build
```
- source the new package
```bash
# from ws folder
. install/setup.bash
```

## urdf and launch
- Create `model.urdf` file under `urdf` folder
- Create `robot_state_publisher.launch.py` launch file under `launch` folder


## setup
- Add all `data files` like urdf and launch file to `data_files` list for deploy at build

```python
data_files=[
        ('share/' + package_name, glob('launch/*.launch.py')),
        ('share/' + package_name + '/urdf', glob('urdf/*.urdf'))
    ],
```


## pkg dependencies
- add `<exec_depend>` to package.xml

```xml
<exec_depend>xacro</exec_depend>
```

- install pkg dependencies
- from ws root folder
  
```bash
rosdep install --from-paths src --ignore-src -r -y
```

## build
```bash
# build all workspace packages
colcon build

# build signal package excluding dependencies
colcon build --package-select my_rotate_bot

#
colcon build --symlink-install
```

if you do colcon build --symlink-install, then instead of a copy of the launch file it will put a symbolic link to the launchfile. This means that if you change something to the launch file in your package you don't have to rebuild the package for the changes to take effect. This is only true for files that don require compilation, so --symlink-install will work for config files or python code / launch files etc.
## run

```bash
ros2 launch my_rotate_bot robot_state_publisher.launch.py
```

## tf
```
ros2 topic list
# 
/joint_states
/parameter_events
/robot_description
/rosout
/tf
/tf_static

```

### joint_state_publisher
install from apt-get or package package.xml
```
sudo apt install ros-foxy-joint-state-publisher
```

or add to package.xml and run rosdep

```
<exec_depend>joint_state_publisher</exec_depend>
```

```
rosdep install -i --from-path src --rosdistro foxy -y
```

#### run
```
ros2 run joint_state_publisher joint_state_publisher ./src/my_rotate_bot/urdf/model.urdf
```

## robot_state_publisher vs joint_state_publisher

### robot_state_publisher
[robot_state_publisher](http://wiki.ros.org/robot_state_publisher)  
robot_state_publisher uses the `URDF` specified by the parameter `robot_description` and the joint positions from the topic `joint_states` to calculate the forward kinematics of the robot and publish the results via `tf`.

> Without `joint_state_publisher` only /tf_static are publish

### joint_state_publisher
[join_state_publisher wiki](http://wiki.ros.org/joint_state_publisher)
This package publishes `sensor_msgs/JointState` messages for a robot. The package reads the robot_description parameter from the `parameter server`, finds all of the **non-fixed** joints and publishes a JointState message with all those joints defined. 

This package can be used in conjunction with the `robot_state_publisher` node to also publish **transforms** for all joint states. 
