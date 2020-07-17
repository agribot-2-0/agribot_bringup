# Agribot bringup
Used to launch Agribot in various configurations

---

## Available launches
### Navigation
`bringup_navigation.launch`

### Teleoperation:
`bringup_teleop.launch`

### Standalone visualization:
`bringup_visualization.launch`

---

## Available launch arguments
* `sim`
    - true - launches simulation
    - false - launches HAL
* `vis`
    - true - launches rviz
    - false - turns off visuzalization
* `osm`
    - true - launches OpenStreetMap visualization (only if `vis` is also true)
    - false - turns off OSM visuzalization
* `smach`
    - true - launches commander (state machine)
    - false - launches path_points_stuffer_node
* `world`
    - empty - empty world without any obstacles
    - orchard - a world with trees in rows

By default (if nothing is added in launch command) parameters are set to false and world is set to empty.

---
## Mapviz

In order to use mapviz satellite maps you need to run docker container
1) Go to agribot_common/docker folder
2) Run docker compose
```
docker-compose up
```

---

## Launch examples
Launching navigation in simulation, with rviz + OSM visualization and path_points_stuffer_node: \
`roslaunch agribot_bringup bringup_navigation.launch sim:=true vis:=true osm:=true`

Launching navigation on robot, with rviz visualization ON, OSM visualization off and commander in use: \
`roslaunch agribot_bringup bringup_navigation.launch vis:=true smach:=true`
