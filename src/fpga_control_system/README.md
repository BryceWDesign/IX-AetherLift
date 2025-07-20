# IX-AetherLift FPGA Control System

> **Modulation and Phase Control Architecture**

---

## 🎛️ Purpose

This directory will contain all Verilog/VHDL logic and configuration files required to implement harmonic field modulation control for IX-AetherLift via FPGA hardware.

---

## ⚙️ Core Responsibilities

- **Tesla 3-6-9 Phase Locking**
- **Pulse Width Modulation (PWM)**
- **Field Strength Vector Adjustment**
- **Feedback Loop Monitoring**

---

## 📂 File Structure (To Be Populated)

- `phase_lock_loop.vhd`
- `pulse_control_unit.vhd`
- `field_modulator_top.vhd`
- `README.md` (this file)

---

## ✅ Development Notes

- **FPGA Model:** Lattice ECP5 (recommended baseline)
- **Frequency Range:** 3 Hz to 369 kHz
- **Safety Clamps:** Zero-ion mode fallback logic to avoid unsafe discharge patterns.

---

## 🔒 Compliance Reminder

All designs in this directory are subject to IX-AetherLift-OTL licensing restrictions.

- **No Weaponization**
- **Civilian Research Only**
- **No TAR/EAR Violations**

---

Document Maintainer: Bryce Wooster  
Version: 1.0 — July 2025  
Project: IX-AetherLift
