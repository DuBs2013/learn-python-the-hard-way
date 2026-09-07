# Variables and Names

# cars is the number of cars
cars = 100

# space_in_a_car is the total occupancy of each car
space_in_a_car = 4.0

# drivers is the number of drivers available today
drivers = 30

# passengers is the number of people that need a ride
passengers = 90

# cars_not_driven is the number of cars minus the number of available drivers to drive 
cars_not_driven = cars - drivers

# cars_driven is equal to the number of available drivers since only one driver can drive one car at a time
cars_driven = drivers

# carpool_capacity is the number of cars_driven times the amount of space in each car
carpool_capacity = cars_driven * space_in_a_car

# average_passengers_per_car is the number of passengers divided by the number of cars_driven
average_passengers_per_car = passengers / cars_driven   

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

