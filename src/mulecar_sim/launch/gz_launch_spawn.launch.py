import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch import logging

log = logging.get_logger(__name__)

def generate_launch_description():
    urdf_file_name = 'urdf/basic.urdf'

    urdf = os.path.join(
        get_package_share_directory('mulecar_description'),
        urdf_file_name)

    log.warning(urdf)

    return LaunchDescription([
        ExecuteProcess(
                cmd=[
                    "gazebo",
                    "-s",
                    "libgazebo_ros_init.so",
                    "-s",
                    "libgazebo_ros_factory.so"
                ],
                output="screen"
            ),
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            name='urdf_spawner',
            output='screen',
            arguments=["-file", urdf, "-entity", "my"])
    ])
