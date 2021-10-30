import rclpy
from rclpy.node import Node
class MyNode(Node):
    def __init__(self):
        super().__init__('my_node_name')
        self.get_logger().info("hello node")
        self.declare_parameter('simulation_mode', False)

        sim_mode = self.get_parameter('simulation_mode')
        self.get_logger().info(f"param value: {sim_mode.value}")

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__ == '__main__':
    main()