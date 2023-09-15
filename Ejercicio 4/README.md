## Setup
Primero, copiamos dump_odom.py en el container
```bash
docker container cp src/dump_odom.py simulation_env:/home
```
El container no tiene el PIP ni los paquetes transforms3d como el ros-humble-transforms-3d:

```bash
sudo apt install python3-pip
sudo pip3 install transforms3d
sudo apt install ros-humble-tf-transformations
```

Iniciamos el container y corremos la simulacion 
```bash
docker exec -it simulation_env bash
source /opt/ros/humble/setup.bash
. /usr/share/gazebo/setup.bash
export TURTLEBOT3_MODEL=waffle
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:/opt/ros/humble/share/turtlebot3_gazebo/models
ros2 launch nav2_bringup tb3_simulation_launch.py headless:=False
```

En otra terminal empezamos a capturar los mensajer del subscriptor de odometria mientrar el waffle esta estatico:
```bash
docker exec -it simulation_env bash
source /opt/ros/humble/setup.bash
cd /home/
python3 dump_odom.py > log.txt
```
Por ultimo, sacamos el log.txt del container al host
```bash
docker container cp simulation_env:/home/log.txt /home/XXXXX/Desktop/
```

4) En esta carpeta ejecutamos
```bash
python3 -m venv venv
python3 -m pip install -r requirements.txt
jupyter-notebook
```