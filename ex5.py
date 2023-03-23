the_name = 'Devon Gifford'
my_age = 28
my_height = 186 #cm's
my_weight = 69 #Kg's
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Brown'

print(f"let's talk about {the_name}.")
print(f"He's {my_height} centimeters tall.") 
print(f"He's {my_weight} kilo's heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee")

#
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")

#Study Drills
#1 - Find and Replace function is your friend

#2 - Converting centimeters to inches, and kilo's to pounds 
my_imperial_height = my_height / 2.54
print(f"\n\nMy height is as follows: \nImperial height\t=\t{my_imperial_height} inches\nMetric height\t=\t{my_height} cm's")

my_imperial_weight = my_weight * 2.205
print(f"\n\nMy weight is as follows: \nImperial weight\t=\t{my_imperial_weight} pounds\nMetric weight\t=\t{my_weight} kilograms")
