from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    demo_param = LaunchConfiguration('demo_param')
    demo_param_cmd = DeclareLaunchArgument(
        name='demo_param', 
        default_value="True")
    simple_node_cmd = Node(
            package='ros2_workshop',
            executable='pnode',
            parameters=[
                {'demo_param': demo_param}
            ],
            output='screen',
        )
    ld = LaunchDescription()
    ld.add_action(demo_param_cmd)
    ld.add_action(simple_node_cmd)

    return ld