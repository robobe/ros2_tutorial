# Hello ROS2 launch file

- launch file must contain `generate_launch_description()` function
- launch file must return `LaunchDescription` object

## Copy launch file to install folder
### cmake
```c
install(DIRECTORY
  launch
  DESTINATION share/${PROJECT_NAME}
)
```

### python setup
- Add to data_files array (dest, src)
```python
from glob import glob
...
import os
from glob import glob
from setuptools import setup

package_name = 'my_package'

setup(
    # Other parameters ...
    data_files=[
        # ... Other data files
        # Include all launch files. This is the most important line here!
        (os.path.join('share', package_name), glob('launch/*.launch.py'))
    ]
)
```
## References
- [launch file example](https://roboticsbackend.com/ros2-launch-file-example/)
- [Launching/monitoring multiple nodes with Launch](https://docs.ros.org/en/foxy/Tutorials/Launch-system.html)