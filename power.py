import time
import random

class PowerManager:
    def __init__(self):
        self.power_consumption = 0.0  # Current power consumption in kW
        self.total_energy_consumed = 0.0  # Total energy consumed in kWh
        self.is_power_on = False
        self.start_time = None
        
    def turn_on(self):
        if not self.is_power_on:
            self.is_power_on = True
            self.start_time = time.time()
            print("Power turned ON")
        
    def turn_off(self):
        if self.is_power_on:
            self.is_power_on = False
            self.total_energy_consumed += self.power_consumption * ((time.time() - self.start_time) / 3600)  # Convert seconds to hours for kWh
            self.power_consumption = 0.0
            print("Power turned OFF")
            print(f"Total energy consumed: {self.total_energy_consumed:.2f} kWh")
        
    def measure_power_consumption(self):
        # Simulate power consumption measurement
        if self.is_power_on:
            # Generate random power consumption value
            self.power_consumption = random.uniform(0.5, 2.5)  # Random value between 0.5 and 2.5 kW
        else:
            self.power_consumption = 0.0
            
    def get_telemetry_data(self):
        # Return telemetry data as a dictionary
        return {
            "power_on": self.is_power_on,
            "power_consumption": self.power_consumption,
            "total_energy_consumed": self.total_energy_consumed
        }
        
if __name__ == "__main__":
    power_manager = PowerManager()
    
    try:
        while True:
            power_manager.turn_on()
            for _ in range(5):
                power_manager.measure_power_consumption()
                telemetry_data = power_manager.get_telemetry_data()
                print("Telemetry:", telemetry_data)
                time.sleep(1)  # Simulate 1 second interval
            
            power_manager.turn_off()
            time.sleep(2)  # Simulate 2 seconds off time
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
