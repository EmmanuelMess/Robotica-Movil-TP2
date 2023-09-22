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

## Comandos ros2 topic pub para el camino cuadrado
En el apartado D del ejercicio sabiendo que la velocidad lineal del robot iba a ser 0.1 m/s en las rectas y al girar la angular iba a ser de pi/20 en yaw. Entonces en las rectas
el robot tendria que viajar 20 seg y al momento de girar lo tendria que hacer por 10 seg. Eso en un mundo ideal con un ratio 1:1 entre el tiempo real y el simulado. Lo que hicimos
es agregarle a esos tiempos ideales un promedio del ratio que teniamos entre ambos tiempos (porque el --keep-alive X actua sobre X tiempo real). Debemos admitir  que fue un poco 
rudimentario el ajuste porque no siempre el ratio se mantiene:
```bash
ros2 topic pub --once --keep-alive 23 /cmd_vel geometry_msgs/msg/Twist '{linear:  {x: 0.1, y: 0.0, z: 0.0}, angular: {x: 0.0,y: 0.0,z: 0.0}}'; 
ros2 topic pub --once --keep-alive 11.5 /cmd_vel geometry_msgs/msg/Twist '{linear:  {x: 0.0, y: 0.0, z: 0.0}, angular: {x: 0.0,y: 0.0,z: 0.157079633}}'; 
ros2 topic pub --once --keep-alive 23 /cmd_vel geometry_msgs/msg/Twist '{linear:  {x: 0.1, y: 0.0, z: 0.0}, angular: {x: 0.0,y: 0.0,z: 0.0}}';
ros2 topic pub --once --keep-alive 11.5 /cmd_vel geometry_msgs/msg/Twist '{linear:  {x: 0.0, y: 0.0, z: 0.0}, angular: {x: 0.0,y: 0.0,z: 0.157079633}}'; 
ros2 topic pub --once --keep-alive 23 /cmd_vel geometry_msgs/msg/Twist '{linear:  {x: 0.1, y: 0.0, z: 0.0}, angular: {x: 0.0,y: 0.0,z: 0.0}}';
ros2 topic pub --once --keep-alive 11.5 /cmd_vel geometry_msgs/msg/Twist '{linear:  {x: 0.0, y: 0.0, z: 0.0}, angular: {x: 0.0,y: 0.0,z: 0.157079633}}'; 
ros2 topic pub --once --keep-alive 23 /cmd_vel geometry_msgs/msg/Twist '{linear:  {x: 0.1, y: 0.0, z: 0.0}, angular: {x: 0.0,y: 0.0,z: 0.0}}'; 
ros2 topic pub --once --keep-alive 1  /cmd_vel geometry_msgs/msg/Twist '{linear:  {x: 0.0, y: 0.0, z: 0.0}, angular: {x: 0.0,y: 0.0,z: 0.0}}'
```

##Caminos Circulares
En la carpeta /circulos se encuentras las 4 combinaciones de signos entre velocidad angular y lineal. A forma de breve conclusion son los 4 posibles giros que podemos
hacer con el robot ya sea horario u antihorario tanto de reversa como de frente
