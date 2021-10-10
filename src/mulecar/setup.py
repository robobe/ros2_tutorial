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
