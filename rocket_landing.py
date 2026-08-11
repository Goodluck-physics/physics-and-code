velocity_of_rocket = 300
time =  0
velocity_log = []
time_log = []

while time <= 10:
    velocity_log.append(velocity_of_rocket)
    time_log.append(time)


    if velocity_of_rocket <= 220:
        print(f"SECOND {time}seconds, VELOCITY IS {velocity_of_rocket}m/s || STATUS TERMINAL STABLE")
    elif velocity_of_rocket > 221 and velocity_of_rocket < 279:
        print(f"SECOND {time}seconds, VELOCITY IS {velocity_of_rocket}m/s || STATUS RETRO BURNING ENGAGED")
        velocity_of_rocket -= 25
    else:
        print(f"SECOND {time}seconds, VELOCITY IS {velocity_of_rocket}m/s || STATUS ATMOSPHERIS PLUNGE DRAG")
        velocity_of_rocket -= 10

    time += 1

print(f"The velocity lod is: {velocity_log}")
print(f"The time log is: {time_log}")       


