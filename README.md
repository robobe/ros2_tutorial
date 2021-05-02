# ROS2



## urdf and launch


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




# Wiki
```
git submodule add https://github.com/robobe/ros2_tutorial.wiki.git wiki
git commit -m "Adding wiki"
git push
```