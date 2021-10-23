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

package_name = "camera_calibration"
def generate_launch_description():
    sdf_file_name = 'perspective.sdf'
    sdf = os.path.join(
        get_package_share_directory(package_name),
        "sdf",
        sdf_file_name)
    # 

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
            name='spawner',
            output='screen',
            arguments=['-file', sdf, "-entity", "my_camera"])
    ])
