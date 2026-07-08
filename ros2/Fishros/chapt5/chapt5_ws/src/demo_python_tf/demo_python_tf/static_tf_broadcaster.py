import math
import rclpy
from rclpy.node import Node
from tf2_ros import StaticTransformBroadcaster  #静态坐标发布器（Static...)
from geometry_msgs.msg import TransformStamped  #消息接口
from tf_transformations import quaternion_from_euler    #欧拉角转四元数
import math


class StaticTFBroadcaster(Node):

    def __init__(self):
        super().__init__('static_tf2_broadcaster')
        self.static_broadcaster_ = StaticTransformBroadcaster(self) #创建一个静态发布器
        self.publish_static_tf()

    def publish_static_tf(self):
        """
        发布静态TF 从 base_link 到 camera_link 之间的坐标关系
        """
        transform = TransformStamped()
        transform.header.stamp = self.get_clock().now().to_msg()
        transform.header.frame_id = "base_link" #父坐标系
        transform.child_frame_id = "camera_link"    #子坐标系
        transform.transform.translation.x = 0.5 
        transform.transform.translation.y = 0.3 
        transform.transform.translation.z = 0.6 
        # 欧拉角转四元数
        rotation_quat = quaternion_from_euler(math.radians(180), 0, 0)  #生成一个数组
        transform.transform.rotation.x = rotation_quat[0]
        transform.transform.rotation.y = rotation_quat[1]
        transform.transform.rotation.z = rotation_quat[2]
        transform.transform.rotation.w = rotation_quat[3]
      	# 发布静态坐标变换
        self.static_broadcaster_.sendTransform(transform)
        self.get_logger().info(f"发布 TF:{transform}")


def main():
    rclpy.init()
    static_tf_broadcaster = StaticTFBroadcaster()
    rclpy.spin(static_tf_broadcaster)
    rclpy.shutdown()
