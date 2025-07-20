"""
Test Suite for tesla_phase_tools.py — IX-AetherLift
Validates harmonic frequency generation, phase distribution, and modulation methods.
"""

import unittest
import numpy as np
from src.utils import tesla_phase_tools as tpt

class TestTeslaPhaseTools(unittest.TestCase):

    def test_harmonic_3_6_9_sequence(self):
        base_freq = 10.0
        sequence = tpt.harmonic_3_6_9_sequence(base_freq, count=6)
        expected = [10.0, 30.0, 90.0, 10.0, 30.0, 90.0]
        self.assertEqual(sequence, expected)

    def test_golden_phase_offsets(self):
        base_phase = 0
        result = tpt.golden_phase_offsets(base_phase, iterations=3)
        self.assertEqual(len(result), 3)
        self.assertTrue(all(0 <= angle < 360 for angle in result))

    def test_tri_phase_distribution(self):
        result = tpt.tri_phase_distribution(100.0)
        expected_phases = [0, 120, 240]
        for i, r in enumerate(result):
            self.assertEqual(r['freq'], 100.0)
            self.assertAlmostEqual(r['phase_deg'], expected_phases[i])

    def test_apply_369_modulation_shape(self):
        sig = np.ones(12)
        modulated = tpt.apply_369_modulation(sig, 1000)
        self.assertEqual(modulated.shape, sig.shape)

if __name__ == "__main__":
    unittest.main()
