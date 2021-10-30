# https://roboticsbackend.com/ros2-yaml-params/
import rclpy
from rclpy.node import Node

class TestYAMLParams(Node):

    def __init__(self):
        super().__init__('node_with_yaml_params')
        self.declare_parameters(
            namespace='',
            parameters=[
                ('bool_value', None),
                ('int_number', None),
                ('float_number', None),
                ('str_text', None),
                ('bool_array', None),
                ('int_array', None),
                ('float_array', None),
                ('str_array', None),
                ('bytes_array', None),
                ('nested_param.another_int', None)
            ])
        demo_param = self.get_parameter('int_number')
        self.get_logger().info(f"param value: {demo_param.value}")
        demo_param = self.get_parameter('str_array')
        self.get_logger().info(f"param value: {demo_param.value}")

def main(args=None):
    rclpy.init(args=args)
    node = TestYAMLParams()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()