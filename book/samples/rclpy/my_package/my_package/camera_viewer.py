import cv2
import rclpy
from cv_bridge import CvBridge
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from sensor_msgs.msg import Image


class CameraViewer(Node):
    def __init__(self):
        super().__init__('camera_viewer')
        self.declare_parameter('edge', False)   # True ならエッジ（輪郭）を表示する
        # ROS 2 の画像のメッセージと、OpenCV の画像を変換する道具
        self.bridge = CvBridge()
        # カメラの画像は BEST_EFFORT で送られてくるので、センサ用の QoS で受け取る
        self.subscription = self.create_subscription(
            Image, 'front_camera/image_raw', self.image_callback,
            qos_profile_sensor_data)

    def image_callback(self, msg):
        # ROS 2 のメッセージ → OpenCV の画像（色の並びは BGR）
        image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        if self.get_parameter('edge').value:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)   # 白黒にする
            image = cv2.Canny(gray, 100, 200)                # エッジを取り出す
        cv2.imshow('Front Camera', image)
        cv2.waitKey(1)   # 画面を更新する


def main(args=None):
    rclpy.init(args=args)
    node = CameraViewer()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        cv2.destroyAllWindows()
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
