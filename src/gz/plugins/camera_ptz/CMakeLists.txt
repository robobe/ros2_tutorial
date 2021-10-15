add_library(ptz_plugin SHARED ptz_plugin.cpp)
target_link_libraries(ptz_plugin ${GAZEBO_LIBRARIES})
install(TARGETS ptz_plugin DESTINATION ${PROJECT_SOURCE_DIR}/bin)