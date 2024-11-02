import matplotlib.pyplot as plt
import time

# Warehouse dimensions and robot specifications
warehouse_width, warehouse_height = 10, 10
robot_speed = 0.1  
movement_time = 0.1  
pause_time = 2  

# Starting and destination coordinates
start_x, start_y = 0, 0
destination_x, destination_y = 7, 9

# Initialize the robot's position
robot_x, robot_y = start_x, start_y

# Initialize plot
plt.figure(figsize=(6, 6))
plt.xlim(0, warehouse_width)
plt.ylim(0, warehouse_height)

# Plot the destination point
plt.plot(destination_x, destination_y, 'go', markersize=10, label="Destination")

# Path tracking
path_x, path_y = [robot_x], [robot_y]

# Function to move the robot towards the destination
def move_robot():
    global robot_x, robot_y
    while ((robot_x - destination_x)**2 + (robot_y - destination_y)**2) > 0.01:  # Allow a small tolerance
        if robot_x < destination_x:
            robot_x += min(robot_speed, destination_x - robot_x)
        elif robot_x > destination_x:
            robot_x -= min(robot_speed, robot_x - destination_x)
        
        if robot_y < destination_y:
            robot_y += min(robot_speed, destination_y - robot_y)
        elif robot_y > destination_y:
            robot_y -= min(robot_speed, robot_y - destination_y)
        
        # Log the path
        path_x.append(robot_x)
        path_y.append(robot_y)
        
        # Plot the current position
        plt.plot(robot_x, robot_y, 'bo')
        plt.pause(movement_time)
        
        # Simulate stopping for 2 seconds
        plt.pause(pause_time)  # Changed from time.sleep to plt.pause

# Start the movement simulation
move_robot()

# Plot the path
plt.plot(path_x, path_y, 'r-', label="Path")
plt.xlabel("X Position (meters)")
plt.ylabel("Y Position (meters)")
plt.title("Autonomous Robot Navigation Simulation")
plt.legend()
plt.show()