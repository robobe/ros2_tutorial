# Node
## Node with parameters

```python
--8<-- "src/ros2_workshop/ros2_workshop/param_node.py"
```

### build and run
```bash
# build
colcon build --packages-select ros2_workshop
# run
ros2 run ros2_workshop pnode
# run with params
ros2 run ros2_workshop pnode --ros-args -p demo_param:=True
```

### Nodes params
- list
```bash
ros2 param list
# Result
/MyNode:
  simulation_mode
  use_sim_time
```

- get
```bash
# ros2 param get <Node> <param name>
ros2 param get /MyNode demo_param
# Result
Boolean value is: False
```

## Launch file
- Run node with parameters from launch file


```python
--8<-- "src/ros2_workshop/launch/node_with_params.launch.py"
```

!!! note

    Add line to setup.py `data_files` array  
    ```
    data_files=[
    (os.path.join('share', package_name), glob('launch/*.launch.py'))
    ```


### build and run
```bash
# build
colcon build --packages-select ros2_workshop
# launch
ros2 launch ros2_workshop node_with_params.launch.py
```

## Launch file with argument
```python
--8<-- "src/ros2_workshop/launch/node_params_args.launch.py"
```

#### Check 
- Show launch file arguments

```bash
ros2 launch ros2_workshop node_params_args.launch.py -s
#result
Arguments (pass arguments as '<name>:=<value>'):

    'demo_param':
        no description given
        (default: 'True')

```

#### launch
```
ros2 launch ros2_workshop node_params_args.launch.py demo_param:=False
```


### node YAML params
- load node parameters from YAML file
- 
&nbsp;  
&nbsp;  
&nbsp;  
## References
- [rclpy Params Tutorial](https://roboticsbackend.com/rclpy-params-tutorial-get-set-ros2-params-with-python/)