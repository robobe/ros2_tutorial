#!/usr/bin/env python3

import rclpy
from rclpy.impl.rcutils_logger import SkipFirst
from rclpy.node import Node
from rclpy.clock import Clock

class Simple_Node(Node):
    def __init__(self):
        super().__init__('simple_node')
        # Create a timer that will gate the node actions twice a second
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.node_callback)
        self.system_clock = Clock()

    def node_callback(self):
        # self.get_logger().debug('simple_node is alive')
        # self.get_logger().info('simple_node is alive')
        # self.get_logger().warning('simple_node is alive')
        # self.get_logger().error('simple_node is alive')
        # self.get_logger().info('log once', once=True)
        self.get_logger().error('log once', once=True)
        self.get_logger().info('skip first', skip_first=True)
        self.get_logger().warn('throttle', 
            throttle_duration_sec=2, 
            throttle_time_source_type=self.system_clock)



def main(args=None):
    rclpy.init(args=args)
    my_node = Simple_Node()   # instantiate my simple_node
    rclpy.spin(my_node)       # execute simple_node 
    my_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
    