import rclpy                                           # ROS 2 の Python 用ライブラリ
from rclpy.executors import ExternalShutdownException  # 終了するときに起きる例外
from rclpy.node import Node                            # ROS 2 のノードの元になるクラス


class HelloNode(Node):
    def __init__(self):
        super().__init__('hello_node')
        self.get_logger().info('こんにちは、ROS 2!')


def main(args=None):
    rclpy.init(args=args)
    node = HelloNode()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
