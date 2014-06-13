#Declaración de variables, no se usan tipos de variables. 
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
#Asignación y operaciones entre variables.
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

#the number of car.
print "There are", cars, "cars available."

#The number of drivers
print "There are only", drivers, "drivers available."

#print the cars_not_drivven value, it's the diffrence 
#between cars and drivers. 
print "There will be", cars_not_driven, "empty cars today."
#The factor between cars_drive and space_in_cars. 
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
