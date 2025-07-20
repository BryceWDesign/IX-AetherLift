"""
Test Suite for aether_matrix.py — IX-AetherLift
Validates harmonic matrix construction, symmetry alignment, and phase modulation matrix output.
"""

import unittest
import numpy as np
from src.core.aether_matrix import (
    build_369_matrix,
    validate_gankyil_pattern,
    apply_phase_modulation
)

class TestAetherMatrix(unittest.TestCase):

    def test_build_369_matrix_dimensions(self):
        matrix = build_369_matrix(size=3)
        self.assertIsInstance(matrix, np.ndarray)
        self.assertEqual(matrix.shape, (3, 3))

    def test_validate_gankyil_pattern_logic(self):
        harmonic = np.array([
            [3, 6, 9],
            [9, 3, 6],
            [6, 9, 3]
        ])
        result = validate_gankyil_pattern(harmonic)
        self.assertTrue(result)

    def test_apply_phase_modulation_output(self):
        matrix = np.array([
            [3, 6, 9],
            [9, 3, 6],
            [6, 9, 3]
        ])
        modulated = apply_phase_modulation(matrix, phase_shift=90)
        self.assertEqual(modulated.shape, (3, 3))
        self.assertTrue(np.any(modulated != matrix))

if __name__ == "__main__":
    unittest.main()
