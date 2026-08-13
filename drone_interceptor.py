time_log = []
distance = []
battery_drain = []

starting_distance =  800
time = 0
battery_status = 100

while time <= 12:
    time_log.append(time)
    distance.append(starting_distance)
    battery_drain.append(battery_drain)

    if starting_distance <= 200:
        print(f"Second {time}: Distance is {starting_distance}m - WARNING: PERIMETER BREACHED!")
    elif starting_distance < 500 and starting_distance > 201:
        print(f"Second {time}: Distance is {starting_distance}m - Status: Target Appraching Zone ") 
    else:
        print(f"Seconds {time}: The Distance is {starting_distance}m - Status: Airspace Secure") 
    print(f"The battery drain history is {battery_drain}")    

    starting_distance -= 50
    battery_drain -= 4
    time +=1    


print("\n=== SYSTEM SIMULATION COMPLETION LOCK ===")

print(f"The drone distance captured at exactly Second 6 was: {distance[6]}m")

        

