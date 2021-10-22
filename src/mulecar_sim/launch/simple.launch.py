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
log.info("-------------------")
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
                    "libsimple_plugin.so",
                    world_file
                ],
                output="screen",
                additional_env=env
            )
        ]
    )
