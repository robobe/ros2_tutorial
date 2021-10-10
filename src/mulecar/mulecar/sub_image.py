import rclpy
from rclpy.node import Node

from tutorial_interfaces.msg import ImageFixed
import time

class MinimalSubscriber(Node):
    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            ImageFixed,
            'my_topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
    def listener_callback(self, msg):
        now_us = (int)(time.time() * 1000000)
        latency = now_us - msg.time
        self.get_logger().info('I heard: (%d, %d, %d), size = %d, latency = %d us' % (msg.width, msg.height, msg.seq, len(msg.data), latency))


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()
    rclpy.spin(minimal_subscriber)

    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

# size = 2097152, latency = 444926 us


