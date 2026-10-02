import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    # インストールされた設定ファイルの場所を調べる
    config = os.path.join(
        get_package_share_directory('my_package'), 'config', 'turtlesim.yaml')

    return LaunchDescription([
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim',
            parameters=[config],              # YAML ファイルから読み込む
        ),
        Node(
            package='my_package',
            executable='param_node',
            output='screen',
            parameters=[config, {'max_speed': 0.8}],   # 後に書いたほうが優先
        ),
    ])
