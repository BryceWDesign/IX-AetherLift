-- IX-AetherLift FPGA Control System
-- System Configuration Definitions
-- Version 1.0 — July 2025
-- Author: Bryce Wooster
-- License: IX-AetherLift-OTL

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

package system_config is

    -- Default System Clock Frequency in Hz
    constant SYS_CLK_FREQ : integer := 100_000_000; -- 100 MHz

    -- Base Harmonic Frequencies for Tesla 3-6-9 Logic
    constant BASE_HARMONIC_3   : integer := 3_000_000;  -- 3 MHz
    constant BASE_HARMONIC_6   : integer := 6_000_000;  -- 6 MHz
    constant BASE_HARMONIC_9   : integer := 9_000_000;  -- 9 MHz

    -- FPGA I/O Control Parameters
    constant MODULATION_BITWIDTH : integer := 16;
    constant FREQUENCY_INPUT_WIDTH : integer := 32;

end system_config;
