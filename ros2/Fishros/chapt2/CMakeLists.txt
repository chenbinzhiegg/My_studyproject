cmake_minimum_required(VERSION 3.8) #最小的CMake版本
project(HelloWolrd) #项目名字
add_executable(learn_cmake hello_world.cpp) #生成的可执行文件的名字 原文件名字

find_package(rclcpp REQUIRED)   #直接查找到对应得头文件和库文件
message(STATUS ${rclcpp_INCLUDE_DIRS})  #头文件及rclcpp依赖的头文件
message(STATUS ${rclcpp_LIBRARIES}) #库文件及rclcpp依赖的库文件

target_include_directories(ros2_cpp_node PUBLIC ${rclcpp_INCLUDE_DIRS}) #头文件包含
target_link_libraries(ros2_cpp_node ${rclcpp_LIBRARIES})    #库文件链接