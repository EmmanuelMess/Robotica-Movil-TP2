## Setup
1)En una terminal primero corremos la simulacion y ejecutamos el montecarlo para la averiguacion de la posicion final
```bash
docker exec -it simulation_env bash
source /opt/ros/humble/setup.bash
. /usr/share/gazebo/setup.bash
export TURTLEBOT3_MODEL=waffle
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:/opt/ros/humble/share/turtlebot3_gazebo/models
ros2 launch nav2_bringup tb3_simulation_launch.py headless:=False
```
