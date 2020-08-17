# Agribot bringup
Used to launch Agribot in various configurations

---

## Available launches
### Agribot base
`agribot_base.launch`

### Agribot base for robomaker
`agribot_base_robomaker.launch`

### Standalone visualization:
`bringup_visualization.launch`

### Standalone mapviz:
`bringup_mapviz.launch`

### Bag playback (with robot description):
`bringup_playback.launch`

---

## Available launch arguments (for `agribot_base.launch`)
NOTE: **Bolded** values are default values of arguments

* `launch_type`
    - sim - launches simulation
    - **hal - launches HAL**
    - anything else (e.g. "robomaker") - neither simulation nor HAL are launched
* `path_synchronization`
    - **true - launches path_synchronization node**
    - false - turns off path_synchronization node
* `monitoring`
    - **true - launches monitoring node**
    - false - turns off monitoring node
* `perception_sensors`
    - true - launches agribot_obstacle_detection and include perception sensors in agribot_description
    - **false - turns off agribot_obstacle_detection**
* `world` - name of world (from agribot_simulation/worlds) used in gazebo
    - **empty**
    - vineyard
* `gazebo_gui`
    - true - launches gazebo with GUI
    - **false - launches gazebo without GUI**
* `gazebo_debug`
    - true - launches gazebo in debug mode
    - **false - launches gazebo in debug mode**
* `vis`
    - true - launches visualization
    - **false - turns off visualization**
* `mapviz`
    - true - launches mapviz (if `vis` is also set to true)
    - **false - turns off mapviz**
* `cmd_vel_arbiter_starting_state` - selects starting state of cmd_vel_arbiter 
    - **stop - cmd_vel disconnected (0.0 published)**
    - navigation - cmd_vel connected to cmd_vel_navigation
    - teleop - cmd_vel connected to cmd_vel_teleop
* `map_file` - selects map used in move_base 
    - **$(find agribot_map)/maps/moderna.yaml**
* `use_ukf`
    - true - UKF used in agribot_localization
    - **false - EKF used in agribot_localization**

---
agribot_localization numeric parameters
* `wheel_radius`
    - 0.16
* `chassis_length`
    - 2.1
* `orientation_covariance`
    - 0.01
* `position_covariance`
    - 0.01
* `linear_velocity_x_covariance`
    - 0.0001
* `linear_velocity_y_covariance`
    - 0.0001
* `angular_velocity_z_covariance`
    - 0.0001

---
agribot_obstacle_detection numeric parameters
* `robot_length`
    - 4.3
* `robot_width`
    - 1.4
* `detection_robot_length_offset`
    - 0.3
* `detection_robot_width_offset`
    - 0.3

---

Firebase parameters
* `uid`
* `rsn`
---


## Mapviz

In order to use mapviz satellite maps you need to run docker container
1) Go to agribot_common/docker folder
2) Run docker compose
```
docker-compose up
```

---

## Launch example
`roslaunch agribot_bringup agribot_base.launch launch_type:=sim perception_sensors:=true world:=vineyard vis:=true mapviz:=true  gazebo_gui:=true`