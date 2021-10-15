# Model plugin
Create basic plugins and project structure

&nbsp;  
## Project structure
```
├── bin
│   └── libptz_plugin.so
├── build
├── CMakeLists.txt
├── plugins
│   ├── camera_ptz
│   │   ├── CMakeLists.txt
│   │   └── ptz_plugin.cpp
│   └── CMakeLists.txt
├── README.md
└── worlds
    └── plug_teste.world
```

## CMakefiles hierarchy
- root
- plugins
- for each plugin sub directory

### root
```bash
cmake_minimum_required(VERSION 3.0)
project (gz)
# Find Gazebo
find_package(gazebo REQUIRED)
include_directories(${GAZEBO_INCLUDE_DIRS})
link_directories(${GAZEBO_LIBRARY_DIRS})
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${GAZEBO_CXX_FLAGS}")

add_subdirectory(plugins)
```
&NewLine;  
&NewLine;  
### plugins
- This cmake file call other plugin cmake files


```bash
add_subdirectory(camera_ptz)
```
&NewLine;  
&NewLine;  
### plugin 
```bash
add_library(ptz_plugin SHARED ptz_plugin.cpp)
target_link_libraries(ptz_plugin ${GAZEBO_LIBRARIES})
install(TARGETS ptz_plugin DESTINATION ${PROJECT_SOURCE_DIR}/bin)
```
&NewLine;  
&NewLine;  
## Plugin code

- print log message to Console using `gzdbg` `gzmsg` `gzwarn` `gzerr` when running gazebo in verbose mode

&nbsp;  
&nbsp;  
```cpp
#include <functional>
#include <gazebo/gazebo.hh>
#include <gazebo/physics/physics.hh>
#include <gazebo/common/common.hh>
#include <ignition/math/Vector3.hh>

namespace gazebo
{
  class Ptz : public ModelPlugin
  {
    public: void Load(physics::ModelPtr _parent, sdf::ElementPtr /*_sdf*/)
    {
      // Store the pointer to the model
      this->model = _parent;
      gzdbg << "hello debug msg" << std::endl;
      gzmsg << "hello info msg" << std::endl;
      gzwarn << "hello warning msg" << std::endl;
      gzerr << "hello error msg" << std::endl;

      // Listen to the update event. This event is broadcast every
      // simulation iteration.
      this->updateConnection = event::Events::ConnectWorldUpdateBegin(
          std::bind(&Ptz::OnUpdate, this));
    }

    // Called by the world update start event
    public: void OnUpdate()
    {
    }

    // Pointer to the model
    private: physics::ModelPtr model;

    // Pointer to the update event connection
    private: event::ConnectionPtr updateConnection;
  };

  // Register this plugin with the simulator
  GZ_REGISTER_MODEL_PLUGIN(Ptz)
}
```

## world example
```xml
--8<-- "/home/user/ros2_tutorial/src/gz/worlds/plug_teste.world"
```

### usage
```bash
# dont forget add plugin `so` to GAZEBO_PLUGIN_PATH
gazebo --verbose world/plug_test.world

# Or use -s to load plugin
gazebo --verbose -s bin/libptz_plugin.so worlds/plug_teste.world
```

