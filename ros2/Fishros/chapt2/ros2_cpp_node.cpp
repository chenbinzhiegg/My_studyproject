#include "rclcpp/rclcpp.hpp"

int main(int argc,char** argv)
{
    rclcpp::init(argc,argv);
    auto node = std::make_shared<rclcpp::Node>("cpp_node");
    RCLCPP_INFO(node->get_logger(),"你好c++节点！");
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}


// std::cout<<"参数数量"<<argc<<std::endl;
// std::cout<<"程序名字"<<argv[0]<<std::endl;

/*
# 这份ROS2 C++代码涉及的C++知识点梳理
## 一、基础C++语法


### 2. 程序入口 `main` 函数
```cpp
int main(int argc, char** argv)
```
1. `int main()`：C/C++程序唯一入口函数，返回`int`表示程序退出码
2. `argc`：int类型，命令行参数**个数**
3. `char** argv`：字符串指针数组，存储所有命令行参数
   - `argv[0]`：程序自身名称
   - `argv[1...]`：传入的命令行参数
4. `return 0;`：返回0代表程序正常退出，非0为异常

## 二、命名空间 namespace
代码中大量 `rclcpp::xxx`
- `rclcpp` 是ROS2的C++库命名空间，`::` 为**作用域解析运算符**
- 作用：区分不同库同名类/函数，避免命名冲突
- 等价简写（不推荐大型项目）：`using namespace rclcpp;` 之后直接写`init()`

## 三、auto 类型自动推导（C++11）
```cpp
auto node = std::make_shared<rclcpp::Node>("cpp_node");
```
1. `auto`：编译器根据右侧表达式自动推导变量类型，无需手写长类型
2. 完整等价写法：
```cpp
std::shared_ptr<rclcpp::Node> node = std::make_shared<rclcpp::Node>("cpp_node");
```
3. 规则：定义时必须赋值，不能单独`auto x;`

## 四、模板 & 智能指针（STL标准库）
### 1. 模板函数 `std::make_shared<T>()`
- `<rclcpp::Node>`：**模板参数**，实例化模板函数，指定要创建的对象类型
- 模板是C++泛型编程核心，一套代码适配多种数据类型

### 2. 共享智能指针 `std::shared_ptr`
- STL内存管理工具，自动引用计数，无需手动`new/delete`，内存自动释放，杜绝内存泄漏
- `node->get_logger()`：`->` 箭头运算符，智能指针/裸指针访问类成员（普通对象用`.`）

## 五、类、对象、构造函数
```cpp
std::make_shared<rclcpp::Node>("cpp_node");
```
1. `rclcpp::Node`：ROS2封装的**类**（结构体的升级版，带成员函数、封装）
2. `"cpp_node"`：传入Node类的**构造函数**，初始化节点名称
3. `node->get_logger()`：调用类的**成员函数**，获取日志输出对象

## 六、宏定义（预处理）
```cpp
RCLCPP_INFO(node->get_logger(),"你好c++节点！");
```
- `RCLCPP_INFO` 是库提前用`#define`定义的**宏**，预处理阶段直接文本替换
- 作用：封装日志打印逻辑，分级输出（INFO/WARN/ERROR等）
- 区别于普通函数：无类型检查，纯文本替换

## 七、函数调用 & 作用域生命周期
```cpp
rclcpp::init(argc,argv);   // 初始化ROS2上下文
rclcpp::spin(node);        // 阻塞循环，处理节点消息回调
rclcpp::shutdown();        // 关闭ROS2上下文
```
1. 普通函数调用语法：`函数名(参数)`
2. 生命周期顺序：
   - `init` 启动环境 → 创建节点 → 运行spin循环 → `shutdown` 回收资源
3. `rclcpp::spin(node)`：阻塞函数，程序停留在此，直到Ctrl+C终止

## 八、指针基础：二级指针 `char** argv`
- `char*`：字符串指针（C风格字符串）
- `char**`：指向字符串指针的指针，等价于 `char* argv[]` 字符串数组


## 十、可选拓展：标准输出流（注释代码）
```cpp
std::cout<<"参数数量"<<argc<<std::endl;
```
1. `std`：STL标准库命名空间
2. `cout`：标准输出流对象，`<<` 流插入运算符，链式拼接输出内容
3. `std::endl`：换行并刷新输出缓冲区

# 补充：C++版本要求
`auto`、`std::shared_ptr`、`std::make_shared` 均为 **C++11 标准**，ROS2工程编译时必须指定`c++11`及以上标准。

*/