import rclpy
from rclpy.node import Node
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import sys, tty, termios

class Teleop(Node):

    def __init__(self):
        super().__init__('arm_keyboard')
        self.pub = self.create_publisher(
            JointTrajectory,
            '/arm_controller/joint_trajectory',
            10
        )

        self.pos = [0.0,0.0,0.0,0.0]

    def getKey(self):
        tty.setraw(sys.stdin.fileno())
        key = sys.stdin.read(1)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
        return key

    def run(self):

        while True:
            k = self.getKey()

            if k=='q': self.pos[0]+=0.1
            if k=='a': self.pos[0]-=0.1

            if k=='w': self.pos[1]+=0.1
            if k=='s': self.pos[1]-=0.1

            if k=='e': self.pos[2]+=0.1
            if k=='d': self.pos[2]-=0.1

            if k=='r': self.pos[3]+=0.1
            if k=='f': self.pos[3]-=0.1

            msg = JointTrajectory()
            msg.joint_names = ['joint1','joint2','joint3','gripper_joint']

            point = JointTrajectoryPoint()
            point.positions = self.pos
            point.time_from_start.sec = 1

            msg.points.append(point)

            self.pub.publish(msg)

def main():
    rclpy.init()
    node = Teleop()
    node.run()

settings = termios.tcgetattr(sys.stdin)