# Half-Atwood Machine Kinematics Simulator
This repository contains a Python-based simulator for the **Half-Atwood Machine** physics model. The program takes user inputs for the masses of the cart, hanging weight, and pulley, computes the system's acceleration and tensions, and visualizes the kinematics (position and velocity over time) using graphs.

---

## Key Features
- Dynamic user inputs for Cart Mass ($M_1$), Hanging Mass ($M_2$), and Pulley Mass ($M_p$) with error handling.
- Automatic calculation of system acceleration ($a$) and individual string tensions ($T_1$, $T_2$).
- Data visualization providing **Position vs. Time** and **Velocity vs. Time** graphs using Matplotlib.

## Requirements & Environment
To run this simulator, you need Python 3.x and the following external libraries:
- `numpy` (for mathematical arrays and data processing)
- `matplotlib` (for data visualization and plotting)

**Installation Command:**
Open your Terminal (macOS) or Command Prompt (Windows) and run the following command to install the required packages:

```bash
pip install numpy matplotlib
```

## How to Run
```text
1. Download or clone this repository to your local machine.
2. Open your terminal, navigate to the project directory, and run the file using the following command:
   physics_project_group7.py
3. Enter the numeric values for the masses (M1, M2, Mp) when prompted in the terminal.
4. The calculated metrics will be displayed immediately, and a window showing the motion graphs will pop up automatically.
```
