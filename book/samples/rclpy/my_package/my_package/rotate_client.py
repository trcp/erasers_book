import math
import sys

import rclpy
from rclpy.action import ActionClient
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from turtlesim.action import RotateAbsolute


class RotateClient(Node):
    def __init__(self):
        super().__init__('rotate_client')
        self.client = ActionClient(
            self, RotateAbsolute, '/turtle1/rotate_absolute')

    def send_goal(self, theta):
        goal = RotateAbsolute.Goal()
        goal.theta = theta
        self.client.wait_for_server()
        # ゴールを送り、フィードバックが届いたら feedback_callback を呼んでもらう
        future = self.client.send_goal_async(
            goal, feedback_callback=self.feedback_callback)
        future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('ゴールが拒否されました')
            rclpy.shutdown()
            return
        self.get_logger().info('ゴールが受け付けられました')
        # 結果が届いたら result_callback を呼んでもらう
        result_future = goal_handle.get_result_async()
        result_future.add_done_callback(self.result_callback)

    def feedback_callback(self, feedback_msg):
        remaining = feedback_msg.feedback.remaining
        self.get_logger().info(f'残りの回転量: {remaining:.2f} rad')

    def result_callback(self, future):
        result = future.result().result
        self.get_logger().info(f'完了しました（回転量: {result.delta:.2f} rad）')
        rclpy.shutdown()


def main(args=None):
    rclpy.init(args=args)
    node = RotateClient()
    # 引数で角度（度）を受け取る。省略したら 90 度
    degrees = float(sys.argv[1]) if len(sys.argv) > 1 else 90.0
    node.send_goal(math.radians(degrees))
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
