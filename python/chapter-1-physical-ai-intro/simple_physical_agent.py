"""
Simple Physical AI Agent Example

This example demonstrates the basic concepts of Physical AI by implementing
a simple agent that interacts with a physical environment simulation.
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple, List


class SimpleEnvironment:
    """
    A simple 2D environment representing a physical space where the agent operates.
    """

    def __init__(self, width: float = 10.0, height: float = 10.0):
        self.width = width
        self.height = height
        self.obstacles = []  # List of (x, y, radius) tuples

    def add_obstacle(self, x: float, y: float, radius: float):
        """Add a circular obstacle to the environment."""
        self.obstacles.append((x, y, radius))

    def is_valid_position(self, x: float, y: float) -> bool:
        """Check if a position is valid (not inside obstacles)."""
        for obs_x, obs_y, obs_radius in self.obstacles:
            distance = np.sqrt((x - obs_x)**2 + (y - obs_y)**2)
            if distance <= obs_radius:
                return False
        return True

    def get_distance_to_goal(self, pos_x: float, pos_y: float, goal_x: float, goal_y: float) -> float:
        """Calculate Euclidean distance to goal."""
        return np.sqrt((pos_x - goal_x)**2 + (pos_y - goal_y)**2)


class PhysicalAgent:
    """
    A simple Physical AI agent that can sense and act in the environment.
    """

    def __init__(self, start_x: float, start_y: float, env: SimpleEnvironment):
        self.x = start_x
        self.y = start_y
        self.env = env
        self.history = [(start_x, start_y)]  # Track movement history

    def sense(self) -> dict:
        """
        Sense the environment and return sensor readings.
        """
        # Simulate range sensors in 4 directions (front, back, left, right)
        sensor_angles = [0, np.pi, np.pi/2, -np.pi/2]  # radians
        sensor_range = 2.0  # meters
        readings = {}

        for i, angle in enumerate(sensor_angles):
            dx = np.cos(angle) * sensor_range
            dy = np.sin(angle) * sensor_range

            # Sample points along the sensor ray
            num_samples = 10
            step_size = sensor_range / num_samples
            obstacle_detected = False

            for j in range(num_samples):
                sample_x = self.x + np.cos(angle) * j * step_size
                sample_y = self.y + np.sin(angle) * j * step_size

                if not self.env.is_valid_position(sample_x, sample_y):
                    readings[f'sensor_{i}'] = j * step_size
                    obstacle_detected = True
                    break

            if not obstacle_detected:
                readings[f'sensor_{i}'] = sensor_range

        return readings

    def move_towards(self, target_x: float, target_y: float, step_size: float = 0.1):
        """
        Move the agent towards a target position, respecting environment constraints.
        """
        # Calculate direction vector
        dx = target_x - self.x
        dy = target_y - self.y
        distance = np.sqrt(dx**2 + dy**2)

        if distance == 0:
            return  # Already at target

        # Normalize and scale by step size
        dx_norm = (dx / distance) * step_size
        dy_norm = (dy / distance) * step_size

        # Calculate proposed new position
        new_x = self.x + dx_norm
        new_y = self.y + dy_norm

        # Check if the new position is valid
        if self.env.is_valid_position(new_x, new_y):
            self.x = new_x
            self.y = new_y
            self.history.append((new_x, new_y))
        else:
            # If blocked, try to move around the obstacle slightly
            # This is a simplified obstacle avoidance behavior
            adjusted_angle = np.arctan2(dy, dx) + np.random.uniform(-0.2, 0.2)
            new_x = self.x + np.cos(adjusted_angle) * step_size
            new_y = self.y + np.sin(adjusted_angle) * step_size

            if self.env.is_valid_position(new_x, new_y):
                self.x = new_x
                self.y = new_y
                self.history.append((new_x, new_y))

    def get_position(self) -> Tuple[float, float]:
        """Get current position of the agent."""
        return (self.x, self.y)


def run_simple_physical_ai_demo():
    """
    Demonstrate the Physical AI concepts with a simple navigation task.
    """
    print("Physical AI Agent Demo")
    print("=" * 30)

    # Create environment
    env = SimpleEnvironment(width=10.0, height=10.0)

    # Add some obstacles
    env.add_obstacle(5.0, 5.0, 1.0)  # Circular obstacle in the center
    env.add_obstacle(7.0, 3.0, 0.8)  # Another obstacle

    # Create agent
    agent = PhysicalAgent(start_x=1.0, start_y=1.0, env=env)

    # Define goal
    goal_x, goal_y = 8.0, 8.0

    print(f"Starting position: ({agent.x:.2f}, {agent.y:.2f})")
    print(f"Goal position: ({goal_x:.2f}, {goal_y:.2f})")
    print()

    # Run simulation
    max_steps = 200
    reached_goal_threshold = 0.5

    for step in range(max_steps):
        # Sense environment
        sensors = agent.sense()

        # Display sensor readings occasionally
        if step % 20 == 0:
            print(f"Step {step}: Position=({agent.x:.2f}, {agent.y:.2f}), "
                  f"Distance to goal={env.get_distance_to_goal(agent.x, agent.y, goal_x, goal_y):.2f}")
            print(f"Sensors: Front={sensors['sensor_0']:.2f}, Back={sensors['sensor_1']:.2f}, "
                  f"Left={sensors['sensor_2']:.2f}, Right={sensors['sensor_3']:.2f}")

        # Check if reached goal
        distance_to_goal = env.get_distance_to_goal(agent.x, agent.y, goal_x, goal_y)
        if distance_to_goal < reached_goal_threshold:
            print(f"\nGoal reached in {step} steps!")
            break

        # Move towards goal
        agent.move_towards(goal_x, goal_y)

    else:
        print(f"\nMaximum steps reached. Final distance to goal: {distance_to_goal:.2f}")

    # Visualize the path
    fig, ax = plt.subplots(figsize=(10, 10))

    # Plot environment boundaries
    ax.plot([0, env.width, env.width, 0, 0], [0, 0, env.height, env.height, 0], 'k-', linewidth=2)

    # Plot obstacles
    for obs_x, obs_y, obs_radius in env.obstacles:
        circle = plt.Circle((obs_x, obs_y), obs_radius, color='red', alpha=0.5)
        ax.add_patch(circle)

    # Plot path
    path_x, path_y = zip(*agent.history)
    ax.plot(path_x, path_y, 'b-', linewidth=2, label='Agent Path')
    ax.scatter(path_x[0], path_y[0], color='green', s=100, label='Start', zorder=5)
    ax.scatter(path_x[-1], path_y[-1], color='red', s=100, label='End', zorder=5)
    ax.scatter(goal_x, goal_y, color='yellow', s=100, marker='*', label='Goal', zorder=5)

    ax.set_xlim(-0.5, env.width + 0.5)
    ax.set_ylim(-0.5, env.height + 0.5)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.legend()
    ax.set_title('Physical AI Agent Navigation')

    plt.tight_layout()
    plt.show()

    print(f"\nTotal path length: {len(agent.history)} positions recorded")
    print("Demo completed successfully!")


if __name__ == "__main__":
    run_simple_physical_ai_demo()