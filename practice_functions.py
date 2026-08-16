# Altitude simulation: function + loop + list logging practice
# I am learning pyhton to solve a problem and get a job i want to be useful in the tech aspect of everywhere i go also
# I will soon learn C++ once I am done  with python Thank you.
# This are  just some task i got from Claude AI i can tell you this claudeis amazing it really tasks you wont  tell you the answer
# so far if i made a mistake he tells me not to run the code but the correct it my self he wont tell me the answer it makes me think
# And i really appreaciate that alot from Claude so Claude is my journey partner.

import math
def calculate_fall_time(height):

    time = math.sqrt(2*(height/9.8))

    return time

height =  45
fall_time = calculate_fall_time(height)


print(f"An object falling from 45m takes {fall_time} seconds to hit the ground")


def calculate_landing_velocity(height):
    velocity =  math.sqrt(2*height*9.8)
    return velocity

height = 45
landing_velocity = calculate_landing_velocity(height)

print(f"An object falling from 45m hits the ground at {landing_velocity}m/s")


def calcualte_update_altitude(altitude, decrease_rate):
    change_in_altitude = altitude - decrease_rate
    return change_in_altitude




altitude = 500
time = 0
altitude_log = []
time_log = []

while  altitude > 0:
    altitude_log.append(altitude)
    time_log.append(time)

    altitude = calcualte_update_altitude(altitude,  25)
    print(f"The altittude is {altitude} at time {time}")
   
    time += 1

print(f"The altitude history is {altitude_log}")
print(f"The time history is {time_log}")