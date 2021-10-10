import rclpy
import time
from rclpy.node import Node

from tutorial_interfaces.msg import ImageFixed

# int32 width
# int32 height
# int32 seq
# uint64 time
# uint8[2097152] data

class MinimalPublisher(Node):
    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(ImageFixed, 'my_topic', 10)
        timer_period = 1/10  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.count_ = 0
        self.msg = ImageFixed()

    def timer_callback(self):
        self.msg.width = 128
        self.msg.height = 64
        self.msg.seq = self.count_
        self.msg.time = (int)(time.time() * 1000000)
        self.publisher_.publish(self.msg)
        self.get_logger().info('Publishing: (%d %d %d) ' % (self.msg.width, self.msg.height, self.msg.seq))
        self.count_ += 1

def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)
    minimal_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()