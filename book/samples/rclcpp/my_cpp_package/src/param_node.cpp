#include <chrono>
#include <memory>
#include <string>

#include "rclcpp/rclcpp.hpp"

using namespace std::chrono_literals;

class ParamNode : public rclcpp::Node
{
public:
  ParamNode()
  : Node("param_node")
  {
    // パラメータを宣言する（名前と初期値）
    declare_parameter("robot_name", "turtle");
    declare_parameter("max_speed", 0.5);
    timer_ = create_wall_timer(1s, std::bind(&ParamNode::timer_callback, this));
  }

private:
  void timer_callback()
  {
    // パラメータの今の値を、型を指定して取得する
    std::string name = get_parameter("robot_name").as_string();
    double speed = get_parameter("max_speed").as_double();
    RCLCPP_INFO(get_logger(), "%s の最高速度は %.1f m/s です", name.c_str(), speed);
  }

  rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<ParamNode>());
  rclcpp::shutdown();
  return 0;
}
