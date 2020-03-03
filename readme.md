# Agribot bringup
Used to launch Agribot in various configurations

---

## Available launches
### Robot:
`bringup_robot_navigation.launch` \
`bringup_robot_teleop.launch`

### Simulation:
`bringup_simulation_navigation.launch` \
`bringup_simulation_teleop.launch`

### Standalone visualization:
`bringup_visualization.launch`

---

## Available launch arguments
* `vis`
    - true - launches rviz
    - false - turns off visuzalization
* `osm`
    - true - launches OpenStreetMap visualization (only if `vis` is also true)
    - false - turns off OSM visuzalization
* `smach`
    - true - launches commander (state machine)
    - false - launches path_points_stuffer_node

By default (if nothing is added in launch command) parameters are set to false.

---

## Launch example
Launching navigation in simulation, with rviz + OSM visualization and path_points_stuffer_node: \
`roslaunch agribot_bringup bringup_simulation_navigation.launch vis:=true osm:=true smach:=false`
