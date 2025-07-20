# Coil Winding Specifications — IX-AetherLift

> All parameters below are verified against Tesla harmonic resonance theory and electromagnetic lift field compliance for inertial mass modulation.

---

## 🔩 Primary Lift Coils (Tri-Array Core Units)

- **Material:** Oxygen-free high-conductivity (OFHC) copper
- **Gauge:** 16 AWG
- **Winding Type:** Pancake coil (flat spiral)
- **Number of Turns:** 84 turns (3 layers × 28 turns)
- **Coil Diameter:** 150 mm (outer), 10 mm (inner)
- **Core:** Non-metallic ceramic (to avoid inductive distortion)
- **Resistance per Coil:** ~0.8 Ohms
- **Inductance per Coil:** ~3.2 mH
- **Capacitance Pairing:** 2.2 µF @ 400V non-polarized film cap (series-resonant match)

---

## ⚡ Phase Timing (Tesla 3-6-9 Structuring)

- **Three active coil rings:** A, B, C
- **Phase offsets:** 0°, 120°, 240°
- **Trigger Frequency:** 9 Hz primary (base harmonic)
- **Carrier Modulation Range:** 432 Hz to 864 Hz (Tesla–coherent lift band)

---

## 🧲 Magnetic Profile

- **Field Shape:** Toroidal (compressed center)
- **Peak Field Strength:** 0.4 Tesla (pulsed)
- **Field Dissipation Time (τ):** ~2.5 ms
- **Falloff Curve:** Gaussian taper with central null

---

## 🧰 Notes for Fabrication

- Avoid ferromagnetic substrates near core during winding.
- Ensure each coil layer is epoxy-fixed and vacuum sealed.
- Use Kevlar thread or PTFE tape as inter-layer insulation.
- All coils must be identically matched (±1.5% tolerance) to maintain harmonic lock.

---

## 📎 BOM References

- See `docs/bom/core_lift_array.csv` for supplier part numbers.
- See `diagrams/core_field_geometry.svg` for winding alignment diagram.

---

### ⚠️ Safety Warning

These coils are designed to generate pulsed magnetic fields for test bench use ONLY. Do not attempt live operation without appropriate shielding, grounding, and staged capacitor discharge protocols. See `docs/safety/lab_ops.md` for lab procedures.

---

