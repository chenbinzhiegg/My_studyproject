这里给你整理了 **Ubuntu 20.04/22.04 系统常用命令**，按功能分类，方便你直接取用：

---
### 📁 文件与目录操作
```bash
# 查看当前路径
pwd

# 列出目录内容
ls
ls -l  # 详细信息
ls -a  # 显示隐藏文件

# 切换目录
cd /path/to/dir
cd ~   # 回到用户主目录
cd ..  # 回到上一级目录

# 创建/删除目录
mkdir dir_name
mkdir -p dir1/dir2  # 递归创建多级目录  # mkdir -p ros2_ws/src
rmdir dir_name      # 删除空目录

# 创建/删除文件
touch file.txt
rm file.txt
rm -rf dir_name     # 强制删除目录及所有内容（谨慎使用）

# 复制/移动/重命名
cp source.txt dest.txt
cp -r source_dir dest_dir  # 复制目录
mv old.txt new.txt         # 重命名
mv file.txt /path/to/dir/  # 移动文件
```

---
### 📝 文件查看与编辑
```bash
# 查看文件内容
cat file.txt
less file.txt   # 分页查看（上下键翻页，q退出）
head -n 10 file.txt  # 查看前10行
tail -n 10 file.txt  # 查看后10行
tail -f log.txt      # 实时跟踪文件更新（常用于日志）

# 搜索文件内容
grep "关键词" file.txt
grep -r "关键词" /path/to/dir  # 递归搜索目录下所有文件

# 文本编辑（新手推荐 nano）
nano file.txt  # 简单编辑器，Ctrl+O保存，Ctrl+X退出
vim file.txt   # 功能强大的编辑器，:wq 保存退出，:q! 强制退出
```

---
### ⚙️ 系统与权限管理
```bash
# 更新软件源与软件包
sudo apt update && sudo apt upgrade -y

# 安装/卸载软件
sudo apt install package_name   #安装
sudo apt remove package_name    #卸载
sudo apt autoremove  # 清理无用依赖

# 权限管理
chmod 755 script.sh  # 修改文件权限
chown user:group file.txt  # 修改文件所有者

# 查看系统信息
uname -a        # 内核信息
lsb_release -a  # Ubuntu版本信息
df -h           # 磁盘使用情况
free -h         # 内存使用情况
top / htop      # 查看进程与资源占用
```

---
### 📦 压缩与解压
```bash
# .tar.gz 格式
tar -zcvf archive.tar.gz dir_name/  # 压缩
tar -zxvf archive.tar.gz            # 解压

# .zip 格式
zip -r archive.zip dir_name/
unzip archive.zip

# .bz2 格式
tar -jcvf archive.tar.bz2 dir_name/
tar -jxvf archive.tar.bz2
```

---
### 🌐 网络操作
```bash
# 查看IP地址
ip addr
ifconfig  # 需安装 net-tools

# 测试网络连通性
ping baidu.com

# 下载文件
wget https://example.com/file.zip
curl -O https://example.com/file.zip

# 查看端口占用
netstat -tulpn | grep 8080
ss -tulpn | grep 8080  # 推荐使用，更高效
```

---
### 🔧 进程与任务管理
```bash
# 查看进程
ps aux | grep "进程名"

# 结束进程
kill PID          # 正常结束
kill -9 PID       # 强制结束

# 后台运行任务
./script.sh &     # 后台运行
jobs              # 查看后台任务
fg %1             # 将任务1切回前台
bg %1             # 将任务1切回后台
```

---
### 💡 补充：ROS 2 开发常用辅助命令
```bash
# 刷新环境变量
source /opt/ros/humble/setup.bash
source ~/ros2_ws/install/setup.bash

# 查看ROS2节点/话题/服务
ros2 node list
ros2 topic list
ros2 service list
ros2 topic echo /topic_name  # 查看话题数据
```

需要我帮你按“**新手必背**”和“**进阶常用**”再精简一份吗？