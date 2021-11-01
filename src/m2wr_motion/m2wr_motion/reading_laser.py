import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan

MAX_READING = 10

class ReadRay(Node):
    def __init__(self):
        super().__init__('read_laser')
        self.subscription = self.create_subscription(
            LaserScan,
            '/m2wr/scan',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg:LaserScan):
        # 720 / 5 = 144
        regions = [
            min(min(msg.ranges[0:143]),   MAX_READING),
            min(min(msg.ranges[144:287]), MAX_READING),
            min(min(msg.ranges[288:431]), MAX_READING),
            min(min(msg.ranges[432:575]), MAX_READING),
            min(min(msg.ranges[576:713]), MAX_READING),
        ]
        self.get_logger().info('I heard: "%s"' % regions)

def main(args=None):
    rclpy.init(args=args)
    node = ReadRay()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()