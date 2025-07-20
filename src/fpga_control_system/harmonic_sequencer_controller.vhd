-- IX-AetherLift FPGA Control System
-- Harmonic Sequencer Controller
-- Version 1.0 — July 2025
-- Author: Bryce Wooster
-- License: IX-AetherLift-OTL

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;
use work.system_config.all;

entity harmonic_sequencer_controller is
    Port ( clk : in STD_LOGIC;
           reset : in STD_LOGIC;
           enable : in STD_LOGIC;
           base_harmonic : in unsigned(HARMONIC_INDEX_WIDTH-1 downto 0);
           harmonic_out : out unsigned(HARMONIC_INDEX_WIDTH-1 downto 0)
         );
end harmonic_sequencer_controller;

architecture Behavioral of harmonic_sequencer_controller is

    signal harmonic_counter : unsigned(HARMONIC_INDEX_WIDTH-1 downto 0);

begin

    process(clk, reset)
    begin
        if reset = '1' then
            harmonic_counter <= base_harmonic;
        elsif rising_edge(clk) then
            if enable = '1' then
                if harmonic_counter = MAX_HARMONIC_VALUE then
                    harmonic_counter <= base_harmonic;
                else
                    harmonic_counter <= harmonic_counter + 1;
                end if;
            end if;
        end if;
    end process;

    harmonic_out <= harmonic_counter;

end Behavioral;
