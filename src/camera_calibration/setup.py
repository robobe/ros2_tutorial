from setuptools import setup
import os
from glob import glob

package_name = 'camera_calibration'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, "sdf"), glob('sdf/*')),
        (os.path.join('share', package_name), glob('launch/*'))
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
            'img_sub = camera_calibration.sub_image:main',
            'mini = camera_calibration.mini_node:main',
            'pnode = camera_calibration.param_node:main'
        ],
    },
)
