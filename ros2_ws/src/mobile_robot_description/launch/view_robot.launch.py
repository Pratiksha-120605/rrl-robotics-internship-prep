from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():

    pkg_path = get_package_share_directory('mobile_robot_description')

    urdf_file = os.path.join(pkg_path, 'urdf', 'robot.urdf.xacro')
    rviz_config = os.path.join(pkg_path, 'rviz', 'mobile_robot.rviz')

    return LaunchDescription([

        # Robot State Publisher
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            output='screen',
            parameters=[{
                'robot_description': os.popen(f'xacro {urdf_file}').read()
            }]
        ),

        # Joint State Publisher GUI
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            output='screen'
        ),

        # RViz
        ExecuteProcess(
            cmd=['rviz2'],
            output='screen'
        )
    ])
