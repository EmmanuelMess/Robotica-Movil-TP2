## Setup

### Install Docker
  - [Docker official Installation guide](https://docs.docker.com/engine/install/)

### Run the setup script

```bash
bash dev/setup.sh
```

```bash
docker compose build
docker compose up -d
docker exec -it simulation_env bash
source /opt/ros/humble/setup.bash
. /usr/share/gazebo/setup.bash
export TURTLEBOT3_MODEL=waffle
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:/opt/ros/humble/share/turtlebot3_gazebo/models
ros2 launch nav2_bringup tb3_simulation_launch.py headless:=False
```
