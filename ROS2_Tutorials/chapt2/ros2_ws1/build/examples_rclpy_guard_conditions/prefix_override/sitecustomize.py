import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/chenzhibin/My_studyproject/ROS2_Tutorials/chapt2/ros2_ws1/install/examples_rclpy_guard_conditions'
