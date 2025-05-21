class ModelBasedReflexAgent:
    def __init__(self):
        self.last_action = None  # Could be "ON" or "OFF"

    def decide(self, temperature):
        if temperature < 20:
            if self.last_action != "ON":
                self.last_action = "ON"
                return "Turning heater ON"
            else:
                return "Heater is already ON"
        else:
            if self.last_action != "OFF":
                self.last_action = "OFF"
                return "Turning heater OFF"
            else:
                return "Heater is already OFF"

# Example usage
agent = ModelBasedReflexAgent()
temperatures = [18, 19, 19, 21, 21, 18, 20]

for temp in temperatures:
    print(f"Temperature: {temp}°C -> {agent.decide(temp)}")
