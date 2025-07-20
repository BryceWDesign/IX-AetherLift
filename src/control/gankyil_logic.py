"""
IX-AetherLift Gankyil Formation Logic Core
Version 1.0 — July 2025
Author: Bryce Wooster
License: IX-AetherLift-OTL

Implements Gankyil triad logic for harmonic field phase management in AetherLift systems.
"""

import math

class GankyilCore:
    def __init__(self, primary_frequency=369.0):
        self.primary_frequency = primary_frequency  # Tesla 3-Harmonic Anchor
        self.phase_angles = [0, 120, 240]  # Gankyil standard tri-phase
        self.intensities = [1.0, 1.0, 1.0]  # Normalized intensities per phase

    def calculate_gankyil_output(self, t):
        """
        Calculate combined tri-phase Gankyil output value at time t seconds.
        Returns a float value normalized between -1.0 and 1.0.
        """
        combined_signal = 0.0
        for i in range(3):
            angle = 2 * math.pi * self.primary_frequency * t + math.radians(self.phase_angles[i])
            component = self.intensities[i] * math.sin(angle)
            combined_signal += component

        # Normalize combined signal between -1.0 and 1.0
        combined_signal /= 3
        return combined_signal

    def adjust_phase_angles(self, delta_angles):
        """
        Adjust phase angles dynamically.
        delta_angles must be a list of three floats in degrees.
        """
        if len(delta_angles) != 3:
            raise ValueError("Delta angles list must contain exactly three values.")
        self.phase_angles = [(self.phase_angles[i] + delta_angles[i]) % 360 for i in range(3)]

    def adjust_intensities(self, new_intensities):
        """
        Adjust triad intensities.
        new_intensities must be a list of three normalized float values between 0 and 1.
        """
        if len(new_intensities) != 3:
            raise ValueError("Intensities list must contain exactly three values.")
        if not all(0 <= value <= 1 for value in new_intensities):
            raise ValueError("All intensity values must be between 0 and 1.")
        self.intensities = new_intensities
