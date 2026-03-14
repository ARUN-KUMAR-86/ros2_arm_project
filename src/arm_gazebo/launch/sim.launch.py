from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
import os

def generate_launch_description():

    world = os.path.join(
        os.getenv('HOME'),
        'arm_ws/src/arm_gazebo/worlds/empty.world'
    )

    xacro_file = os.path.join(
        os.getenv('HOME'),
        'arm_ws/src/arm_description/urdf/arm.xacro'
    )

    return LaunchDescription([

        ExecuteProcess(
            cmd=['gazebo', world, '--verbose', '-s', 'libgazebo_ros_factory.so'],
            output='screen'
        ),

        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=['-entity', 'arm', '-file', xacro_file],
            output='screen'
        )
    ])