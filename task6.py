altitude = 500
time = 0
altitude_decrease_under_free_fall = 50
altitude_decrease_when_thrust_activated = 20
altitude_history = []
time_history = []

print("Simulating flight path and logging data...")

while altitude > 0:
    
    altitude_history.append(altitude)
    time_history.append(time)
    
    
    if altitude <= 200:
        altitude -= altitude_decrease_when_thrust_activated
    else:
        altitude -= altitude_decrease_under_free_fall
        
    time += 1

print("\n=== FLIGHT SIMULATION COMPLETED ===")


print(f"Total Seconds Logged: {len(time_history)} data points")
print(f"Recorded Time Array: {time_history}")
print(f"Recorded Altitude Array: {altitude_history}")
