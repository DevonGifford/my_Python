#These are all the variable that I will use in the program 
#Using variables like this is ideal, as we do not have to 'hard code' the data in the program
cars = 100
sapce_in_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity,"people today")
print("We have",passengers,"passengers to carpool today.")
print("We need to put about", average_passengers_per_car,
" in each car")

#As for the error in the original code 
#The Reason for the traceback error was that the "carpool capacity" variable was only created after a variable had called it
#This is because of something called 'control flow' and in Python follows a sequential execution 
#Meaning that statemets will be performed one after another, i.e. the interpreter goes line by line  