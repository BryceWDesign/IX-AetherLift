"""
IX-AetherLift Control Algorithms Module
Version 1.0 — July 2025
Author: Bryce Wooster
License: IX-AetherLift-OTL

Core control algorithms for modulation of harmonic resonance and Gankyil feedback loops.
"""

import math
import time

class ResonanceController:
    def __init__(self, base_freq=369.0):
        self.base_freq = base_freq  # Base Tesla 3 frequency in Hz
        self.phase_shift = 0.0      # Current phase shift in degrees
        self.amplitude = 1.0        # Normalized amplitude (0 to 1)
        self.feedback_enabled = True
        self.feedback_latency = 0.7  # milliseconds
        self.last_feedback_time = time.time()

    def set_phase_shift(self, degrees):
        if 0 <= degrees < 360:
            self.phase_shift = degrees
        else:
            raise ValueError("Phase shift must be within 0-359 degrees.")

    def modulate_amplitude(self, input_signal):
        """
        Modulate amplitude based on input signal strength.
        Input signal expected normalized between 0 and 1.
        """
        if not (0 <= input_signal <= 1):
            raise ValueError("Input signal must be normalized between 0 and 1.")
        self.amplitude = input_signal
        return self.amplitude

    def calculate_resonance(self, t):
        """
        Calculate resonance value at time t seconds.
        Uses base frequency, phase shift, and amplitude.
        Returns float resonance output.
        """
        radians = 2 * math.pi * self.base_freq * t + math.radians(self.phase_shift)
        resonance_value = self.amplitude * math.sin(radians)
        return resonance_value

    def feedback_loop(self, sensor_input):
        """
        Adjust phase and amplitude based on sensor input.
        Sensor input expected normalized between 0 and 1.
        """
        current_time = time.time()
        elapsed = (current_time - self.last_feedback_time) * 1000  # ms
        if self.feedback_enabled and elapsed >= self.feedback_latency:
            # Simple feedback: adjust phase by ±5 degrees depending on input
            if sensor_input > 0.5:
                self.phase_shift = (self.phase_shift + 5) % 360
            else:
                self.phase_shift = (self.phase_shift - 5) % 360
            # Adjust amplitude proportionally
            self.amplitude = sensor_input
            self.last_feedback_time = current_time
            return True
        return False
