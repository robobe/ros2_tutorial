import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist, Point
from nav_msgs.msg import Odometry
import math
import tf_transformations

RAD2DEG = 57.2957795130823209

class MinimalSubscriber(Node):
    def __init__(self):
        super().__init__('go_to_point')
        self.get_logger().info("start ---2--------------------")
        self.pub_twist = self.create_publisher(Twist, '/m2wr/cmd_vel', 1)
        self.subscription = self.create_subscription(
            Odometry,
            '/m2wr/odom',
            self.clbk_odom,
            10)
        self.subscription  # prevent unused variable warning
        self.speed = Twist()
        self.goal = Point()
        self.goal.x = 5.0
        self.goal.y = 5.0
        self.goal.z = 0.0
        self.theta = 0.0
        self.timer = self.create_timer(1.0/10, self.__simple_goto)
        

    def clbk_odom(self, msg):
        # position
        self.position_ = msg.pose.pose.position
        # self.get_logger().info('I heard: "%s"' % self.position_)
        # yaw
        quaternion = (
            msg.pose.pose.orientation.x,
            msg.pose.pose.orientation.y,
            msg.pose.pose.orientation.z,
            msg.pose.pose.orientation.w)
        euler = tf_transformations.euler_from_quaternion(quaternion)
        self.theta = euler[2]
        
        # self.__state_machine()

    def __simple_goto(self):
        inc_x = self.goal.x - self.position_.x
        inc_y = self.goal.y - self.position_.y

        angle_to_goal = math.atan2(inc_y, inc_x)
        err_angle = angle_to_goal - self.theta
        err_pos = math.sqrt(pow(self.goal.y - self.position_.y, 2) + pow(self.goal.x - self.position_.x, 2))
        self.get_logger().info("theta: {} ,angle to goal: {}".format(self.theta * RAD2DEG,err_angle))

        if abs(err_angle) > 0.1:
            self.speed.linear.x = 0.0
            self.speed.angular.z = 0.3
        elif err_pos > 0.1:
            self.speed.linear.x = 0.5
            self.speed.angular.z = 0.0
        else:
            self.speed.linear.x = 0.0
            self.speed.angular.z = 0.0
        self.pub_twist.publish(self.speed)

def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber = MinimalSubscriber()
    rclpy.spin(minimal_subscriber)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()