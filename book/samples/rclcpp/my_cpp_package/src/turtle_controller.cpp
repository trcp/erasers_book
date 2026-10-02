#include <chrono>
#include <memory>
#include <optional>

#include "geometry_msgs/msg/twist.hpp"
#include "rclcpp/rclcpp.hpp"
#include "turtlesim/msg/pose.hpp"

using namespace std::chrono_literals;

class TurtleController : public rclcpp::Node
{
public:
  TurtleController()
  : Node("turtle_controller")
  {
    // カメの位置を受け取る
    subscription_ = create_subscription<turtlesim::msg::Pose>(
      "turtle1/pose", 10,
      std::bind(&TurtleController::pose_callback, this, std::placeholders::_1));
    // カメに速度の指令を送る
    publisher_ = create_publisher<geometry_msgs::msg::Twist>("turtle1/cmd_vel", 10);
    // 100 ミリ秒ごとに、次にどう動くかを決める
    timer_ = create_wall_timer(100ms, std::bind(&TurtleController::timer_callback, this));
  }

private:
  void pose_callback(const turtlesim::msg::Pose & msg)
  {
    pose_ = msg;   // 最新の位置を覚えておくだけ
  }

  void timer_callback()
  {
    if (!pose_) {
      return;      // まだ位置が届いていない
    }
    auto cmd = geometry_msgs::msg::Twist();
    bool near_wall = pose_->x < 1.5 || pose_->x > 9.5 ||
      pose_->y < 1.5 || pose_->y > 9.5;
    if (near_wall) {
      cmd.linear.x = 0.5;    // 壁に近いときは、ゆっくり進みながら曲がる
      cmd.angular.z = 2.0;
    } else {
      cmd.linear.x = 2.0;    // 壁から遠いときは、まっすぐ進む
    }
    publisher_->publish(cmd);
  }

  std::optional<turtlesim::msg::Pose> pose_;   // Python の None にあたる「値がない」状態を持てる
  rclcpp::Subscription<turtlesim::msg::Pose>::SharedPtr subscription_;
  rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr publisher_;
  rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<TurtleController>());
  rclcpp::shutdown();
  return 0;
}
