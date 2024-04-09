#include "ros2_dwa/ros2_dwa.hpp"

int main(int argc, char *argv[])
{
  rclcpp::init(argc, argv);
  std::shared_ptr<DWAPlanner> dwa = std::make_shared<DWAPlanner>();
  rclcpp::spin(dwa);
  rclcpp::shutdown();
  return 0;
}