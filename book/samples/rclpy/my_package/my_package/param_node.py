import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node


class ParamNode(Node):
    def __init__(self):
        super().__init__('param_node')
        # パラメータを宣言する（名前と初期値）
        self.declare_parameter('robot_name', 'turtle')
        self.declare_parameter('max_speed', 0.5)
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        # パラメータの今の値を取得する
        name = self.get_parameter('robot_name').value
        speed = self.get_parameter('max_speed').value
        self.get_logger().info(f'{name} の最高速度は {speed} m/s です')


def main(args=None):
    rclpy.init(args=args)
    node = ParamNode()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
