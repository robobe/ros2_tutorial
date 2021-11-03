import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist, Point
from nav_msgs.msg import Odometry
import math
import tf_transformations

class MinimalSubscriber(Node):
    def __init__(self):
        super().__init__('go_to_point')
        self.pub_twist = self.create_publisher(Twist, '/m2wr/cmd_vel', 1)
        self.subscription = self.create_subscription(
            Odometry,
            '/m2wr/odom',
            self.clbk_odom,
            10)
        self.subscription  # prevent unused variable warning
        self.timer = self.create_timer(1.0, self.__state_machine)
        self.desired_position_ = Point()
        self.desired_position_.x = -3.0
        self.desired_position_.y = 7.0
        self.desired_position_.z = 0.0
        self.yaw_precision_ = math.pi / 90 # +/- 2 degree allowed
        self.dist_precision_ = 0.3
        self.yaw_ = 0
        self.state_ = 0
        

    def clbk_odom(self, msg):
        # position
        self.position_ = msg.pose.pose.position
        self.get_logger().info('I heard: "%s"' % self.position_)
        # yaw
        quaternion = (
            msg.pose.pose.orientation.x,
            msg.pose.pose.orientation.y,
            msg.pose.pose.orientation.z,
            msg.pose.pose.orientation.w)
        euler = tf_transformations.euler_from_quaternion(quaternion)
        self.yaw_ = euler[2]
        self.get_logger().info(self.yaw_)

    def fix_yaw(self, des_pos):
        desired_yaw = math.atan2(
            des_pos.y - self.position_.y, 
            des_pos.x - self.position_.x)
        err_yaw = desired_yaw - self.yaw_
        
        twist_msg = Twist()
        if math.fabs(err_yaw) > self.yaw_precision_:
            twist_msg.angular.z = 0.7 if err_yaw > 0 else -0.7
        
        
        self.pub_twist.publish(twist_msg)
        
        # state change conditions
        if math.fabs(err_yaw) <= self.yaw_precision_:
            self.get_logger().info(('Yaw error: [%s]' % err_yaw))
            self.change_state(1)

    def change_state(self, state):
        self.state_ = state
        print ('State changed to [%s]' % self.state_)

    def go_straight_ahead(self, des_pos):
        desired_yaw = math.atan2(des_pos.y - self.position_.y, des_pos.x - self.position_.x)
        err_yaw = desired_yaw - self.yaw_
        err_pos = math.sqrt(pow(des_pos.y - self.position_.y, 2) + pow(des_pos.x - self.position_.x, 2))
        
        if err_pos > self.dist_precision_:
            twist_msg = Twist()
            twist_msg.linear.x = 0.6
            self.pub_twist.publish(twist_msg)
        else:
            print ('Position error: [%s]' % err_pos)
            self.change_state(2)
        
        # state change conditions
        if math.fabs(err_yaw) > self.yaw_precision_:
            print ('Yaw error: [%s]' % err_yaw)
            self.change_state(0)

    def done(self):
        twist_msg = Twist()
        twist_msg.linear.x = 0
        twist_msg.angular.z = 0
        self.pub_twist.publish(twist_msg)

    def __state_machine(self):
        while rclpy.ok:
            if self.state_ == 0:
                self.fix_yaw(self.desired_position_)
            elif self.state_ == 1:
                self.go_straight_ahead(self.desired_position_)
            elif self.state_ == 2:
                self.done()
                pass
            else:
                self.get_logger().error('Unknown state!')
                pass


def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber = MinimalSubscriber()
    rclpy.spin(minimal_subscriber)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()