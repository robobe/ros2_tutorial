cmake_minimum_required(VERSION 3.5)
project(mulecar_plugins)

set(CMAKE_CXX_STANDARD 14)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
# find_package(gazebo REQUIRED)
find_package(gazebo_dev REQUIRED)
find_package(gazebo_ros REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
# find_package(geometry_msgs REQUIRED)

# include_directories(${GAZEBO_INCLUDE_DIRS})
# link_directories(${GAZEBO_LIBRARY_DIRS})
# set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${GAZEBO_CXX_FLAGS}")

# add_library(simple_plugin SHARED src/simple_plugin.cpp)
# target_link_libraries(simple_plugin ${GAZEBO_LIBRARIES})
# target_include_directories(simple_plugin PUBLIC
#   ${CMAKE_CURRENT_SOURCE_DIR}/include)




# # gazebo_ros_template
# add_library(gazebo_ros_template SHARED
#   src/gazebo_ros_template.cpp
# )
# target_include_directories(gazebo_ros_template PUBLIC include)
# ament_target_dependencies(gazebo_ros_template
#   "gazebo_ros"
#   "rclcpp"
# )
# ament_export_libraries(gazebo_ros_template)


# # gazebo_ros_force
# add_library(gazebo_ros_force SHARED
#   src/gazebo_ros_force.cpp
# )
# target_include_directories(gazebo_ros_force PUBLIC include)
# ament_target_dependencies(gazebo_ros_force
#   "gazebo"
#   "gazebo_ros"
#   "geometry_msgs"
#   "rclcpp"
# )

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
  # simple_plugin
  # gazebo_ros_force
  # gazebo_ros_template
  gazebo_ros_simple
  ARCHIVE DESTINATION lib
  LIBRARY DESTINATION lib
  RUNTIME DESTINATION bin)



if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
