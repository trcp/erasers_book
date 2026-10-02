from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(package='turtlesim', executable='turtlesim_node',
             name='sim', namespace='turtlesim1'),
        Node(package='turtlesim', executable='turtlesim_node',
             name='sim', namespace='turtlesim2'),
        # 1 匹目のカメの位置を受け取り、2 匹目のカメに同じ動きをさせる
        Node(
            package='turtlesim',
            executable='mimic',
            name='mimic',
            remappings=[
                ('/input/pose', '/turtlesim1/turtle1/pose'),
                ('/output/cmd_vel', '/turtlesim2/turtle1/cmd_vel'),
            ],
        ),
    ])
