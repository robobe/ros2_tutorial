import rclpy
from rclpy.node import Node

class MyNode(Node):
    def __init__(self):
        super().__init__('MyNode')
        self.get_logger().info("hello node")

        self.declare_parameter('demo_param', False)

        demo_param = self.get_parameter('demo_param')
        self.get_logger().info(f"param value: {demo_param.value}")

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__ == '__main__':
    main()