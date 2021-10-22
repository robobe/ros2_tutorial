#ifndef GAZEBO_PLUGINS__GAZEBO_ROS_SIMPLE_HPP_
#define GAZEBO_PLUGINS__GAZEBO_ROS_SIMPLE_HPP_

#include <gazebo/common/Plugin.hh>
#include <std_msgs/msg/string.hpp>

namespace gazebo_plugins
{
  class GazeboRosSimplePrivate;

  class GazeboRosSimple : public gazebo::ModelPlugin
  {
  public:
    GazeboRosSimple();
    virtual ~GazeboRosSimple();

  protected:
    void Load(gazebo::physics::ModelPtr model, sdf::ElementPtr sdf) override;
    virtual void OnUpdate();

  private:
    void OnRosStringMsg(const std_msgs::msg::String::ConstSharedPtr msg);
    std::unique_ptr<GazeboRosSimplePrivate> impl_;
  };
} // namespace gazebo_plugins

#endif
