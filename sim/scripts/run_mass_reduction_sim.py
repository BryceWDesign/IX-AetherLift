"""
IX-AetherLift: Inertial Mass Reduction Simulation Runner
Author: Bryce Wooster
License: IX-AetherLift-OTL
Version: 1.0 — July 2025

Simulates mass reduction via Tesla 3-6-9 harmonic field resonance. 
Couples frequency matrix with Gankyil tri-phase structure to evaluate lift and damping performance.
"""

import numpy as np
import matplotlib.pyplot as plt
import yaml
import csv
from datetime import datetime

# Load configuration
with open('sim/config/mass_reduction_sim.yaml', 'r') as f:
    config = yaml.safe_load(f)

# Extract relevant config values
freq = config['modulation_field']['frequency_hz']
amplitude = config['modulation_field']['amplitude_scale']
phase_offsets = config['modulation_field']['phase_offsets_deg']
resonance_coupling = config['material_behavior']['field_resonance_coupling']
dampening = config['material_behavior']['inertial_dampening_coefficient']
mass = config['object_properties']['base_mass_kg']

# Simulation parameters
duration = 10  # seconds
sampling_rate = 1000  # Hz
t = np.linspace(0, duration, duration * sampling_rate)
signal = np.zeros_like(t)

# Construct Gankyil tri-phase signal
for offset in phase_offsets:
    signal += amplitude * np.sin(2 * np.pi * freq * t + np.radians(offset))
signal /= 3

# Simulate dynamic mass reduction response
effective_mass = mass - (resonance_coupling * signal * dampening * mass)
effective_mass = np.clip(effective_mass, 0.01, mass)  # avoid zero or negative mass

# Compute lift force generated
g = config['environment']['gravity_m_s2']
lift_force = (mass - effective_mass) * g

# Output and plotting
plt.figure(figsize=(10, 5))
plt.plot(t, effective_mass, label='Effective Mass (kg)', color='blue')
plt.plot(t, lift_force, label='Lift Force (N)', color='green')
plt.title('Mass Reduction & Lift Force Simulation')
plt.xlabel('Time (s)')
plt.ylabel('Values')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("output/mass_reduction_sim_plot.png")
plt.close()

# Save CSV
with open("output/mass_reduction_output.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Time (s)", "Effective Mass (kg)", "Lift Force (N)"])
    for i in range(len(t)):
        writer.writerow([t[i], effective_mass[i], lift_force[i]])

# Archive marker
with open("output/archive_snapshot.txt", "w") as f:
    f.write(f"Mass Reduction Simulation Run: {datetime.utcnow().isoformat()} UTC\n")
    f.write(f"Base Mass: {mass} kg\n")
    f.write(f"Final Effective Mass Range: {np.min(effective_mass):.2f} - {np.max(effective_mass):.2f} kg\n")
