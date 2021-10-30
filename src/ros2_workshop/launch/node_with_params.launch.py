from launch import LaunchDescription
from launch_ros.actions import Node
def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ros2_workshop',
            executable='pnode',
            parameters=[
                {'demo_param': True}
            ],
            output='screen',
        )
    ])