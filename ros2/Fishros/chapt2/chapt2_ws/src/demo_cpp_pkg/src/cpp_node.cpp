#include "rclcpp/rclcpp.hpp"

int main(int argc,char** argv)
{
    rclcpp::init(argc,argv);
    auto node = std::make_shared<rclcpp::Node>("cpp_node"); //auto 智能推导类型 ; std:make_shared 创造智能指针
    RCLCPP_INFO(node->get_logger(),"你好c++节点！");
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}
