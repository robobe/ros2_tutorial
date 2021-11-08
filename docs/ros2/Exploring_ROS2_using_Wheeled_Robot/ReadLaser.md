# Read Laser

- Run gazebo
```
gazebo --verbose -s libgazebo_ros_factory.so
```
- Spawn entity

```hl_lines="3"
xacro <full_path>/m2wr_description/urdf/m2wr.xacro | ros2 run gazebo_ros spawn_entity.py \
-entity cart \
-stdin
```

## Check topic
```
ros2 topic info /m2wr/scan --verbose
Type: sensor_msgs/msg/LaserScan

Publisher count: 1

Node name: gazebo_ros_head_hokuyo_controller
Node namespace: /m2wr
Topic type: sensor_msgs/msg/LaserScan
Endpoint type: PUBLISHER
GID: 01.0f.e3.ae.e3.55.02.00.01.00.00.00.00.00.4d.03.00.00.00.00.00.00.00.00
QoS profile:
  Reliability: RMW_QOS_POLICY_RELIABILITY_RELIABLE
  Durability: RMW_QOS_POLICY_DURABILITY_VOLATILE
  Lifespan: 2147483651294967295 nanoseconds
  Deadline: 2147483651294967295 nanoseconds
  Liveliness: RMW_QOS_POLICY_LIVELINESS_AUTOMATIC
  Liveliness lease duration: 2147483651294967295 nanoseconds

Subscription count: 0


```