types_of_people =10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)
#repeating the above with f.strings within f.strings
print(f"I said: {x}")
print(f"I also said: '{y}'")
#anexample of injecting a variable in a string with .format method (this is from python 2.7 but still works in recent versions)
hilarious = False 
joke_evaluation = "Isn't that joke so funny?!{}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of ..."
e = "a string with a right side."

print(w + e)

#Study Drill - 4 
#This is string concatenation, we are printhing the string named 'w', then we are combining the strings with the '+' symbol, with the string named 'e'.