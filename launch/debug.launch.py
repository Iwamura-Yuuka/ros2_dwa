import launch
import launch_ros.actions

def generate_launch_description():
    return launch.LaunchDescription([
        launch_ros.actions.Node(
            package='ros2_dwa',
            node_executable='ros2_dwa_node',
            output='screen',
            node_name='ros2_dwa_node',
            remappings=[('/local_map/obstacle', '/obstacle_pose')]
        )
    ])