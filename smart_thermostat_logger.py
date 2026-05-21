MIN_VALID_TEMP = 40
MAX_VALID_TEMP = 100

COLD_LIMIT = 68
WARM_LIMIT = 76

# Input

user_readings = int(input("Enter temperature readings: "))

while user_readings <= 0:
    print("Temperature readings need to be greater than 0.")
    user_readings = int(input("Enter valid temperature readings: "))

total_temp = 0
below_comfort = 0
above_comfort = 0

for i in range(1, user_readings + 1):
    temp = int(input("Enter temperature number" + str(i) + ": "))

    while temp < MIN_VALID_TEMP or temp > MAX_VALID_TEMP:
        print("Temperature must be between", MIN_VALID_TEMP, "and", MAX_VALID_TEMP)
        temp = int(input("Enter valid temperature number" + str(i) + ": "))

    total_temp += temp

    if temp < COLD_LIMIT:
        below_comfort += 1
    elif temp > WARM_LIMIT:
        above_comfort += 1

average_temp = total_temp / user_readings

print("Smart Thermostat Summary")
print("------------------------")
print("Average temperature:", round(average_temp, 2))
print("Readings below comfort range:", below_comfort)
print("Readings above comfort range:", above_comfort)