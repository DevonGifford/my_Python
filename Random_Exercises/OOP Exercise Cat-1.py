#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats

kitty_one = Cat('Tom', 10)
kitty_two = Cat('Garfield', 8)
kitty_three = Cat('Felix', 3)

print(kitty_one.name)
print(kitty_two.name)
print(kitty_three.age)

# 2 Create a function that finds the oldest cat

#IDEA 1
#for kitty in Cat.age():
#    cats_age = Cat.age()
#    oldest_fucking_cat = cats_age.max()
#print(oldest_fucking_cat)
#How do I add the objects variabe to a list?


#IDEA 2
#put all cats ages into a data type (thinking tuple or dictionary)
#useing the built in max function find the oldest 
#    def bouncer():
#        oldest_cat = []
#        age.max()    

#ANSWER
def cat_bouncer(*args):
        return max(args)

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

print(f"The oldest and most wisest cat is {cat_bouncer(kitty_one.age,kitty_two.age,kitty_three.age)} years old there chap")



