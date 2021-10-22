#include <functional>
#include <gazebo/gazebo.hh>
#include <rclcpp/rclcpp.hpp>
#include <std_msgs/msg/string.hpp>
#include <gazebo/physics/physics.hh>
#include <gazebo/common/common.hh>
#include <ignition/math/Vector3.hh>

#ifndef ROS_SIMPLE_PLUGIN_HPP_
#define ROS_SIMPLE_PLUGIN_HPP_


namespace gazebo
{
    class ROSSimple : public ModelPlugin
    {
    public:
        void Load(physics::ModelPtr _parent, sdf::ElementPtr _sdf);
        void OnUpdate();
        void cmd_cb(std_msgs::msg::String::SharedPtr msg);
        // Pointer to the model
    private:
        
        rclcpp::Subscription<std_msgs::msg::String>::SharedPtr cmd_sub_;
        rclcpp::Node::SharedPtr ros_node_;
        gazebo::physics::ModelPtr model;
        gazebo::event::ConnectionPtr updateConnection;
    };
}
#endif