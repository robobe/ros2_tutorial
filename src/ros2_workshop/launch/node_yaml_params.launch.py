import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    config = os.path.join(
        get_package_share_directory('ros2_workshop'),
        'config',
        'params.yaml'
        )
        
    node=Node(
        package = 'ros2_workshop',
        name = 'node_with_yaml_params',
        executable = 'yaml_node',
        parameters = [config]
    )

    ld.add_action(node)
    return ld