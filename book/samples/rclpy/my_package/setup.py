import os
from glob import glob

from setuptools import find_packages, setup

package_name = 'my_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # launch ファイルと設定ファイルもインストールする
        (os.path.join('share', package_name, 'launch'),
            glob('launch/*.launch.*')),
        (os.path.join('share', package_name, 'config'),
            glob('config/*.yaml')),
        (os.path.join('share', package_name, 'urdf'),
            glob('urdf/*.urdf')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='user',
    maintainer_email='user@todo.todo',
    description='本書の第24章のサンプルのノード',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'my_node = my_package.my_node:main',
            'hello_node = my_package.hello_node:main',
            'talker = my_package.talker:main',
            'listener = my_package.listener:main',
            'turtle_controller = my_package.turtle_controller:main',
            'add_two_ints_server = my_package.add_two_ints_server:main',
            'add_two_ints_client = my_package.add_two_ints_client:main',
            'rotate_client = my_package.rotate_client:main',
            'fibonacci_server = my_package.fibonacci_server:main',
            'param_node = my_package.param_node:main',
            'status_publisher = my_package.status_publisher:main',
            'frame_listener = my_package.frame_listener:main',
            'obstacle_avoider = my_package.obstacle_avoider:main',
            'kachaka_speaker = my_package.kachaka_speaker:main',
            'camera_viewer = my_package.camera_viewer:main',
            'front_distance = my_package.front_distance:main',
        ],
    },
)
