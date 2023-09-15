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
2)En una segunda terminal descargamos y corremos el teleop para la distro humble
```bash
sudo apt-get update
sudo apt-get install ros-humble-teleop-twist-keyboard
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```
3)En una tercera terminal iniciamos la recoleccion de los odom logs en el archivo logdinamico.txt
```bash
cd /home
touch logdinamico.txt
python3 dump_odom.py > logdinamico.txt
```

Una vez hecho esto empezamos a usar el teleop y vemos como en gazebo como en rviz el turtlebot se mueve ggwp

4) En esta carpeta ejecutamos
```bash
python3 -m venv venv
python3 -m pip install -r requirements.txt
jupyter-notebook
```