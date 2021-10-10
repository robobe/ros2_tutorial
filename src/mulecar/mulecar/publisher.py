import rclpy

def main(args=None):
    rclpy.init(args=args)
    node = rclpy.create_node("py_pub")
    node.get_logger().info("py pub simple")
    
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()