-- IX-AetherLift FPGA Control System
-- Harmonic Core Controller
-- Version 1.0 — July 2025
-- Author: Bryce Wooster
-- License: IX-AetherLift-OTL

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;
use work.system_config.all;

entity harmonic_core_controller is
    Port ( clk : in STD_LOGIC;
           reset : in STD_LOGIC;
           enable : in STD_LOGIC;
           base_frequency : in unsigned(FREQUENCY_INPUT_WIDTH-1 downto 0);
           harmonic_out : out STD_LOGIC_VECTOR(2 downto 0)  -- 3 outputs for 3-6-9 harmonics
         );
end harmonic_core_controller;

architecture Behavioral of harmonic_core_controller is

    signal counter_3 : unsigned(31 downto 0) := (others => '0');
    signal counter_6 : unsigned(31 downto 0) := (others => '0');
    signal counter_9 : unsigned(31 downto 0) := (others => '0');

    signal out_3 : STD_LOGIC := '0';
    signal out_6 : STD_LOGIC := '0';
    signal out_9 : STD_LOGIC := '0';

begin

    process(clk, reset)
    begin
        if reset = '1' then
            counter_3 <= (others => '0');
            counter_6 <= (others => '0');
            counter_9 <= (others => '0');
            out_3 <= '0';
            out_6 <= '0';
            out_9 <= '0';
        elsif rising_edge(clk) then
            if enable = '1' then

                -- 3 MHz Harmonic Generator
                if counter_3 = (SYS_CLK_FREQ / (2 * BASE_HARMONIC_3)) then
                    out_3 <= not out_3;
                    counter_3 <= (others => '0');
                else
                    counter_3 <= counter_3 + 1;
                end if;

                -- 6 MHz Harmonic Generator
                if counter_6 = (SYS_CLK_FREQ / (2 * BASE_HARMONIC_6)) then
                    out_6 <= not out_6;
                    counter_6 <= (others => '0');
                else
                    counter_6 <= counter_6 + 1;
                end if;

                -- 9 MHz Harmonic Generator
                if counter_9 = (SYS_CLK_FREQ / (2 * BASE_HARMONIC_9)) then
                    out_9 <= not out_9;
                    counter_9 <= (others => '0');
                else
                    counter_9 <= counter_9 + 1;
                end if;

            end if;
        end if;
    end process;

    harmonic_out <= out_9 & out_6 & out_3;

end Behavioral;
