import rclpy
from rclpy.node import Node
def main(args=None):
    rclpy.init(args=args)
    node = Node('my_node_name')
    node.get_logger().info("hello node")
    rclpy.spin(node)
    rclpy.shutdown()
if __name__ == '__main__':
    main()