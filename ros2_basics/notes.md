# ROS2 Basics

## Environment
- OS: Ubuntu 22.04 LTS
- ROS2 Distribution: Humble
- Editor: VS Code

## What is ROS2
ROS2 is a robotics middleware that provides communication tools such as nodes, topics, services, and actions for building robotic systems.

## Key Concepts
- **Node**: A single executable that performs a specific task
- **Topic**: A named bus over which nodes exchange messages
- **Publisher**: Sends data to a topic
- **Subscriber**: Receives data from a topic

## Basic Commands
```bash
ros2 node list
ros2 topic list
ros2 topic echo /topic_name
```
## Practice

- Created a ROS2 workspace using colcon

- Built and ran a custom Python publisher node

- Verified communication using two terminals
