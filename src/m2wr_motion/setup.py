from setuptools import setup

package_name = 'm2wr_motion'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
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
            'read_node = m2wr_motion.reading_laser:main',
            'goto = m2wr_motion.goto:main',
            'spawn_box=m2wr_motion.spawn_box:main'
        ],
    },
)