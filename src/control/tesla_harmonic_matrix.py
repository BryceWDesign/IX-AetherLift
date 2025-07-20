"""
IX-AetherLift Tesla Harmonic Matrix Definition
Version 1.0 — July 2025
Author: Bryce Wooster
License: IX-AetherLift-OTL

Defines Tesla 3-6-9 frequency matrix for use in harmonic field generation and resonance control systems.
"""

TESLA_HARMONIC_MATRIX = {
    "Primary_Frequencies": [3, 6, 9],  # Core Tesla set in Hz multiples
    "Extended_Series": {
        "Low_Band": [3, 6, 9, 12, 15, 18, 21],
        "Mid_Band": [369, 396, 432, 528, 639, 741, 852, 963],
        "High_Band": [3330, 6660, 9990],
    },
    "Phase_Angles": {
        "Default": [0, 120, 240],
        "Offset_Options": [15, 30, 45],
    },
    "Usage_Notes": """
    - Primary_Frequencies are used as anchor points for GankyilCore and other field modulation routines.
    - Extended_Series expands usable frequency bands for larger scale field applications.
    - Phase_Angles define starting angles for tri-phase Gankyil logic.
    """,
    "Matrix_Metadata": {
        "Author": "Bryce Wooster",
        "Version": "1.0",
        "Repo": "IX-AetherLift",
        "Date": "July 2025",
    }
}
