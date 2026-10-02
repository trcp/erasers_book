import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    urdf_path = os.path.join(
        get_package_share_directory('my_package'), 'urdf', 'simple_robot.urdf')
    # URDF のファイルを読み込んで、中身を文字列として取り出す
    with open(urdf_path) as f:
        robot_description = f.read()

    return LaunchDescription([
        # URDF と関節の角度から、各リンクの座標変換を tf2 に流す
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_description}],
        ),
        # スライダで関節の角度を決めて、/joint_states に流す
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
        ),
        Node(package='rviz2', executable='rviz2'),
    ])
