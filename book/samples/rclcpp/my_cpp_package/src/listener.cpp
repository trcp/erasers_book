#include <memory>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

class Listener : public rclcpp::Node
{
public:
  Listener()
  : Node("listener")
  {
    // chatter トピックを購読し、届くたびに listener_callback を呼び出す
    subscription_ = create_subscription<std_msgs::msg::String>(
      "chatter", 10,
      std::bind(&Listener::listener_callback, this, std::placeholders::_1));
  }

private:
  void listener_callback(const std_msgs::msg::String & msg) const
  {
    RCLCPP_INFO(get_logger(), "I heard: \"%s\"", msg.data.c_str());
  }

  rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscription_;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<Listener>());
  rclcpp::shutdown();
  return 0;
}
