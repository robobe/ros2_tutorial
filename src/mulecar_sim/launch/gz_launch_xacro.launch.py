import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch import logging
from launch.substitutions import Command
import xacro

log = logging.get_logger(__name__)


def generate_launch_description():
    xacro_file_name = 'urdf/basic.urdf.xacro'

    xacro_file = os.path.join(
        get_package_share_directory('mulecar_description'),
        xacro_file_name)
    doc = xacro.parse(open(xacro_file))
    xacro.process_doc(doc)
    params = {'robot_description': doc.toxml()}

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
            package='robot_state_publisher',
            executable='robot_state_publisher',
            output='screen',
            parameters=[params]
        ),

        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            name='urdf_spawner',
            output='screen',
            arguments=['-topic', 'robot_description', "-entity", "my"])
    ])
