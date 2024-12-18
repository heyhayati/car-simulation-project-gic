# **GIC Assignment: Auto Driving Car Simulation Project**

This project simulates a grid-based field where autonomous cars can move based on a set of predefined commands. The simulation detects collisions between cars and ensures cars stay within the boundaries of the field.

---

## **Assignment Requirements**

The project meets the following criteria:
- **Simulate car movements**: Supports basic movement commands: F (Forward), L (Left turn), and R (Right turn).
- **Collision detection**: Detect and report cars from overlapping or crashing into each other.
- **Configurable Boundary**: Configurable grid size for the simulation field. 
- **State management**: Track the state of each car, including position, speed, and direction.
- **Step-based execution**: Command execution is step-based, ensuring all cars act in sequence.

---

## **Setup and Installation**

Follow these steps to set up the project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/heyhayati/car-simulation-project-gic.git
   ```
2. Navigate to the project directory:
   ```bash
   cd car-simulation-project-gic
   ```
3. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Use `venv\Scripts\activate` on Windows
   ```
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the simulation:
   ```bash
   python main.py
   ```

---

## **How to Use**

1. **Run the Simulation**  
   Launch the simulation using:
   ```bash
   python main.py
   ```

2. **Follow the prompts to:**

- Create a simulation field.
- Add cars with initial positions, directions, and commands.
- Run the simulation and view results.

---

## **Example**

### **Input:**

```
Welcome to Auto Driving Car Simulation!
Please enter the width and height of the simulation field in x y format:
10 10

You have created a field of 10 x 10.

Please choose from the following options:
[1] Add a car to field
[2] Run simulation
Enter your choice: 1
Please enter the name of the car: A
Please enter initial position of car A in x y Direction format: 1 2 N
Please enter the commands for car A: FFRFFFFRRL
```
### **Output:**

```
Your current list of cars are:
- A, (1,2) N, FFRFFFFRRL

After simulation, no collisions occurred.
Final positions:
- A, (5,4) S
```
---
## **Algorithm Overview**
### **Stepwise Simulation Algorithm**
This problem can be classified as a stepwise simulation algorithm because:

1. Sequential Execution:
- Each car executes a single command during each simulation step, ensuring fair and ordered movement.

2. Concurrent Movements:
- Commands for all cars are processed simultaneously within the same step, simulating real-world parallel execution.

3.Collision Detection:
- Collisions are checked after all cars execute their commands in a step. This ensures accurate detection and allows for immediate halting of collided cars.

4.Stateful Simulation:
- Each step updates the state of the grid and cars, carrying forward the outcomes of previous steps to the next.
---
## **Testing**

Unit tests are provided to validate core functionalities such as movement and collision detection. To run the tests:

```bash
pytest
```

Test coverage includes:
- Validating car movements based on speed and direction.
- Ensuring no collisions occur during the simulation.
- Checking state updates for accuracy.

---

## **Key Design Decisions**

1. **Object-Oriented Design:**
- The project follows OOP principles to encapsulate responsibilities and behaviors in specific classes:
  - `Field`: Manages grid dimensions and boundary validation.
  - `Car`: Handles movement, direction changes, and state.
  - `Simulation`: Orchestrates cars, commands, and collision detection.

2.**Step-Based Execution:**  
- Commands are processed one step at a time to ensure fairness between cars and accurate collision detection.

3.**Boundary Validation**
- Cars are prevented from moving out of bounds. Commands that would result in an out-of-bounds movement are ignored.

4.**Collision Detection Logic**
- Positions of cars are tracked using a dictionary for efficient lookup.
- Collisions are detected by checking for multiple cars at the same position after each step.

5.**Car State Management:**
- Each car has its own state (`name`, `x`, `y`, `direction`, and `commands`).
- Cars stop processing commands once they collide with another car.

6.**Modular Structure:**
- Classes are designed to handle specific responsibilities, making the system easy to understand and maintain.

7.**Extensibility:**
- The modular design allows for easy addition of features, such as obstacles or new command types.

---
## **Key Design Decisions**
1. Grid Coordinates:
- The top-left corner of the grid is (0, 0), with x increasing to the right and y increasing downward.

2. Boundary Behavior:
- Cars cannot move beyond the boundaries of the field.
- Commands attempting to move a car out of bounds are ignored.

3. Command Execution:
- All cars process one command per step in parallel. 
- Commands are executed in the order they are provided.

4. Collision Behavior:
- Collisions are detected only at the end of each step.
- Collided cars stop further execution of their commands.
- Simulation ends on first collision.

5. Unique Car Names:
- Each car in the simulation has a unique name.

6. Sequential Input:
- Users add cars and then run the simulation. Cars cannot be added during a simulation.

---
## **Complexity Analysis**
### **Time Complexity**
- Per Step: Processing one command for one car is `O(1)` (updating position or direction).
- Overall: For `n` cars and `m` commands per car, the total complexity is:
                                  `𝑂(𝑛 × 𝑚)`

### **Space Complexity**
- Position Tracking: A dictionary to store car positions, requiring `O(n)` space.
---
## **Future Optimizations**

### **Core Bottlenecks**
- Sequential Processing: Each car processes one command at a time, which can be slow if the number of cars (`n`) and commands (`m`) are large.
- Position Tracking with Dictionary: Although checking for collisions is `O(1)` per step, the overall complexity grows with the number of steps.
- Boundary Checks: Each movement involves repeated checks against the field boundaries.

### **Algorithm Optimization**

1. **Spatial Hashing:**
- Use spatial hashing to efficiently detect collisions in larger grids.
  - Divide the field into smaller regions (e.g., a grid of cells). 
  - Map cars to cells based on their positions. 
  - Check for collisions only within the relevant cell and its neighbors.
This approach reduces unnecessary collision checks in sparse scenarios.

2. **Concurrency:**
- Parallelize the processing of commands for multiple cars.
- Simulates real-time movement in complex scenarios.

3. **Command Preprocessing:**
- Precompute and store valid moves for each position and direction. This reduces boundary checks during execution.
---
## **Future Enhancements**

- Add support for traffic lights and road networks to simulate a realistic traffic environment.
- Introduce AI-based decision-making for autonomous car behaviors.
- Optimize collision detection for highly dense scenarios.

---
## **Contact**

Developed by [Hayati Hamzah](https://www.linkedin.com/in/hayati-hamzah/).  
For any questions, reach out at heyyhayati@gmail.com.
