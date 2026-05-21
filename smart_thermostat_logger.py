MIN_VALID_TEMP = 40
MAX_VALID_TEMP = 100

COLD_LIMIT = 68
WARM_LIMIT = 76

# Input

User_Temperature = int(input("Enter temperature readings: "))

while User_Temperature <= 0:
    print("Temperature readings need to be greater than 0.")
    User_Temperature = int(input("Enter valid temperature readings: "))

total_temp = 0
below_comfort = 0
above_comfort = 0

for i in range(1, User_Temperature + 1):
    temp = int(input("Enter temperature number" + str(i) + ": "))

    while temp < MIN_VALID_TEMP or temp > MAX_VALID_TEMP:
        print("Temperature must be between", MIN_VALID_TEMP, "and", MAX_VALID_TEMP)
        temp = int(input("Enter valid temperature number" + str(i) + ": "))

    total_temp += temp

    if temp < COLD_LIMIT:
        below_comfort += 1
    elif temp > WARM_LIMIT:
        above_comfort += 1

average_temp = total_temp / User_Temperature