distance_of_the_drone = 400
time = 0
distance_covered_per_second = 40
distance_log = []
time_log = []

while time <=8:

    distance_log.append(distance_of_the_drone)
    time_log.append(time)

    if distance_of_the_drone <=160:
        print(f"BREACH IMMENIENT AT DISTANCE:{distance_of_the_drone}meters AND TIME{time}seconds")
        
    elif  distance_of_the_drone >161 and distance_of_the_drone <280:
        print(f"WARNING APPROACHING FACILITY  AT DISTANCE: {distance_of_the_drone}meters AND TIME: {time}secconds")
    else:
        print(f"SAFE DISTANCE AT DISTANCE: {distance_of_the_drone}meters AND TIME: {time}seconds")  

    distance_of_the_drone -= distance_covered_per_second
    time += 1

print(f"The Distance log of the drone is{distance_log}")
print(f"The Time log of the drone is {time_log}")    