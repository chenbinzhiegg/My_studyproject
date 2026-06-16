这里给你整理了ROS2 `ros2 run` 命令的完整用法和常用示例，全部带标注，可直接复制运行：

---

### 一、基础语法格式
```bash
# 最基础格式（必须掌握）
ros2 run <包名> <可执行文件名>
```
说明：
- `<包名>`：你的ROS2功能包名称（`package.xml` 中定义的 `name` 字段）
- `<可执行文件名>`：编译生成的可执行文件（`CMakeLists.txt` 中 `add_executable` 定义的目标名）

---

### 二、常用示例（直接复制可用）
#### 1. 官方示例包（快速测试ROS2环境）
```bash
# 1. 运行C++版话题发布器（talker）
ros2 run demo_nodes_cpp talker

# 2. 运行C++版话题订阅器（listener），新开终端运行
ros2 run demo_nodes_cpp listener

# 3. 运行Python版话题发布器
ros2 run demo_nodes_py talker

# 4. 运行Python版话题订阅器
ros2 run demo_nodes_py listener
```

#### 2. 海龟仿真器（ROS2入门经典示例）


```bash
# 1. 启动海龟仿真器主节点（会弹出蓝色窗口）
ros2 run turtlesim turtlesim_node

# 2. 启动键盘控制节点，新开终端运行，用方向键控制海龟移动
ros2 run turtlesim turtle_teleop_key
```

#### 3. 自定义包运行（以你截图中的 rclcpp 示例为例）
假设你自己写了一个包 `ros2_study`，可执行文件名为 `my_first_node`：
```bash
# 运行自定义C++节点
ros2 run ros2_study my_first_node
```

---

### 三、进阶用法（带参数/重映射/命名空间）
```bash
# 1. 运行节点并设置节点名称（重命名）
ros2 run demo_nodes_cpp talker --ros-args -r __node:=my_custom_talker

# 2. 运行节点并设置命名空间
ros2 run demo_nodes_cpp talker --ros-args -r __ns:=/robot1

# 3. 话题重映射（将默认话题名改为自定义名称）
ros2 run demo_nodes_cpp talker --ros-args -r chatter:=/custom_topic

# 4. 运行节点并设置参数
ros2 run demo_nodes_cpp talker --ros-args -p some_param:=123

# 5. 组合使用（同时设置命名空间、节点名和话题重映射）
ros2 run demo_nodes_cpp talker --ros-args \
  -r __ns:=/demo \
  -r __node:=my_talker \
  -r chatter:=my_topic
```

---

### 四、运行前必做的准备步骤
```bash
# 1. 先进入工作空间
cd ~/ros2_ws

# 2. 编译工作空间（修改代码后必须执行）
colcon build

# 3. 刷新环境变量（每次新开终端都要执行）
source install/setup.bash

# 4. 验证包是否存在（可选）
ros2 pkg list | grep <你的包名>

# 5. 验证可执行文件是否存在（可选）
ros2 pkg executables <你的包名>
```

---

### 五、常见问题排查
```bash
# 报错“Package not found”：
# 解决：确认包名正确，且已执行 source install/setup.bash

# 报错“Executable not found”：
# 解决：确认可执行文件名正确，且CMakeLists.txt中已配置 install 规则

# 节点运行无日志输出：
# 解决：检查节点中是否调用了 rclcpp::init 和 rclcpp::spin
```

---

如果你把你的功能包名和可执行文件名发给我，我可以帮你生成直接复制就能用的专属运行命令。