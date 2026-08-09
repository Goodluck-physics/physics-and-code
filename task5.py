transformer_voltage = 200
time = 0
increase_rate = 10

while time <= 10:
    print(f"Volatge of the transformer: {transformer_voltage}volts, time:{time}secs")
    if  transformer_voltage >= 280:
        print("DANGER VOLTAGE HIGH")
    else:
        print("STABLE VOLTAGE")
    transformer_voltage += increase_rate
    time += 1        