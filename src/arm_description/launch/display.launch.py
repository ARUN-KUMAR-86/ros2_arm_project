from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command
import os

def generate_launch_description():

    xacro_file = os.path.join(
        os.getenv('HOME'),
        'arm_ws/src/arm_description/urdf/arm.xacro'
    )

    robot_description = Command(['xacro ', xacro_file])

    return LaunchDescription([

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_description}],
            output='screen'
        ),

        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui'
        ),

        Node(
            package='rviz2',
            executable='rviz2'
        )
    ])