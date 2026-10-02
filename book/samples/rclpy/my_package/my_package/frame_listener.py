import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from rclpy.time import Time
from tf2_ros import TransformException
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener


class FrameListener(Node):
    def __init__(self):
        super().__init__('frame_listener')
        # 届いた座標変換をためておく入れ物と、/tf を受け取るリスナ
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        try:
            # world 座標系から見た turtle1 座標系の位置と向き（最新のもの）
            t = self.tf_buffer.lookup_transform('world', 'turtle1', Time())
        except TransformException as e:
            self.get_logger().info(f'座標変換がまだ得られません: {e}')
            return
        x = t.transform.translation.x
        y = t.transform.translation.y
        self.get_logger().info(f'turtle1 の位置: x={x:.2f}, y={y:.2f}')


def main(args=None):
    rclpy.init(args=args)
    node = FrameListener()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
