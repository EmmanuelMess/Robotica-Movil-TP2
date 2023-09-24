FROM ros:humble-perception

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    lsb-release \
    wget \
    gnupg \
    ros-humble-turtlesim \
    ros-humble-rqt* \
    ros-humble-navigation2 \
    ros-humble-nav2-bringup \
    ros-humble-turtlebot3* \
    ros-humble-gazebo-* \
    ros-humble-laser-geometry \
    ros-humble-sensor-msgs \
    ros-humble-demo-nodes-cpp \
    ros-humble-demo-nodes-py && \
    rm -rf /var/lib/apt/lists/*

RUN ["/bin/bash", "-c", "source /opt/ros/humble/setup.bash"]
