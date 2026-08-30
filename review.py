def calculate_bettery_status(battery_level):
    if battery_level < 20:
        return "Critical"
    elif battery_level >= 20  and battery_level <= 49:
        return "Low"
    else:
        return "Good"

battery_level = 100

while battery_level > 0:
    result = calculate_bettery_status(battery_level)
    print(f"{battery_level} --- Status {result}")
    battery_level -= 25

print("Device shutting down.")    
