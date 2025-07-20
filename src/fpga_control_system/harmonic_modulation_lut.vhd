-- IX-AetherLift FPGA Control System
-- Harmonic Modulation Look-Up Table (LUT)
-- Version 1.0 — July 2025
-- Author: Bryce Wooster
-- License: IX-AetherLift-OTL

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;
use work.system_config.all;

entity harmonic_modulation_lut is
    Port ( index : in unsigned(HARMONIC_INDEX_WIDTH-1 downto 0);
           modulated_value : out unsigned(MODULATION_WIDTH-1 downto 0)
         );
end harmonic_modulation_lut;

architecture Behavioral of harmonic_modulation_lut is

    type modulation_array is array (0 to 511) of unsigned(MODULATION_WIDTH-1 downto 0);
    constant modulation_table : modulation_array := (
        0 => to_unsigned(369, MODULATION_WIDTH),
        1 => to_unsigned(111, MODULATION_WIDTH),
        2 => to_unsigned(222, MODULATION_WIDTH),
        3 => to_unsigned(333, MODULATION_WIDTH),
        4 => to_unsigned(444, MODULATION_WIDTH),
        5 => to_unsigned(555, MODULATION_WIDTH),
        6 => to_unsigned(666, MODULATION_WIDTH),
        7 => to_unsigned(777, MODULATION_WIDTH),
        -- ... Repeat and fill in up to 511 with Tesla-derived values or experimentally tuned harmonic coefficients
        others => to_unsigned(369, MODULATION_WIDTH)
    );

begin

    modulated_value <= modulation_table(to_integer(index));

end Behavioral;
