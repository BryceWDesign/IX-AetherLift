"""
Tesla Phase Tools — IX-AetherLift
Utility module for harmonic pulse shaping, golden ratio phase alignment, and 3-6-9 interval optimization.
"""

import math
import numpy as np

GOLDEN_RATIO = (1 + math.sqrt(5)) / 2  # φ ≈ 1.618

def harmonic_3_6_9_sequence(base_freq: float, count: int = 9):
    """
    Generate a 3-6-9 Tesla harmonic frequency sequence.

    Parameters:
    - base_freq (float): The initial base frequency in Hz
    - count (int): Number of harmonics to generate

    Returns:
    - list of float: Frequencies following 3-6-9 progression
    """
    return [base_freq * (3 ** (i % 3)) for i in range(count)]

def golden_phase_offsets(base_phase_deg: float, iterations: int = 5):
    """
    Generate phase offsets using the golden ratio spiral pattern.

    Parameters:
    - base_phase_deg (float): Initial phase angle in degrees
    - iterations (int): Number of offsets to return

    Returns:
    - list of float: Golden-ratio distributed phase offsets
    """
    return [(base_phase_deg + (GOLDEN_RATIO * i * 360)) % 360 for i in range(iterations)]

def tri_phase_distribution(base_freq: float, phase_offset_deg: float = 120):
    """
    Calculate a 3-phase frequency distribution aligned to Tesla triadic symmetry.

    Parameters:
    - base_freq (float): Frequency in Hz
    - phase_offset_deg (float): Angular separation in degrees (default 120 for tri-phase)

    Returns:
    - list of dict: Each with frequency and phase in degrees
    """
    return [
        {"freq": base_freq, "phase_deg": 0},
        {"freq": base_freq, "phase_deg": phase_offset_deg},
        {"freq": base_freq, "phase_deg": (2 * phase_offset_deg) % 360}
    ]

def apply_369_modulation(signal: np.ndarray, sample_rate: int):
    """
    Modulate a signal using 3-6-9 gate multipliers.

    Parameters:
    - signal (np.ndarray): Input waveform
    - sample_rate (int): Sample rate in Hz

    Returns:
    - np.ndarray: Modulated waveform
    """
    length = signal.shape[0]
    gate_pattern = np.tile([3, 6, 9], int(np.ceil(length / 3)))[:length]
    modulation = np.sin(2 * np.pi * gate_pattern * np.arange(length) / sample_rate)
    return signal * modulation
