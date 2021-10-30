import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch import logging
from launch.substitutions import Command

log = logging.get_logger(__name__)

PACAKGE_NAME = "m2wr_description"

def generate_launch_description():
    pkg_share = get_package_share_directory(PACAKGE_NAME)
      
    log.info(pkg_share)
    # Set the path to the URDF file
    xacro_file = os.path.join(pkg_share, "urdf", "m2wr.xacro")



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
