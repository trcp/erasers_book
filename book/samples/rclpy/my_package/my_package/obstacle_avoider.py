import math

import rclpy
from geometry_msgs.msg import Twist, TwistStamped
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from sensor_msgs.msg import LaserScan


class ObstacleAvoider(Node):
    def __init__(self):
        super().__init__('obstacle_avoider')
        self.declare_parameter('safe_distance', 0.5)    # 止まって曲がり始める距離 [m]
        self.declare_parameter('linear_speed', 0.15)    # 前に進む速さ [m/s]
        self.declare_parameter('angular_speed', 1.0)    # その場で回る速さ [rad/s]
        self.declare_parameter('front_angle', 0.0)      # LiDAR から見たロボットの正面の向き [rad]
        self.declare_parameter('stamped', True)         # TwistStamped で送るか（False なら Twist）
        self.front_distance = None
        # LiDAR のデータを受け取る（センサ用の QoS を使う）
        self.subscription = self.create_subscription(
            LaserScan, 'scan', self.scan_callback, qos_profile_sensor_data)
        self.stamped = self.get_parameter('stamped').value
        msg_type = TwistStamped if self.stamped else Twist
        self.publisher = self.create_publisher(msg_type, 'cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)

    def scan_callback(self, msg):
        # 正面（左右 30 度以内）の、正しく測れた距離だけを集める
        front_angle = self.get_parameter('front_angle').value
        front = []
        for i in range(len(msg.ranges)):
            angle = msg.angle_min + i * msg.angle_increment - front_angle
            angle = math.atan2(math.sin(angle), math.cos(angle))   # -π〜π に直す
            r = msg.ranges[i]
            if abs(angle) < math.radians(30) and msg.range_min < r < msg.range_max:
                front.append(r)
        # 何も測れなかったときは、正面に障害物がない（無限に遠い）とみなす
        self.front_distance = min(front) if front else math.inf

    def timer_callback(self):
        if self.front_distance is None:
            return   # まだ LiDAR のデータが届いていない
        safe_distance = self.get_parameter('safe_distance').value
        twist = Twist()
        if self.front_distance < safe_distance:
            # 障害物が近いときは、その場で左に回る
            twist.angular.z = self.get_parameter('angular_speed').value
        else:
            # 障害物が遠いときは、まっすぐ進む
            twist.linear.x = self.get_parameter('linear_speed').value
        if self.stamped:
            # TwistStamped では、時刻と座標系の名前も入れる
            cmd = TwistStamped()
            cmd.header.stamp = self.get_clock().now().to_msg()
            cmd.header.frame_id = 'base_link'
            cmd.twist = twist
            self.publisher.publish(cmd)
        else:
            self.publisher.publish(twist)


def main(args=None):
    rclpy.init(args=args)
    node = ObstacleAvoider()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
