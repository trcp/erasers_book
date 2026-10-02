from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        # turtlesim のノード
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim',
        ),
        # 第24章で作った、カメを自動で動かすノード
        Node(
            package='my_package',
            executable='turtle_controller',
            output='screen',
        ),
    ])
