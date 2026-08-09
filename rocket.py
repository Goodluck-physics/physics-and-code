altitude = 500
time = 0
altitude_decrease_under_free_fall = 50
altitude_decrease_when_thrust_activated = 20

while altitude > 200:
    print(f"Current Altitude is: {altitude}meters and the time is: {time}secs")
    print("Stable Decend")
    altitude -= altitude_decrease_under_free_fall
    time  += 1

while altitude >= 0:
    print(f"Current Altitude is: {altitude}meters and the time is: {time}secs")
    print("-----THRUST ACTIVATED-----")
    altitude -= altitude_decrease_when_thrust_activated
    time += 1