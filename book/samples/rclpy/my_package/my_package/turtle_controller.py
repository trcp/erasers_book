import rclpy
from geometry_msgs.msg import Twist
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from turtlesim.msg import Pose


class TurtleController(Node):
    def __init__(self):
        super().__init__('turtle_controller')
        self.pose = None
        # カメの位置を受け取る
        self.subscription = self.create_subscription(
            Pose, 'turtle1/pose', self.pose_callback, 10)
        # カメに速度の指令を送る
        self.publisher = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        # 0.1 秒ごとに、次にどう動くかを決める
        self.timer = self.create_timer(0.1, self.timer_callback)

    def pose_callback(self, msg):
        # 最新の位置を覚えておくだけ
        self.pose = msg

    def timer_callback(self):
        if self.pose is None:
            return   # まだ位置が届いていない
        cmd = Twist()
        near_wall = (self.pose.x < 1.5 or self.pose.x > 9.5
                     or self.pose.y < 1.5 or self.pose.y > 9.5)
        if near_wall:
            cmd.linear.x = 0.5    # 壁に近いときは、ゆっくり進みながら曲がる
            cmd.angular.z = 2.0
        else:
            cmd.linear.x = 2.0    # 壁から遠いときは、まっすぐ進む
        self.publisher.publish(cmd)


def main(args=None):
    rclpy.init(args=args)
    node = TurtleController()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
