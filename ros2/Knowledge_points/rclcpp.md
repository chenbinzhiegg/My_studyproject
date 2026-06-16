`rclcpp.hpp` 是 ROS 2 中 **C++ 客户端库（rclcpp）** 的总入口头文件，几乎写所有 ROS 2 C++ 节点都要先 `#include <rclcpp/rclcpp.hpp>`。

### 一、它是什么
- **全称**：`rclcpp/rclcpp.hpp`
- **位置**：ROS 2 安装目录下 `include/rclcpp/`
- **作用**：一次性包含 ROS 2 C++ 开发最常用的所有头文件，如节点、发布器、订阅器、服务、定时器、参数、日志等，无需逐个 `#include`。

### 二、主要包含的核心类/功能
- **节点**：`rclcpp::Node`（创建节点、管理生命周期）
- **话题通信**：
  - 发布：`rclcpp::Publisher` / `node->create_publisher<MsgT>(topic, qos)`
  - 订阅：`rclcpp::Subscription` / `node->create_subscription<MsgT>(topic, qos, callback)`
- **服务通信**：
  - 服务端：`rclcpp::Service` / `node->create_service<SrvT>(name, callback)`
  - 客户端：`rclcpp::Client` / `node->create_client<SrvT>(name)`
- **定时器**：`rclcpp::WallTimer` / `node->create_wall_timer(period, callback)`
- **参数**：`rclcpp::Parameter`、`node->get_parameter()`、`node->set_parameter()`
- **日志**：`RCLCPP_INFO`、`RCLCPP_WARN`、`RCLCPP_ERROR` 等宏
- **生命周期管理**：`rclcpp::init()`、`rclcpp::spin()`、`rclcpp::shutdown()`

### 三、最小示例（Hello World 节点）
```cpp
#include <rclcpp/rclcpp.hpp>  // 只需要这一个头文件

int main(int argc, char * argv[])
{
    // 1. 初始化 ROS 2
    rclcpp::init(argc, argv);

    // 2. 创建节点（智能指针）
    auto node = std::make_shared<rclcpp::Node>("my_first_node");

    // 3. 打印日志
    RCLCPP_INFO(node->get_logger(), "Hello ROS 2!");

    // 4. 运行节点（处理回调）
    rclcpp::spin(node);

    // 5. 关闭 ROS 2
    rclcpp::shutdown();
    return 0;
}
```

```python
import rclpy
from rclpy.node import Node

def main(args=None):
    # 1. 初始化 ROS 2（对应 C++ 的 rclcpp::init(argc, argv)）
    rclpy.init(args=args)

    # 2. 创建节点（对应 C++ 的 std::make_shared<rclcpp::Node>("my_first_node")）
    node = Node("my_first_node")

    # 3. 打印日志（对应 C++ 的 RCLCPP_INFO(node->get_logger(), "Hello ROS 2!")）
    node.get_logger().info("Hello ROS 2!")

    # 4. 运行节点（处理回调，对应 C++ 的 rclcpp::spin(node)）
    rclpy.spin(node)

    # 5. 关闭 ROS 2（对应 C++ 的 rclcpp::shutdown()）
    rclpy.shutdown()

if __name__ == "__main__":
    main()
```



### 四、编译依赖（package.xml + CMakeLists.txt）
#### package.xml
```xml
<buildtool_depend>ament_cmake</buildtool_depend>
<depend>rclcpp</depend>
```

#### CMakeLists.txt
```cmake
find_package(rclcpp REQUIRED)
add_executable(my_node src/my_node.cpp)
ament_target_dependencies(my_node rclcpp)
```

### 五、常见问题
1. **找不到头文件**：
   - 确认 `package.xml` 有 `<depend>rclcpp</depend>`
   - 确认 `CMakeLists.txt` 有 `find_package(rclcpp REQUIRED)` 和 `ament_target_dependencies(...)`
   - 编译前执行 `source install/setup.bash`
2. **命名空间**：所有核心类都在 `rclcpp::` 命名空间下。

要不要我给你一个可直接编译运行的“发布器+订阅器”完整示例，包含 CMakeLists.txt 和 package.xml？