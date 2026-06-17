import numpy as np
import matplotlib.pyplot as plt

def plot_pulley_kinematics_with_tension(v0=0.0, time_end=2.0):
    try:
        M1 = float(input("Enter the mass of the cart (M1 in kg): "))
        M2 = float(input("Enter the mass of the hanging weight (M2 in kg): "))
        Mp = float(input("Enter the mass of the pulley (Mp in kg): "))
    except ValueError:
        print("Please enter a valid numeric value.")
        return

    g = 9.81
    
    denominator = M1 + M2 + 0.5 * Mp
    a = (M2 / denominator) * g
    
    T1 = (M1 * M2 / denominator) * g
    T2 = ((M1 * M2 + 0.5 * M2 * Mp) / denominator) * g

    print("\n" + "="*45)
    print(f"Entered Cart Mass (M1): {M1} kg")
    print(f"Entered Hanging Mass (M2): {M2} kg")
    print(f"Entered Pulley Mass (Mp): {Mp} kg")
    print(f"Initial Velocity (v0): {v0} m/s")
    print("-" * 45)
    print(f"Calculated Acceleration (a): {a:.3f} m/s²")
    print(f"Calculated Cart-side Tension (T1): {T1:.3f} N")
    print(f"Calculated Hanging-side Tension (T2): {T2:.3f} N")
    print(f"Tension Difference (T2 - T1): {T2 - T1:.3f} N")
    print("="*45 + "\n")

    t = np.linspace(0, time_end, 100)
    v = v0 + a * t
    x = v0 * t + 0.5 * a * t**2

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))

    ax1.plot(t, x, 'b-', linewidth=2, label='Position')
    ax1.set_title('Position vs. Time (Half-Atwood Model)', fontsize=14)
    ax1.set_xlabel('Time (s)', fontsize=12)
    ax1.set_ylabel('Position (m)', fontsize=12)
    ax1.grid(True, linestyle='--', alpha=0.7)
    ax1.legend()

    ax2.plot(t, v, 'r-', linewidth=2, label=f'Velocity (a = {a:.3f} m/s²)')
    ax2.set_title('Velocity vs. Time (Half-Atwood Model)', fontsize=14)
    ax2.set_xlabel('Time (s)', fontsize=12)
    ax2.set_ylabel('Velocity (m/s)', fontsize=12)
    ax2.grid(True, linestyle='--', alpha=0.7)
    ax2.legend()

    plt.tight_layout()
    plt.show()

plot_pulley_kinematics_with_tension(
    v0=0.0,
    time_end=2.0
)