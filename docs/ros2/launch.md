# Launch file

### Python package
```
ros2 pkg_create --build-type ament_python <pkg-name>   
```

### launch file

```python linenums="1" hl_lines="8"
from launch import LaunchDescription
import launch_ros.actions

def generate_launch_description():    
    return LaunchDescription([        
        launch_ros.actions.Node(            
            package = 'mulecar',
            executable = 'pub', 
            output = 'screen')])
```

### setup.py

```python linenums="1" hl_lines="14 22"
from setuptools import setup
from glob import glob
import os

package_name = 'mulecar'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        (os.path.join('share', package_name), ['package.xml']),
        (os.path.join('share', package_name),  glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='user',
    maintainer_email='robobe2020@gmail.com',
    entry_points={
        'console_scripts': [
            'pub = mulecar.publisher:main'
        ],
    },
)
```

- (line 14) Copy launch files to install folder
- (line 22) Node entry point call by the launch file `launch_ros.actions.Node` method argument `executable`
- 
## Build and Run
```bash
colcon build --symlink-install --packages-select <pkg_name>
source install/setup.bash
ros2 launch <pkg_name> <launc_file>.launch.py
```
## Resources
- [Launching/monitoring multiple nodes with Launch](https://docs.ros.org/en/foxy/Tutorials/Launch-system.html)