from setuptools import setup
import os
from glob import glob

package_name = 'ros2_workshop'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, "config"), glob('config/*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='user',
    maintainer_email='robobe2020@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            't_node = ros2_workshop.node_template_timer:main',
            'pnode = ros2_workshop.param_node:main',
            'yaml_node = ros2_workshop.test_yaml_params:main'
        ],
    },
)
