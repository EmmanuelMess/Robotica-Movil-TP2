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
source /opt/ros/humble/setup.bash
ros2 topic pub /cmd_vel geometry_msgs/Twist '{linear:  {x: 0.5, y: 0.0, z: 0.0}, angular: {x: 0.0,y: 0.0,z: 1.0}}'
```
3)En una tercera terminal iniciamos la recoleccion de los odom logs en el archivo logdinamico.txt
```bash
cd /home
touch logcircular.txt
python3 dump_odom.py > logcircular.txt
```

Antes de esto movimos el robot abajo de la columna central mirando a la derecha. La publicacion constante del topico hace que el 
robot vaya en sentido antihorario alrededor de la columna central

4) En el esta carpeta ejecutamos
```bash
python3 -m venv venv
python3 -m pip install -r requirements.txt
jupyter-notebook
```
