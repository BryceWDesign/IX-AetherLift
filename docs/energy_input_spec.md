# IX-AetherLift Energy Input Specification

> **Approved Energy Sources, Power Requirements, and System Safeguards**

---

## 🔌 Core Input Philosophy

IX-AetherLift is strictly powered by **non-nuclear, non-restricted civilian-grade energy systems**. This aligns with IX-AetherLift-OTL licensing and ensures legal international compliance.

No prohibited high-risk inputs (e.g., weapons-grade fission or fusion power).

---

## ⚡ Acceptable Energy Sources

| **Source Type**         | **Notes**                                      |
|------------------------|------------------------------------------------|
| Solar PV Panels        | Primary for low-power field modulation units.  |
| Liquid Metal Batteries | Preferred for stable DC output.                |
| Molten Salt Batteries  | Optional where higher energy density required. |
| Supercapacitors        | Short-term pulse energy buffers.               |
| Inductive Grid Coupling| For lab-bench prototypes only.                 |

---

## 🔋 Baseline Power Draw Estimates

| **System Component**          | **Typical Draw** | **Peak Draw**   |
|-------------------------------|------------------|-----------------|
| Harmonic Field Coil Driver    | 100 W            | 750 W           |
| Feedback Controller (FPGA)    | 15 W             | 25 W            |
| Sensor Array                  | 20 W             | 35 W            |
| System Cooling (Passive or Active) | 0–50 W       | 100 W (if active) |
| Safety Interlock Systems      | 5 W              | 10 W            |

> **Total Peak Draw:** ≈ 1 kW  
> **Average Continuous Draw (Civilian Prototype):** ≈ 300–500 W

---

## 🔄 Voltage & Current Ratings

- **Nominal Voltage:**  
  48–120 V DC

- **Peak Voltage Tolerance:**  
  Up to 240 V DC (under surge conditions)

- **Continuous Current Range:**  
  5–15 A (depending on build scale)

- **Transient Pulse Support:**  
  System capacitors rated for up to 100 A surge over <10 ms.

---

## ⚠️ Energy System Safety Guidelines

- **Always Isolate Power Before Maintenance**
- **Use Non-Flammable Battery Chemistry Where Possible**
- **Integrate Reverse-Polarity Protection**
- **Do Not Exceed Published Ratings Without Full System Redesign**

---

## 🛑 What Is Prohibited

- Nuclear or radioisotope power sources.
- Weapon-class capacitors (e.g., EMP-grade pulse discharge systems).
- Cryogenic superconducting energy storage (unless specifically cleared for civilian use under local laws).

---

## 📄 Verification Note

All listed specifications align with **real-world, off-the-shelf components** available as of July 2025.  
No proprietary or restricted energy generation methods are included.

---

**Energy Input Specification Last Updated: July 2025**
