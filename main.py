import random
import time

class SimpleThermostat:
    """
    A simple rule-based thermostat that maintains a temperature range.
    This demonstrates a scenario where a complex AI agent might be overkill.
    """
    def __init__(self, desired_min_temp, desired_max_temp):
        self.desired_min_temp = desired_min_temp
        self.desired_max_temp = desired_max_temp
        self.current_temp = random.uniform(18.0, 25.0) # Initial random temperature

    def _perceive(self):
        """
        Simulates perceiving the current environment (temperature).
        In a real system, this would read from a sensor.
        """
        return self.current_temp

    def _decide_action(self, perceived_temp):
        """
        Makes a decision based on simple rules.
        This is the "reasoning engine" part, but purely rule-based.
        """
        # --- This is where the article's concept is illustrated ---
        # For simple, well-defined problems like maintaining a temperature range,
        # a straightforward rule-based approach is often sufficient and more efficient.
        # A complex AI agent with learning might be overkill here, introducing unnecessary
        # complexity, training data requirements, and potential for unpredictable behavior.
        # This highlights when to *avoid* using a full AI agent for simpler tasks.
        if perceived_temp < self.desired_min_temp:
            return "HEAT"
        elif perceived_temp > self.desired_max_temp:
            return "COOL"
        else:
            return "DO_NOTHING"

    def _act(self, action):
        """
        Simulates performing an action on the environment.
        In a real system, this would control a heater/cooler.
        """
        if action == "HEAT":
            self.current_temp += random.uniform(0.5, 1.5) # Simulate heating
            print(f"  Action: Heating (Temp increased)")
        elif action == "COOL":
            self.current_temp -= random.uniform(0.5, 1.5) # Simulate cooling
            print(f"  Action: Cooling (Temp decreased)")
        else:
            # Simulate natural temperature drift if no action is taken
            if self.current_temp < (self.desired_min_temp + self.desired_max_temp) / 2:
                self.current_temp += random.uniform(0.0, 0.2) # Slight natural increase
            else:
                self.current_temp -= random.uniform(0.0, 0.2) # Slight natural decrease
            print(f"  Action: Do Nothing (Temp stable or drifting naturally)")

    def run_cycle(self):
        """Runs one cycle of perceive-decide-act."""
        perceived_temp = self._perceive()
        print(f"Current Temp: {perceived_temp:.2f}°C")
        action = self._decide_action(perceived_temp)
        self._act(action)
        print(f"  New Temp: {self.current_temp:.2f}°C\n")

# --- Main simulation ---
if __name__ == "__main__":
    print("--- Simple Rule-Based Thermostat Simulation ---")
    print("Demonstrates when traditional logic is sufficient, avoiding AI agent overkill.\n")

    thermostat = SimpleThermostat(desired_min_temp=20.0, desired_max_temp=22.0)
    print(f"Desired Temperature Range: {thermostat.desired_min_temp}°C - {thermostat.desired_max_temp}°C\n")

    for i in range(10):
        print(f"--- Cycle {i+1} ---")
        thermostat.run_cycle()
        time.sleep(0.5) # Simulate time passing between cycles

    print("--- Simulation End ---")
