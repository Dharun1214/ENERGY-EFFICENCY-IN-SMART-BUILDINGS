# Case Study 3: Energy Efficiency in Smart Buildings
# AI-Based Energy Management System Simulation

import random
import datetime
import matplotlib.pyplot as plt

def simulate_occupancy(hour):
    # Simulate occupancy levels (0 to 1) based on office hours
    if 8 <= hour <= 18:
        return random.uniform(0.4, 1.0)  # Busy during the day
    else:
        return random.uniform(0.0, 0.2)  # Low at night

def get_weather_forecast():
    # Simulate temperature forecast (°C)
    return random.uniform(24, 35)

def get_historical_energy_usage(hour):
    # Simulate historical energy usage (kWh)
    base = 100  # baseline consumption
    if 8 <= hour <= 18:
        return base + random.uniform(50, 100)  # peak hours
    else:
        return base + random.uniform(0, 30)  # off-peak hours

def optimize_hvac(occupancy, temperature, historical_usage):
    # AI-based HVAC adjustment logic
    efficiency_factor = 1.0
    if occupancy < 0.3:
        efficiency_factor *= 0.7  # reduce HVAC use
    if temperature < 26:
        efficiency_factor *= 0.9  # less cooling needed
    elif temperature > 30:
        efficiency_factor *= 1.1  # more cooling needed

    optimized_usage = historical_usage * efficiency_factor
    return optimized_usage

def run_simulation():
    total_energy_saved = 0
    total_cost_saved = 0
    cost_per_kwh = 0.2  # Example energy cost

    hours = list(range(24))
    occupancies = []
    temperatures = []
    historical_usages = []
    optimized_usages = []

    print("Hour | Occupancy | Temp (°C) | Historical (kWh) | Optimized (kWh)")
    for hour in hours:
        occupancy = simulate_occupancy(hour)
        temp = get_weather_forecast()
        historical_usage = get_historical_energy_usage(hour)
        optimized_usage = optimize_hvac(occupancy, temp, historical_usage)

        energy_saved = historical_usage - optimized_usage
        cost_saved = energy_saved * cost_per_kwh

        total_energy_saved += energy_saved
        total_cost_saved += cost_saved

        occupancies.append(occupancy)
        temperatures.append(temp)
        historical_usages.append(historical_usage)
        optimized_usages.append(optimized_usage)

        print(f"{hour:>4} | {occupancy:.2f}      | {temp:.1f}       | {historical_usage:.1f}            | {optimized_usage:.1f}")

    print(f"\nTotal Energy Saved: {total_energy_saved:.2f} kWh")
    print(f"Total Cost Saved: ${total_cost_saved:.2f}")

    # Plotting
    plt.figure(figsize=(12, 6))
    plt.plot(hours, historical_usages, label='Historical Usage (kWh)', marker='o')
    plt.plot(hours, optimized_usages, label='Optimized Usage (kWh)', marker='o')
    plt.title('Energy Consumption Comparison')
    plt.xlabel('Hour of the Day')
    plt.ylabel('Energy (kWh)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    run_simulation()
