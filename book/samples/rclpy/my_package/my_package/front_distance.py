import math

import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from sensor_msgs.msg import LaserScan


class FrontDistance(Node):
    def __init__(self):
        super().__init__('front_distance')
        # LiDAR から見たロボットの正面の向き [rad]（カチャカは -π/2）
        self.declare_parameter('front_angle', -math.pi / 2)
        self.subscription = self.create_subscription(
            LaserScan, 'lidar/scan', self.scan_callback, qos_profile_sensor_data)

    def scan_callback(self, msg):
        if msg.angle_increment == 0.0:
            return   # 0 で割り算しないように
        # θ = angle_min + i × angle_increment を i について解く
        front_angle = self.get_parameter('front_angle').value
        i = round((front_angle - msg.angle_min) / msg.angle_increment)
        if i < 0 or i >= len(msg.ranges):
            self.get_logger().warn(f'正面の番号 {i} がデータの範囲外です')
            return
        d = msg.ranges[i]
        if math.isinf(d):
            text = '測れる範囲に障害物はありません'
        elif math.isnan(d):
            text = '正しく測れませんでした'
        else:
            text = f'{d:.2f} m'
        # ログがあふれないように、1 秒に 1 回だけ表示する
        self.get_logger().info(f'正面の障害物までの距離: {text}',
                               throttle_duration_sec=1.0)


def main(args=None):
    rclpy.init(args=args)
    node = FrontDistance()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
