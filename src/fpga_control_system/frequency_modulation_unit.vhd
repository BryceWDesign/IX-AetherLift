-- IX-AetherLift FPGA Control System
-- Frequency Modulation Unit
-- Version 1.0 — July 2025
-- Author: Bryce Wooster
-- License: IX-AetherLift-OTL

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;
use work.system_config.all;

entity frequency_modulation_unit is
    Port ( clk : in STD_LOGIC;
           reset : in STD_LOGIC;
           enable : in STD_LOGIC;
           modulation_index : in unsigned(15 downto 0);
           base_freq : in unsigned(FREQUENCY_INPUT_WIDTH-1 downto 0);
           modulated_freq : out unsigned(FREQUENCY_INPUT_WIDTH-1 downto 0)
         );
end frequency_modulation_unit;

architecture Behavioral of frequency_modulation_unit is

    signal freq_shift : unsigned(FREQUENCY_INPUT_WIDTH-1 downto 0);

begin

    process(clk, reset)
    begin
        if reset = '1' then
            freq_shift <= (others => '0');
        elsif rising_edge(clk) then
            if enable = '1' then
                -- Frequency modulation calculation
                freq_shift <= base_freq + (modulation_index * (base_freq / BASE_MODULATION_DIVISOR));
            else
                freq_shift <= base_freq;
            end if;
        end if;
    end process;

    modulated_freq <= freq_shift;

end Behavioral;
