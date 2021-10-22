#include <gazebo_ros_simple.hpp>
#include <gazebo_ros/node.hpp>
#include <std_msgs/msg/string.hpp>
#include <rclcpp/rclcpp.hpp>
#include <string>

const std::string TOPIC = "gazebo_ros_simple";
namespace gazebo_plugins
{
class GazeboRosSimplePrivate
{
public:
  /// A pointer to the GazeboROS node.
  gazebo_ros::Node::SharedPtr ros_node_;
  // Pointer to subscriber
  rclcpp::Subscription<std_msgs::msg::String>::SharedPtr string_sub_;
  // Pointer to the update event connection
  gazebo::event::ConnectionPtr update_connection_;
};

GazeboRosSimple::GazeboRosSimple()
: impl_(std::make_unique<GazeboRosSimplePrivate>())
{
}

GazeboRosSimple::~GazeboRosSimple()
{
}

void GazeboRosSimple::Load(gazebo::physics::ModelPtr model, sdf::ElementPtr sdf)
{
  impl_->ros_node_ = gazebo_ros::Node::Get(sdf);
  // Get QoS profiles
  const gazebo_ros::QoS & qos = impl_->ros_node_->get_qos();
  impl_->string_sub_ = impl_->ros_node_->create_subscription<std_msgs::msg::String>(
    TOPIC, qos.get_subscription_qos("gazebo_ros_simple", rclcpp::SystemDefaultsQoS()),
    std::bind(&GazeboRosSimple::OnRosStringMsg, this, std::placeholders::_1));

  // Callback on every iteration
  impl_->update_connection_ = gazebo::event::Events::ConnectWorldUpdateBegin(
    std::bind(&GazeboRosSimple::OnUpdate, this));
}

void GazeboRosSimple::OnRosStringMsg(const std_msgs::msg::String::ConstSharedPtr msg)
{
  gzmsg << "OnRosStringMsg" << std::endl;
  RCLCPP_INFO(
      impl_->ros_node_->get_logger(), msg->data);
}

void GazeboRosSimple::OnUpdate()
{

}

GZ_REGISTER_MODEL_PLUGIN(GazeboRosSimple)
}  // namespace gazebo_plugins
