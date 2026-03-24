# ROS2 3DOF Robotic Arm Simulation

This repository contains a **3 Degree of Freedom (3DOF) robotic arm simulation** developed using ROS2.
The project demonstrates robot description, visualization in RViz2, and keyboard-based teleoperation control.
https://youtu.be/x5qHGbrOjgs
---

## 📌 Features

* URDF/Xacro based robotic arm model
* RViz2 visualization
* Keyboard teleoperation control
* ROS2 launch file integration
* Colcon workspace build support
* Modular ROS2 package structure

---

## 📂 Project Structure

```
arm_ws/
 ├── src/
 │   ├── arm_description/
 │   ├── arm_teleop_keyboard/
 ├── README.md
 ├── .gitignore
```

---

## ⚙️ Requirements

* ROS2 (Humble / Iron recommended)
* RViz2
* Python3
* Colcon build tools
* Ubuntu Linux

---

## 🚀 How to Run the Project

### 1️⃣ Clone Repository

```
git clone https://github.com/ARUN-KUMAR-86/ros2_arm_project.git
cd ros2_arm_project
```

### 2️⃣ Build Workspace

```
colcon build
source install/setup.bash
```

### 3️⃣ Launch Robot Visualization

```
ros2 launch arm_description display.launch.py
```

### 4️⃣ Run Keyboard Teleoperation

```
ros2 run arm_teleop_keyboard keyboard_control
```

---

## 🎯 Project Objective

This project is developed for learning and demonstrating:

* Robot Modeling using URDF
* ROS2 Package Development
* Robot Visualization in RViz2
* Teleoperation Concepts
* ROS2 Launch System

---

## 🧠 Future Improvements

* Add Gazebo simulation
* Add MoveIt motion planning
* Add Pick and Place functionality
* Add Joystick control
* Add Real robot hardware interface

---

## 👨‍💻 Author

**Arun Kumar**
Robotics / ROS2 Developer

---

## ⭐ Contribution

Feel free to fork this repository and contribute improvements.

---

