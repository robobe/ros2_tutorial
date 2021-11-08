#!/usr/bin/env python3

"""
ros2 run m2wr_motion spawn_box box1 ns1
"""

import rclpy
import os
import argparse
from rclpy.node import Node
from ament_index_python.packages import get_package_share_directory
from gazebo_msgs.srv import SpawnEntity

class SpawnBoxNode(Node):
    def __init__(self, args):
        super().__init__('spawn_box')
        self.args = args
        self.spawn_client = self.create_client(SpawnEntity, "/spawn_entity")
        self.run()

    def run(self):
        sdf_file_path = os.path.join(
        get_package_share_directory("m2wr_description"), "models",
        "box", "box.sdf")
        request = SpawnEntity.Request()
        request.name = str(self.args.name)
        request.xml = open(sdf_file_path, 'r').read()
        request.robot_namespace = self.args.ns
        request.initial_pose.position.x = float(self.args.x)
        request.initial_pose.position.y = float(self.args.y)
        request.initial_pose.position.z = float(self.args.z)
        
        future = self.spawn_client.call_async(request)
        rclpy.spin_until_future_complete(self, future)
        if future.result() is not None:
            self.get_logger().info('response: %r' % future.result())
        else:
            raise RuntimeError('exception while calling service: %r' % future.exception())


def main():
    rclpy.init()
    parser = argparse.ArgumentParser(description = "command args description")
    parser.add_argument("-n", "--name", help="name", default="my_box")
    parser.add_argument("-s", "--ns", help="namespace", default="")
    parser.add_argument("-x", type=float, help = "x pose", default=0)
    parser.add_argument("-y", type=float, help = "y pose", default=0)
    parser.add_argument("-z", type=float, help = "z pose", default=0)
 
    # Read arguments from command line
    args = parser.parse_args()
    
    my_node = SpawnBoxNode(args)
    rclpy.spin_once(my_node)
    my_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()