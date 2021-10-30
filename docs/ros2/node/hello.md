# Hello ROS2 Node
## Objective
- Write minimal ROS2 python Node
- Build and run
- Usage, run the same node multiple times


### Node

```python
--8<-- "src/camera_calibration/camera_calibration/mini_node.py"
```

### setup.py
- Add console entry point
```python hl_lines="25 28" linenums="1"
--8<-- "src/camera_calibration/setup.py"
```

### package.xml
- Add dependency
```xml  linenums="1" hl_lines="15"
--8<-- "src/camera_calibration/package.xml"

```

## Usage node
- Build
- Source
- Run

```bash linenums="1" hl_lines="9 12"
#build
colcon build --packages-select camera_calibration --symlink-install

# Source
source install/setup.bash

# Run
ros2 run camera_calibration mini
[INFO] [1635226536.082675453] [my_node_name]: hello node
# Run same node with different name
ros2 run camera_calibration mini --ros-args -r __node:=other_node
[INFO] [1635226555.757267071] [other_node]: hello node
```