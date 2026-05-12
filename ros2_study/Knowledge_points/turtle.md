这里是从ROS2官方文档整理的 `turtlesim` 完整操作命令，带详细注释，可直接复制运行：

---

### 一、安装与基础启动
```bash
# 1. 安装turtlesim（Humble版本）
sudo apt update
sudo apt install ros-humble-turtlesim

# 2. 验证安装是否成功（查看可执行文件）
ros2 pkg executables turtlesim

# 3. 启动乌龟仿真器主节点（会弹出蓝色窗口）
ros2 run turtlesim turtlesim_node

# 4. 启动键盘控制节点（新开终端，用方向键控制乌龟移动）
ros2 run turtlesim turtle_teleop_key
```


---

### 二、话题（Topic）相关操作
```bash
# 1. 查看所有话题列表
ros2 topic list

# 2. 查看话题的具体消息结构（以速度控制话题为例）
ros2 topic type /turtle1/cmd_vel

# 3. 手动发布速度指令让乌龟移动（单次执行）
ros2 topic pub /turtle1/cmd_vel geometry_msgs/msg/Twist \
"{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.8}}"

# 4. 持续发布速度指令（每秒1次，让乌龟画圆）
ros2 topic pub --rate 1 /turtle1/cmd_vel geometry_msgs/msg/Twist \
"{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.8}}"

# 5. 监听乌龟位姿话题（查看实时坐标和朝向）
ros2 topic echo /turtle1/pose
```

---

### 三、服务（Service）相关操作
```bash
# 1. 查看所有服务列表
ros2 service list

# 2. 清除乌龟行走轨迹（背景上的线条）
ros2 service call /clear std_srvs/srv/Empty "{}"

# 3. 重置乌龟位置到起点（恢复初始状态）
ros2 service call /reset std_srvs/srv/Empty "{}"

# 4. 生成新的乌龟（指定坐标、名字）
ros2 service call /spawn turtlesim/srv/Spawn "{x: 5.0, y: 5.0, theta: 1.57, name: 'turtle2'}"

# 5. 杀死指定乌龟（比如turtle2）
ros2 service call /kill turtlesim/srv/Kill "{name: 'turtle2'}"

# 6. 设置乌龟的画笔颜色和宽度（以turtle1为例）
ros2 service call /turtle1/set_pen turtlesim/srv/SetPen "{r: 255, g: 0, b: 0, width: 3, off: 0}"
```

---

### 四、参数（Parameter）相关操作
```bash
# 1. 查看/turtlesim节点的所有参数
ros2 param list /turtlesim

# 2. 查看当前背景色参数值
ros2 param get /turtlesim background_r
ros2 param get /turtlesim background_g
ros2 param get /turtlesim background_b

# 3. 修改背景色（比如改成偏紫色）
ros2 param set /turtlesim background_r 150
ros2 param set /turtlesim background_g 50
ros2 param set /turtlesim background_b 200
```

---

### 五、节点与系统状态查看
```bash
# 1. 查看当前运行的所有节点
ros2 node list

# 2. 查看/turtlesim节点的详细信息（话题、服务、参数）
ros2 node info /turtlesim

# 3. 查看话题的发布者和订阅者关系
ros2 topic info /turtle1/cmd_vel
```

---

### 六、退出与清理
```bash
# 1. 停止turtlesim_node节点（在运行节点的终端按Ctrl+C）
# 2. 停止turtle_teleop_key节点（在运行节点的终端按q键退出，或Ctrl+C）
```

---

这些命令覆盖了 `turtlesim` 官方教程里的所有操作，从基础启动到话题、服务、参数都包含了，你可以直接复制到终端运行。

需要我再补充一份这些命令的**常见报错排查清单**吗？这样你遇到问题可以快速定位原因。

### 使用rqt

# 放大倍数看
export QT_SCALE_FACTOR=1.5 && rqt 

## 卡死的时候

# 强制关闭 rqt
pkill -9 rqt

# 删除 rqt 损坏的布局配置
rm -f ~/.config/rqt_gui.ini
rm -rf ~/.config/ros.org/rqt_gui.ini

# 清理 rqt 缓存
rm -rf ~/.cache/rqt_*

# 清理 ROS 插件缓存
rm -rf ~/.ros/plugin_cache

# 重启 rqt
rqt