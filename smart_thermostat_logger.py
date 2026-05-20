MIN_VALID_TEMP = 40
MAX_VALID_TEMP = 100

COLD_LIMIT = 68
WARM_LIMIT = 76

# Input

User_Temperature = float(input("Enter temperature readings: "))

while User_Temperature <= 0:
    print("Temperature readings need to be greater than 0.")
    User_Temperature = float(input("Enter valid temperature readings: "))