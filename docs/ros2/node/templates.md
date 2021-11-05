# ROS2 Node Templates

## Python basic
- Using timer to execute flow in specific intervals
- Using logger


```python
--8<-- "src/ros2_workshop/ros2_workshop/node_template_timer.py"
```

&nbsp;  
&nbsp;  
&nbsp;  
### Logger
[Logger level configuration](https://docs.ros.org/en/foxy/Tutorials/Logging-and-logger-configuration.html)
#### Console output formatting
```
export RCUTILS_CONSOLE_OUTPUT_FORMAT="[{severity} {time}] [{name}]: {message} "
```

- file_name: the full file name of the caller including the path
- function_name: the function name of the caller
- line_number: the line number of the caller
- message: the message string after it has been formatted
- name: the full logger name
- severity: the name of the severity level, e.g. INFO
- time: the timestamp of log message in floating point seconds

#### Console output colorizing
- [ros doc](https://docs.ros.org/en/foxy/Tutorials/Logging-and-logger-configuration.html)

```bash
# 1: colored
# 0: no color
export RCUTILS_COLORIZED_OUTPUT=0 
```

![](/img/2021-11-05-13-09-28.png)


#### Control log level
Run node with log level control


- debug (green)
- info  (white)
- warn  (yellow)
- error (red)

```
ros2 run ros2_workshop t_node --ros-args --log-level debug
```
![](/img/2021-11-05-13-20-02.png)

```
ros2 run ros2_workshop t_node --ros-args --log-level warn
```
![](/img/2021-11-05-13-15-30.png))

&nbsp;  
&nbsp;  
#### Log once
- Add `once` argument to log method

```python
self.get_logger().info('log once', once=True)
self.get_logger().error('log once', once=True)
```

![](/img/2021-11-05-13-28-50.png)

!!! note
    See the log once log lines


&nbsp;  
&nbsp;  
&nbsp;  
#### Log skip and throttle
- Control log output

```python
self.get_logger().info('skip first', skip_first=True)
self.get_logger().warn('skip and throttle', 
    throttle_duration_sec=2, 
    throttle_time_source_type=self.system_clock)
```

!!! Note
    declare `self.system_clock = Clock()` in class `__init__`  
    import `from rclpy.clock import Clock` 

![](/img/2021-11-05-14-09-54.png)