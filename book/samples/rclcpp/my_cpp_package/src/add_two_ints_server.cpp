#include <memory>

#include "example_interfaces/srv/add_two_ints.hpp"
#include "rclcpp/rclcpp.hpp"

using AddTwoInts = example_interfaces::srv::AddTwoInts;

class AddTwoIntsServer : public rclcpp::Node
{
public:
  AddTwoIntsServer()
  : Node("add_two_ints_server")
  {
    // add_two_ints サービスを提供する
    service_ = create_service<AddTwoInts>(
      "add_two_ints",
      std::bind(
        &AddTwoIntsServer::add_callback, this,
        std::placeholders::_1, std::placeholders::_2));
  }

private:
  void add_callback(
    const std::shared_ptr<AddTwoInts::Request> request,
    std::shared_ptr<AddTwoInts::Response> response)
  {
    // リクエストを受け取ったら、レスポンスに結果を入れる
    response->sum = request->a + request->b;
    RCLCPP_INFO(
      get_logger(), "%ld + %ld = %ld",
      request->a, request->b, response->sum);
  }

  rclcpp::Service<AddTwoInts>::SharedPtr service_;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<AddTwoIntsServer>());
  rclcpp::shutdown();
  return 0;
}
