from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    nodes = []
    for ns in ['robot1', 'robot2']:
        # 同じノードを、名前空間を変えて 2 組起動する
        nodes.append(Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim',
            namespace=ns,
        ))
        nodes.append(Node(
            package='my_package',
            executable='turtle_controller',
            namespace=ns,
        ))
    return LaunchDescription(nodes)
