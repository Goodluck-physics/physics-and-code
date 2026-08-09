velocity = 0
acceleration = 15
time = 0
time_step = 0.5

while time <= 5:
    print(f"Time:{time}s  Rocket Velocity: {velocity}m/s")
    velocity += (acceleration * time_step)
    time += time_step