# Image transport test
LAB Objective:
    - publish image 640*480 30fps
    - Check cpu usage, memory and latency

LAB HW
- ubuntu 20.04
- ROS foxy
- HW: i5 8G RAM


## image_tools
Using image_tool package [github](https://github.com/ros2/demos)

### install
```
sudo apt install ros-fox-image-tools
```

### Demo
- Run publisher with generated image
- Run with to QoS profiles:
  + Reliable
  - best_effort


#### publisher

fps: 30 (default)

```bash
ros2 run image_tools cam2image \
--ros-args -p burger_mode:=True \
-p width:=640 \
-p height:=480 \
-p reliability:=best_effort
```

#### subscriber

```
ros2 run image_tools showimage \
 --ros-args \
 -p show_image:=False \
 -p reliability:=best_effort
```
#### Results
|           | cpu | latency |             notes             |
| :-------: | :-: | :-----: | :---------------------------: |
| cam2image | 4.6 |         |    640\*480 30fps reliable    |
| showimage | 3.3 |         |       show_image:=False       |
| cam2image | ~4  |         |  640\*480 30fps best_effort   |
| showimage | ~3  |         | show_image:=False best_effort |

## custom subscriber
- Create python custom subscriber
- Check topic info, for QoS

```bash  linenums="1" hl_lines="13-14"
ros2 topic info /image --verbose
#
Type: sensor_msgs/msg/Image

Publisher count: 1

Node name: cam2image
Node namespace: /
Topic type: sensor_msgs/msg/Image
Endpoint type: PUBLISHER
GID: 01.0f.e3.ae.04.6d.d2.3d.01.00.00.00.00.00.12.03.00.00.00.00.00.00.00.00
QoS profile:
  Reliability: RMW_QOS_POLICY_RELIABILITY_BEST_EFFORT
  Durability: RMW_QOS_POLICY_DURABILITY_VOLATILE

```

!!! Reliable
    ```python
    self.subscription = self.create_subscription(
        Image,
        '/image',
        self.listener_callback,
        10)
    ```


!!! best_effort
    ```python
    qos = QoSProfile(
            depth=10,
            reliability=QoSReliabilityPolicy.BEST_EFFORT,
            durability=QoSDurabilityPolicy.VOLATILE)
    self.subscription = self.create_subscription(
        Image, 
        '/image', 
        self.listener_callback, 
        qos)
    ```

### Result
|           | cpu | latency |                 notes                  |
| :-------: | :-: | :-----: | :------------------------------------: |
| cam2image | 4.6 |         |        640\*480 30fps reliable         |
|  img_sub  | 15  |         |                                        |
| cam2image | ~4  |         |       640\*480 30fps best_effort       |
| img_sub | 15  |         |  best_effort,VOLATILE |


### subscriber
- python source code

```python linenums="1" hl_lines="31 21-24"
---8<-- "src/ros2_workshop/ros2_workshop/image/simple_image_sub.py"
```