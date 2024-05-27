
def format_string(number, character):
    formatted_string = "{:{}^10}".format(number, character)
    return formatted_string

result = format_string(145, 'o')
print(result)

radius = 84
pi = 3.14
water_per_square_meter = 1.4  # liters


pond_area = pi * (radius ** 2)

total_water = pond_area * water_per_square_meter

print("The area of the pond is:", int(pond_area))
print("The total amount of water in the pond is:", int(total_water), "liters")

distance = 490  
time_minutes = 7  
time_seconds = time_minutes * 60

speed_mps = distance / time_seconds

print("The speed is:", int(speed_mps), "meters per second")
