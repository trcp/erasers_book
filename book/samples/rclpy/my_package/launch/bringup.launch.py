import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    pkg_dir = get_package_share_directory('my_package')

    # 起動するときに指定できる引数（launch 引数）を宣言する
    robot_name_arg = DeclareLaunchArgument(
        'robot_name', default_value='turtle',
        description='ロボットの名前')

    # ほかの launch ファイルを読み込む
    turtlesim_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_dir, 'launch', 'turtlesim_controller.launch.py')))

    param_node = Node(
        package='my_package',
        executable='param_node',
        output='screen',
        parameters=[{'robot_name': LaunchConfiguration('robot_name')}],
    )

    return LaunchDescription([
        robot_name_arg,
        turtlesim_launch,
        param_node,
        Node(package='my_package', executable='talker'),
        Node(package='my_package', executable='listener', output='screen'),
    ])
