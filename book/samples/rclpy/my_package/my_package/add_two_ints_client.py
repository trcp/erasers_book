import sys

import rclpy
from example_interfaces.srv import AddTwoInts
from rclpy.node import Node


class AddTwoIntsClient(Node):
    def __init__(self):
        super().__init__('add_two_ints_client')
        self.client = self.create_client(AddTwoInts, 'add_two_ints')
        # サーバが起動するまで待つ
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('サービスを待っています...')

    def send_request(self, a, b):
        request = AddTwoInts.Request()
        request.a = a
        request.b = b
        # リクエストを送り、結果を受け取るための future を返す
        return self.client.call_async(request)


def main(args=None):
    rclpy.init(args=args)
    node = AddTwoIntsClient()
    future = node.send_request(int(sys.argv[1]), int(sys.argv[2]))
    # レスポンスが返ってくるまで待つ
    rclpy.spin_until_future_complete(node, future)
    response = future.result()
    node.get_logger().info(f'結果: {response.sum}')
    node.destroy_node()
    rclpy.try_shutdown()


if __name__ == '__main__':
    main()
