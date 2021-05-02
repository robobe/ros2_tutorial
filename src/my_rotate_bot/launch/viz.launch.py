import os

from ament_index_python.packages import get_package_share_directory


from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node

import xacro

PACKAGE_NAME = "my_rotate_bot"

def generate_launch_description():
    # robot state publisher
    my_rotate_bot_path = os.path.join(
        get_package_share_directory(PACKAGE_NAME))

    urdf_file = os.path.join(my_rotate_bot_path,
                              'urdf',
                              'model.urdf')

    doc = xacro.parse(open(urdf_file))
    xacro.process_doc(doc)
    robot_description = {'robot_description': doc.toxml()}
    
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[robot_description]
    )

    node_joint_state_publisher = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        output='screen',
        parameters=[robot_description]
    )

    rviz_config_dir = os.path.join(get_package_share_directory(PACKAGE_NAME), 
        'config',
        'rviz.config.rviz')
    # ,
    rviz = Node(
            package='rviz2',
            node_executable='rviz2',
            node_name='rviz2',
            output='screen',
            arguments=['-d', rviz_config_dir])

    return LaunchDescription([
        # missing:
        rviz,
        node_joint_state_publisher,
        # 2. joint-state-publisher-gui
        node_robot_state_publisher,
    ])
