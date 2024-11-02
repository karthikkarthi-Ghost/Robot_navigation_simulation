# Robot_navigation_simulation

# Autonomous Robot Navigation Simulation

This project simulates an autonomous robot navigating a 10x10 meter warehouse environment. The simulation is built in Python and models the robot’s movement from a specified start point to a target destination within the warehouse while adhering to given constraints.

## Project Overview

The main objective of this project is to simulate an autonomous robot's journey from its starting position to a defined goal in a controlled warehouse setting. The robot’s movement is governed by specific rules regarding speed, pauses, and boundaries.

### Features

- Simulates autonomous robot navigation within a 10x10 meter warehouse
- Models realistic speed and pause behavior:
  - Moves at 0.1 meters per second
  - Pauses for 2 seconds after each 0.1-second movement
- Avoids warehouse boundaries and any possible obstacles

## Getting Started

### Prerequisites

To run this project, you’ll need:
- Python 3.x
- Required Python packages (specified in `requirements.txt` if applicable)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/karthikkarthi-Ghost/Robot_navigation_simulation.git
    cd Robot_navigation_simulation
    ```

2. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. Run the simulation script:

    ```bash
    python simulate_robot.py
    ```

2. Observe the output, which will include:
   - Real-time visualizations of the robot’s movement and pauses
   - Position tracking as it navigates from `(0, 0)` to `(7, 9)`

### Expected Output

The simulation will output:
- Code used for the navigation and stopping logic
- Visual representations or screenshots of the robot’s navigation path
- [Watch the output video](https://drive.google.com/file/d/1BgTcUirc-ve47tH9gZNcGO45SwurtnYp/view?usp=drivesdk)

## Evaluation Criteria

The simulation is assessed based on:

1. **Programming Efficiency**: Organized and efficient code
2. **Simulation Accuracy**: Accurate representation of movement constraints
3. **Creativity and Innovation**: Unique approaches or enhancements in the simulation

## Contributing

Contributions are welcome! Please fork the repository and create a pull request for any changes.

## License

This project is licensed under the MIT License.
