import time

import rclpy
from example_interfaces.action import Fibonacci
from rclpy.action import ActionServer
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node


class FibonacciServer(Node):
    def __init__(self):
        super().__init__('fibonacci_server')
        self.server = ActionServer(
            self, Fibonacci, 'fibonacci', self.execute_callback)

    def execute_callback(self, goal_handle):
        order = goal_handle.request.order
        self.get_logger().info(f'ゴールを受け取りました（order={order}）')
        feedback = Fibonacci.Feedback()
        feedback.sequence = [0, 1]
        for i in range(1, order):
            feedback.sequence.append(
                feedback.sequence[i] + feedback.sequence[i - 1])
            goal_handle.publish_feedback(feedback)   # 途中経過を送る
            time.sleep(1.0)                          # 時間のかかる処理のかわり
        goal_handle.succeed()
        result = Fibonacci.Result()
        result.sequence = feedback.sequence
        return result                                # 結果を返す


def main(args=None):
    rclpy.init(args=args)
    node = FibonacciServer()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
