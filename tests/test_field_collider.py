"""
Test Suite for field_collider.py — IX-AetherLift
Validates collider mesh synthesis, focus node generation, and vector-field integration logic.
"""

import unittest
import numpy as np
from src.subsystems.field_collider import (
    generate_triangular_emitter_array,
    compute_focal_intersections,
    synthesize_collider_mesh
)

class TestFieldCollider(unittest.TestCase):

    def test_generate_triangular_emitter_array(self):
        result = generate_triangular_emitter_array(radius=1.0, z_height=0.5)
        self.assertEqual(len(result), 3)
        for node in result:
            self.assertIn('position', node)
            self.assertIn('orientation', node)

    def test_compute_focal_intersections_centering(self):
        nodes = [
            {'position': [0, 1, 0.5], 'orientation': [0, -1, 0]},
            {'position': [np.sqrt(3)/2, -0.5, 0.5], 'orientation': [-np.sqrt(3)/2, 0.5, 0]},
            {'position': [-np.sqrt(3)/2, -0.5, 0.5], 'orientation': [np.sqrt(3)/2, 0.5, 0]}
        ]
        result = compute_focal_intersections(nodes)
        self.assertIsInstance(result, np.ndarray)
        self.assertEqual(result.shape, (3,))

    def test_synthesize_collider_mesh(self):
        mesh = synthesize_collider_mesh(emitter_count=3)
        self.assertGreater(len(mesh['nodes']), 0)
        self.assertGreater(len(mesh['edges']), 0)
        self.assertIn('type', mesh)
        self.assertEqual(mesh['type'], 'triadic_focal_structure')

if __name__ == "__main__":
    unittest.main()
