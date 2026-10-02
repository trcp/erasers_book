cmake_minimum_required(VERSION 3.8)
project(my_cpp_package)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# 使うパッケージを探す
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(turtlesim REQUIRED)
find_package(example_interfaces REQUIRED)

# ノードごとに、ソースファイルから実行ファイルを作る
add_executable(hello_node src/hello_node.cpp)
ament_target_dependencies(hello_node rclcpp)

add_executable(talker src/talker.cpp)
ament_target_dependencies(talker rclcpp std_msgs)

add_executable(listener src/listener.cpp)
ament_target_dependencies(listener rclcpp std_msgs)

add_executable(turtle_controller src/turtle_controller.cpp)
ament_target_dependencies(turtle_controller rclcpp geometry_msgs turtlesim)

add_executable(add_two_ints_server src/add_two_ints_server.cpp)
ament_target_dependencies(add_two_ints_server rclcpp example_interfaces)

add_executable(param_node src/param_node.cpp)
ament_target_dependencies(param_node rclcpp)

# 作った実行ファイルを install にコピーする
install(TARGETS
  hello_node
  talker
  listener
  turtle_controller
  add_two_ints_server
  param_node
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
