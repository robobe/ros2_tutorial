# ROS2 Gazebo Model plugin
- Create simple GAZEBO plugin as a ROS2 package
- Simple bind between ROS and gazebo

## ROS WS
```
ros_ws
├── install
│   ├── mulecar_sim
│   │    └── worlds
│   └── mulecar_plugins
│        └── lib
│              └── libgazebo_ros_simple.so (link to build folder)
├── build
├── log
└── src
   ├── mulecar_plugins
   │   ├── CMakeLists.txt
   │   ├── package.xml
   │   ├── src
   │   │   └── gazebo_ros_simple.cpp
   │   └── include
   │       └── gazebo_ros_simple.hpp
   └── mulecar_sim
        ├── CMakeLists.txt
        ├── package.xml
        ├── worlds
        │   └── gazebo_ros_simple.world
        └── launch
            └── gazebo_ros_simple.launch.py
```

### ROS2 pkg
```bash
sudo apt install ros-foxy-gazebo-ros

# cmake file to work with gazebo
sudo apt install ros-foxy-gazebo-dev
```

## mulecar_plugins
Simple plugin demonstration how to subscribe to topic and send string msg.  

pkg files
- Plugin header file
- Plugin cpp file
- CMakeLists.txt
- package.xml

### Header (gazebo_ros_simple.hpp)
```cpp
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

```

### CPP
```cpp
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

```

### CMakeLists.txt
```bash
cmake_minimum_required(VERSION 3.5)
project(mulecar_plugins)

set(CMAKE_CXX_STANDARD 14)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(gazebo_dev REQUIRED)
find_package(gazebo_ros REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

# gazebo_ros_simple
add_library(gazebo_ros_simple SHARED
  src/gazebo_ros_simple.cpp
)
target_include_directories(gazebo_ros_simple PUBLIC include)
ament_target_dependencies(gazebo_ros_simple
  "gazebo_dev"
  "gazebo_ros"
  "std_msgs"
  "rclcpp"
)

install(TARGETS
  gazebo_ros_simple
  ARCHIVE DESTINATION lib
  LIBRARY DESTINATION lib
  RUNTIME DESTINATION bin)



if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
```

### package.xml

```xml
<?xml version="1.0"?>
<?xml-model href="http://download.ros.org/schema/package_format3.xsd" schematypens="http://www.w3.org/2001/XMLSchema"?>
<package format="3">
  <name>mulecar_plugins</name>
  <version>0.0.1</version>
  <description>TODO: Package description</description>
  <maintainer email="robobe2020@gmail.com">user</maintainer>
  <license>TODO: License declaration</license>

  <buildtool_depend>ament_cmake</buildtool_depend>

  <depend>std_msgs</depend>

  <build_depend>gazebo_dev</build_depend>
  <build_depend>gazebo_ros</build_depend>
  <build_depend>rclcpp</build_depend>

  <exec_depend>gazebo_dev</exec_depend>
  <exec_depend>gazebo_ros</exec_depend>
  <exec_depend>rclcpp</exec_depend>

  <test_depend>ament_lint_auto</test_depend>
  <test_depend>ament_lint_common</test_depend>

  <export>
    <build_type>ament_cmake</build_type>
  </export>
</package>

```
&nbsp;  
&nbsp;  
## mulecar_sim
- World
- Launch

### world
```xml
<?xml version="1.0"?> 
<sdf version="1.4">
  <world name="default">

    <!-- Ground Plane -->
    <include>
      <uri>model://ground_plane</uri>
    </include>

    <include>
      <uri>model://sun</uri>
    </include>

    <model name="box">
      <pose>0 0 0.5 0 0 0</pose>
      <link name="link">
        <collision name="collision">
          <geometry>
            <box>
              <size>1 1 1</size>
            </box>
          </geometry>
        </collision>

        <visual name="visual">
          <geometry>
            <box>
              <size>1 1 1</size>
            </box>
          </geometry>
        </visual>
      </link>

      <plugin name="simple_plug" filename="libgazebo_ros_simple.so"/>
    </model>        
  </world>
</sdf>
```

&nbsp;  
&nbsp;  
## Test
- Run gazebo
- List Topics
- Pub and test

### Run gazebo

```bash
# from ws root folder
gazebo --verbose -s install/mulecar_plugins/lib/libgazebo_ros_simple.so src/mulecar_sim/worlds/plug_test.world
```

### List Topics
```bash
ros2 topic list
# Result
/clock
/gazebo_ros_simple
/parameter_events
/rosout
``` 

### Pub and Test
```bash
ros2 topic pub --once /gazebo_ros_simple std_msgs/msg/String "{data: 'hello gazebo'}"
# Result
publisher: beginning loop
publishing #1: std_msgs.msg.String(data='hello gazebo')
```

#### View gazebo verbose log
```
...
[Msg] OnRosStringMsg
[INFO] [1634791768.355582634] [simple_plug]: hello gazebo
```

## using launch file
```python
import os
from ament_index_python.packages import get_package_share_directory, get_package_prefix
from launch import LaunchDescription
from launch import logging
from launch.actions import ExecuteProcess

world_prefix = get_package_share_directory("mulecar_sim")
plugins = get_package_prefix("mulecar_plugins")

world_file = os.path.join(world_prefix, "worlds", "plug_test.world")
plugins_path = os.path.join(world_prefix, "lib")
log = logging.get_logger(__name__)
log.info(get_package_prefix("mulecar_plugins"))

def generate_launch_description():

    env = {
        "GAZEBO_MODEL_PATH": os.environ["GAZEBO_MODEL_PATH"],
        "GAZEBO_PLUGIN_PATH": os.environ["GAZEBO_PLUGIN_PATH"] + os.pathsep + plugins_path,
        "GAZEBO_RESOURCE_PATH": os.environ["GAZEBO_RESOURCE_PATH"],
    }

    return LaunchDescription(
        [
            ExecuteProcess(
                cmd=[
                    "gazebo",
                    "--verbose",
                    "-s",
                    "libgazebo_ros_simple.so",
                    world_file
                ],
                output="screen",
                additional_env=env
            )
        ]
    )

```

!!! note
    When launch from ROS gazebo alert 
    ```
    [gazebo-1] [Err] [gazebo_shared.cc:46] System is attempting to load a plugin, but detected an incorrect plugin type
    ```
    The plugin run correctly 
    todo: Need more research