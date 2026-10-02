#include <chrono>
#include <memory>
#include <string>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

using namespace std::chrono_literals;

class Talker : public rclcpp::Node
{
public:
  Talker()
  : Node("talker"), count_(0)
  {
    // String 型のメッセージを chatter トピックにパブリッシュする
    publisher_ = create_publisher<std_msgs::msg::String>("chatter", 10);
    // 500 ミリ秒ごとに timer_callback を呼び出す
    timer_ = create_wall_timer(500ms, std::bind(&Talker::timer_callback, this));
  }

private:
  void timer_callback()
  {
    auto msg = std_msgs::msg::String();
    msg.data = "Hello, ROS 2! " + std::to_string(count_);
    publisher_->publish(msg);
    RCLCPP_INFO(get_logger(), "Publishing: \"%s\"", msg.data.c_str());
    count_++;
  }

  rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
  rclcpp::TimerBase::SharedPtr timer_;
  int count_;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<Talker>());
  rclcpp::shutdown();
  return 0;
}
