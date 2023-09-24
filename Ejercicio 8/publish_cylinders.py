#!/usr/bin/env python3

import sys
import rclpy
from rclpy.node import Node
from visualization_msgs.msg import MarkerArray
from visualization_msgs.msg import Marker
from sensor_msgs.msg import LaserScan
import laser_geometry.laser_geometry as lg
import sensor_msgs_py.point_cloud2 as pc2
from itertools import groupby
from operator import itemgetter

class PublishCylindersServer(Node):

    def __init__(self):
        super().__init__('publish_cylinders_server')
        
        self.RADIUS = 1

        self.publisher = self.create_publisher(MarkerArray, "/visualization_marker", 2)
        self.subscriber = self.create_subscription(LaserScan, '/scan', self.execute_callback, 10)

    def execute_callback(self, scan):
        lp = lg.LaserProjection()
        pc2_msg = lp.projectLaser(scan)
        point_generator = pc2.read_points(pc2_msg)
        point_list = pc2.read_points_list(pc2_msg)
        
        markers = MarkerArray()
            
        markers.markers = []
    
        for i, (k, g) in enumerate(groupby(enumerate(point_list), lambda i_x: i_x[0] - i_x[1].index)):
            cylinderPoints = list(map(itemgetter(1), g))
            centralPointX = (cylinderPoints[0].x + cylinderPoints[-1].x)/2
            centralPointY = (cylinderPoints[0].y + cylinderPoints[-1].y)/2
            
            self.get_logger().info(f"Executing goal... {centralPointX}, {centralPointY}")
            
            marker = Marker()

            marker.header.frame_id = "/base_scan"

            # set shape, Arrow: 0; Cube: 1 ; Sphere: 2 ; Cylinder: 3
            marker.type = 3
            marker.id = i

            # Set the scale of the marker
            marker.scale.x = 1.0
            marker.scale.y = 1.0
            marker.scale.z = 1.0

            # Set the color
            marker.color.r = 0.0
            marker.color.g = 1.0
            marker.color.b = 0.0
            marker.color.a = 1.0

            # Set the pose of the marker
            marker.pose.position.x = centralPointX
            marker.pose.position.y = centralPointY
            marker.pose.position.z = 0.0
            marker.pose.orientation.x = 0.0
            marker.pose.orientation.y = 0.0
            marker.pose.orientation.z = 0.0
            marker.pose.orientation.w = 1.0
            
            markers.markers.append(marker)
            
        self.publisher.publish(markers)


def main(args=sys.argv):
    rclpy.init(args=args)
    spawn_entity_node = PublishCylindersServer()
    spawn_entity_node.get_logger().info('Publish Cylinders Server started')
    rclpy.spin(spawn_entity_node)
    spawn_entity_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
