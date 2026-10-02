import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from std_msgs.msg import String


class KachakaSpeaker(Node):
    def __init__(self):
        super().__init__('kachaka_speaker')
        self.declare_parameter('text', 'こんにちは、ROS 2 で話しています')
        self.declare_parameter('interval', 10.0)   # 話す間隔 [s]
        # 名前空間（/er_kachaka）を付けて起動すると、/er_kachaka/kachaka_speak になる
        self.publisher = self.create_publisher(String, 'kachaka_speak', 10)
        interval = self.get_parameter('interval').value
        self.timer = self.create_timer(interval, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = self.get_parameter('text').value
        self.publisher.publish(msg)
        self.get_logger().info(f'話す内容: {msg.data}')


def main(args=None):
    rclpy.init(args=args)
    node = KachakaSpeaker()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
