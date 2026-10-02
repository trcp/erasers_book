import rclpy
from my_interfaces.msg import RobotStatus
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node


class StatusPublisher(Node):
    def __init__(self):
        super().__init__('status_publisher')
        self.publisher = self.create_publisher(RobotStatus, 'robot_status', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.battery = 100.0

    def timer_callback(self):
        msg = RobotStatus()
        msg.name = 'turtle'
        msg.battery = self.battery
        msg.is_moving = self.battery > 20.0
        self.publisher.publish(msg)
        self.battery = max(self.battery - 5.0, 0.0)


def main(args=None):
    rclpy.init(args=args)
    node = StatusPublisher()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
