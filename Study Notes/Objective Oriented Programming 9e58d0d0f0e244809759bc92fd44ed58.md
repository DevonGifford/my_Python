# Objective Oriented Programming

Actual: 6 hours
ETA: 4 hours
Materials: https://realpython.com/python3-object-oriented-programming/#:~:text=Object%2Doriented%20programming%20(OOP)%20is%20a%20method%20of%20structuring,the%20components%20of%20a%20system.
Reviewed: No
Section: Section 6
Summary: No
Type: Lecture, Notes
complete: Done

# What Is OOP?

Everything in Python is an object

OOP is a ‘*paradigm*’ - a way to think about and structure code

<aside>
☝ **Object-oriented programming** (OOP) is a method of structuring a program by bundling related properties and behaviours into individual **objects**.

Conceptually, objects are like the components of a system. Think of a program as a factory assembly line of sorts. At each step of the assembly line a system component processes some material, ultimately transforming raw material into a finished product.

An object contains data, like the raw or pre-processed materials at each step on an assembly line, and behaviour, like the action each assembly line component performs.

</aside>

<aside>
☝ Object-oriented programming is a [programming paradigm](http://en.wikipedia.org/wiki/Programming_paradigm) that provides a means of structuring programs so that properties and behaviours are bundled into individual **objects**.

For instance, an object could represent a person with **properties** like a name, age, and address and **behaviours** such as walking, talking, breathing, and running. Or it could represent an [email](https://realpython.com/python-send-email/) with properties like a recipient list, subject, and body and behaviors like adding attachments and sending.

Put another way, object-oriented programming is an approach for modelling concrete, real-world things, like cars, as well as relations between things, like companies and employees, students and teachers, and so on. OOP models real-world entities as software objects that have some data associated with them and can perform certain functions.

Another common programming paradigm is **procedural programming**, which structures a program like a recipe in that it provides a set of steps, in the form of functions and code blocks, that flow sequentially in order to complete a task.
(everything we did in the past)  

The key takeaway is that objects are at the centre of object-oriented programming in Python, not only representing the data, as in procedural programming, but in the overall structure of the program as well.

</aside>

Object-oriented programming (OOP) is **a method of structuring a program by bundling related properties and behaviours into individual objects**

# Class Keyword

---

<aside>
☝ Primitive [data structures](https://realpython.com/courses/python-data-types/) *(like; numbers, strings, and lists)* — are designed to represent simple pieces of information, such as the cost of an apple, the name of a poem, or your favourite colours, respectively. What if you want to represent something more complex?

For example, let’s say you want to track employees in an organization. You need to store some basic information about each employee, such as their name, age, position, and the year they started working.

One way to do this is to represent each employee as a [list](https://realpython.com/python-lists-tuples/):

```python
kirk = ["James Kirk", 34, "Captain", 2265]
spock = ["Spock", 35, "Science Officer", 2254]
mccoy = ["Leonard McCoy", "Chief Medical Officer", 2266]`
```

There are a number of issues with this approach.

1. First, it can make larger code files more difficult to manage. If you reference `kirk[0]` several lines away from where the `kirk` list is declared, will you remember that the element with index `0` is the employee’s name?
2. Second, it can introduce errors if not every employee has the same number of elements in the list. In the `mccoy` list above, the age is missing, so `mccoy[1]` will return `"Chief Medical Officer"` instead of Dr. McCoy’s age.

A great way to make this type of code more manageable and more maintainable is to use **classes**.

</aside>

- You can create your own data type using `class` keyword
    
    ---
    
    - make sure using capitals letter
    - using CamelCode (ThisIsWhatTheyCallCamelCode)
    
    basic example
    
    ```python
    class BigObject:                         #this is the 'class'
    	pass
    
    obj1 = BigObject()                       #this is the object
    print (type(BigObject)
    >
    class '__main__.BigObject()
    ```
    
- The `class` is the blue print of what we want to make:
    
    ---
    
    - basic attributes
    - basic methods or actions can make
    
- The class can be instantiated in creating different instances
    
    ---
    
    <aside>
    ☝ All OOP Languages use this type of language 
    *- “I just instantiated this class”
    - “I just created a new instance/object”*
    
    </aside>
    
    lets look at this with the previous example; 
    
    ```python
    class BigObject:                #Class
    	pass   
    
    obj1 = BigObject()              #Instantiate
    print (type(BigObject)
    >
    class '__main__.BigObject()
    ```
    

# Creating Our Own Objects

Learning via coding - Creating a class for a character in a videogame.

```python
class PlayerCharacter:
	def __init__(self, name, age, maritial_status):          #__init__ = dunder method 
		self.name = name                                       #attribute 1 - almost alwasy self is the first attibute
		self.age = age                                         #attribute 2
		self.maritial_status = maritial_status                 #attribute 3

	def run(self):                                           #creating another method 
		print('run')

player1 = PlayerCharacter('Devon Gifford',28,'married to Belle Delphine')        #we need to actually create/instantiate some objects, using our new PlayerCharacter "data-type"
player2 = PlayerCharacer('Bella Delphine',21,'married to Devon Gifford')

print(player1)
print(player1.name)
print(player1.run)
print(player2.age)

>
```

You will see this when building a classes = you will see this at the top 

- often called a "constructor method" or "__init__ method"

```python
def __init__(self, name, age, maritial_status):        
		self.name = name                                       
```

# Attributes and Methods

OOP allows us to create objects, that have their own `methods` (e.g. run(), count(), etc.) and `attributes` (their own properties)

A way to add more functionality to a language and mimic the real world.

- **Class object attributes** *vs.* **class attributes**
    
    Also could be phrased as:
    
    - static vs dynamic
        
        - meaning that class object attributes are static, 
        - meaning its an attribute of the class, 
        - meaning this will exist for all objects we instantiate, 
        - meaning all instantiated items will have access to it, 
        - meaning does not change across instances.
        
    

```python
class PlayerCharacter:
	#Class Object Attributes
	membership = True
	married = True
	def __init__(self, name, age, maritial_status):
		if (PlayerCharacter.membership):
			self.name = name                                       #attrinute 1
			self.age = age                                         #att
			self.maritial_status = maritial_status                 #
	
	def shout(self):
		print (f'my name is {self.name}') 

	def run(self):
		print('run')
		return('done')

player1 = PlayerCharacter('Devon Gifford',28,'married to Belle Delphine')
player2 = PlayerCharacer('Bella Delphine',21,'married to Devon Gifford')

print(player1)
print(player1.name)
```

- Example/Practice
    
    ```python
    #Given the below class:
    class Cat:
        species = 'mammal'
        def __init__(self, name, age):
            self.name = name
            self.age = age
    
    # 1 Instantiate the Cat object with 3 cats
    
    cat1 = Cat('Tom', 3)
    cat2 = Cat('Garfield', 11)
    cat3 = Cat('Cin', 7)
    my_cat_list = [cat1, cat2, cat3]
    
    print(cat1.name)
    print(cat2.name)
    print(cat3.name)
    
    # 2 Create a function that finds the oldest cat
    
    def oldest_cat(*args):
        return max(args)
    
    # 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
    
    print(f'The oldest cat is {oldest_cat(cat1.age, cat2.age, cat3.age)} years old.')
    
    >
    Tom
    Garfield
    Cin
    The oldest cat is 11 years old.
    ```
    

# __init__

- a constructor function
- called every time we instantiate an object
- how we create custom objects
- The **init** method lets the class initialize the object's attributes and serves no other purpose.
- It is only used within classes

An interesting thing that you can do here, because you have control over how the instantiation happens, you can do different safeguards.

- For example
    
    ```python
    class PlayerCharacter:
    	#Class Object Attributes
    	membership = True
    	married = True
    	def __init__(self, name = 'anonyous', age'0, maritial_status = True):
    		if (age>18):
    			self.name = name                                       #attrinute 1
    			self.age = age                                         #att
    			self.maritial_status = maritial_status                 #
    	
    	def shout(self):
    		print (f'my name is {self.name}') 
    
    	def run(self):
    		print('run')
    		return('done')
    
    player1 = PlayerCharacter('Marc',10)  
    > #Result in error 
    
    ```
    

# @classmethod & @staticmethod

<aside>
📹 The @classmethod decorator is **used to declare a method in the class as a class method that can be called using 
`ClassName.MethodName()**.` 

The class method can also be called using an object of the class. 

The @classmethod is an alternative of the classmethod() function.

</aside>

<aside>
💭 95% of classes dont use class methods but need to know

</aside>

- `@classmethod`
    - uses a *‘decorator’* - we will learn more about what this is later on
    - using this decorator we can create a function
    - creating a method we can use
    
    okay so what I understand this is as;
    This is how we can create a “Class Object Attribute”
    
    <aside>
    🤔 hey look at that!
    the `cls` kind of work the same way that the `self` was working when we were learning about creating classes 
    - `cls` is unique to the `@classmethods`
    
    </aside>
    
    - example
        
        ```python
        class PlayerCharacter:
        	married = True
        	def __init__(self, name, age, maritial_status):
        		if (PlayerCharacter.membership):
        			self.name = name                                       
        			self.age = age                                         
        			self.maritial_status = maritial_status        
        
        		@classmethod 
        		def adding_things (cls, num1, num2)
        		return num1 + num2
        ```
        
        <aside>
        ❗ Look out for the `cls`
        `CLS` = Class
        
        </aside>
        
    - We can use the `cls` to instantiate an object in here
        
        <aside>
        💭 this could one day be useful, and helps us understand difference between `@staticmethod` & `@classmethod`
        
        </aside>
        
        for example 
        
        ```python
        class PlayerCharacter:
        	married = True
        	def __init__(self, name, age, maritial_status):
        		if (PlayerCharacter.membership):
        			self.name = name                                       
        			self.age = age                                         
        			self.maritial_status = maritial_status        
        
        	@classmethod 
        	def adding_things (cls, num1, num2)
        	return cls('DIS DA QUICK MATH', num1 + num2
        
        player3 = PlayerCharacter.adding_things(2,3)
        print(player3.adding_things
        ```
        
    
    ---
    
- `@staticmethod`
    
    Works exact same way, however do not haves access to the cls (class)
    
    looks like this:
    
    ```python
    class PlayerCharacter:
    	married = True
    	def __init__(self, name, age, maritial_status):
    		if (PlayerCharacter.membership):
    			self.name = name                                       
    			self.age = age                                         
    			self.maritial_status = maritial_status        
    
    	@staticmethod 
    	def adding_things (cls, num1, num2)
    	return cls('DIS DA QUICK MATH', num1 + num2
    
    player3 = PlayerCharacter.adding_things(2,3)
    print(player3.adding_things
    ```
    
    only difference between the two:
    
    - don’t have access in the parameter to the cls
    - would use when we don’t care about the class state or the attributes
    - we use class state when we do care and want to maybe modify them

---

# recap

- OOP is a paradigm (mindset) - a way for us to think about structuring our code
- Classical OOP = using classes

In python can create a class with the `class` keyword

Using this naming convention:

- Capital Letters
- CamelCode

(this tells other devs, this is a class that needs to be instantiated)

we learned about the following topics:

- class object attributes
- how to instantiate an object
- `__**init__**` functions - runs on every instantiation to customise
- how to add methods to our class, so each object has access to these methods
- `@classmethods` & `@staticmethods` - methods that can be called on without having to instantiate

thats pretty much it (there is alot more but this is the fundamentals) this is going to take practice 

# Fundamentals: Testing Your Own Assumptions

<aside>
🗣 A little useless but need to hear it

</aside>

---

Make sure you test if you know what you know. 

Make sure you test yourself on every bit of new code you learn. 

Test your understanding and your assumptions.  

Explore the code 

for example 
if you learn about the `self` when learning about creating a  `class`

explore find out what happens if you try x and y
see if you have a question 

ask what do you think will happen, then see what actually happens and understand why

Don’t take the word of an instructor, test it yourself - this is a skill for programming not learning or life.  

Thus, if you don’t do this you wont understand

---

<aside>
🤔 **4 things that OOP - ‘*object oriented programming’* does really well.**

- Encapsulation
- Abstraction
- Inheritance
- Polymorphism
</aside>

# Encapsulation

we've actually learned the first one, and that is the idea of encapsulation.

- What is encapsulation?
    
    > Encapsulation is the binding of data & functions that manipulate that data.
    > 
    > 
    > And we encapsulate into one big object, so that we keep everything in this box that users or code or other machines can interact with.  This data and functions are what we call attributes and methods.
    > 
    > Therefore, 
    > We're able to encapsulate the functionality of our player character by having name and age data or attributes and also have functions that can act upon this name and age.
    > 
    
    For example
    
    ```python
    def speak (self):
    	print(f'my name is {self.name}, and I am {self.age} years old')
    ```
    
    I have encapsulated this functionality to the, `object` and then now the  `.speak()` function 
    
    - Why do we want to package data and functions into attributes and methods?
        
        Gives us extra power
        
        Without the actions, methods and attributes - its the same thing as a dictionary
        

# Abstraction

- What is abstraction?
    
    > means hiding of information or abstracting away information and giving access to only what's necessary.
    > 
    > 
    > Therefore,
    > whatever the user or the programmer or the machine is interested in, that's the only thing we give access to everything else.
    > 
    > We kind of hide it in a blanket underneath the hood because our users don't have to worry about it.
    > 

For example

```python
player1 = PllayerCharacter('Devon',28)
player1.speak()
#this is abstraction happening live!
```

I don’t care how speak is implemented, all I know is that player 1 has access and can invoke it.   Therefore we are using ‘abstraction’

This is the power and efficiency of OOP

Another example, 

if we are building an app we don’t need to code the camera functionality to use the camera in our app.  We can call on the functionality e.g. `camera.takepicture()`

<aside>
🤔 **I think I understand**

but there are cons….or risks….
Check out the next section:  Private vs Public Variables

</aside>

### Private vs Public Variables

We made a mistake,  here

```python
class PlayerCharacter:
	
	membership = True
	married = True
	def __init__(self, name, age, maritial_status):
		if (PlayerCharacter.membership):
			self.name = name                                      
			self.age = age                                         
			self.maritial_status = maritial_status                 
	
	def speak(self):
		print (f'my name is {self.name}, and I am {self.age} years old.') 

player1 = PlayerCharacter('Devon', 28)
player1.name = "King Devon"
player1.speak = "I FORKED UP"

print(plaer1.speak)
>
I FORKED UP
```

- we overwrote our class…
    
    if we instantiate a ‘new character’,  we will have access as normal
    
    However for ‘player 1’ , things are broken….
    
    This is bad and has to be recoded…
    
    We should have used private variables….
    

- What are Private variables
    
    Well a private variable would be a variable we wouldnt have access to view or access to edit
    
    not all programming languages have access to this, for example Python
    
    (Java has it built in)
    

- So what can we do to get around this?
    
    we would use an underscore 
    
    this is a rule of thumb among us python programmers
    
    not a double underscore - that’s a dunder, and is something else 
    
    ```python
    	membership = True
    	married = True
    	def __init__(self, name, age, maritial_status):
    		if (PlayerCharacter.membership):
    			self._name = name                                      
    			self._age = age             
    ```
    

# Inheritance

- What is inheritance?
    
    > inheritance allows new objects to take on the properties of existing objects.
    > 
    > 
    > So you can inherit classes.
    > 
    
    For example
    
    ```python
    class User():
    	def sign_in(self):                      #we do not need an __initi__ here, as we have no attributes
    		print('logged in')
    
    class Wizard(User):
    	def __init__(self, name, power):
    		self.name = name
    		self.power = power
    
    	def attack(self):
    		print(f'attacking with a giant mega-blast of {self.power}')
    
    class Archer(User):
    	def __init__(self, name, num_arrows):
    		self.name = name
    		self.num_arrows = num_arrows
    
    	def attack(self):
    		print(f'attacking with a true-arrow, straight to the enemies heart:  arrows left {self.num_arrows}')
    
    Wizard1 = Wizard('Merlin', 'fire')
    Archer1 = Archer('Robin Hood', 12)
    
    Wizard1.attack()
    Archer1.attack()
    ```
    
    So, inheriting functionality is the name of the game here 
        meaning, the wizard and Archer class have unique functions/methods that can be called but the can both call on the ‘user class’ for the sign in.
             i.e.   -  they have inherited that function/method from the ‘parent class’.
    
    <aside>
    📢 the children class is sometime knows as;  **sub-classes** or **derived-classes**
    
    </aside>
    
    Inheritance is applicable with methods and functions too..
    
    - `Isinnstance`
        - built in function
        
        ```python
        print(isinstance(Wizard1, Wizard))
        print(isinstance(Wizard1, User))
        print(isinstance(Wizard1, object))
        >
        True 
        True
        True
        
        ```
        

# Polymorphism

*Poly = many + Morphism = form   - ‘manyforms’*

We know that methods belong to objects.  We use the self keyword to act upon the object that got instantiated.

- What is polymorphism?
    
    > refers to the way in which object classes can share the same method name but those method names can act differently based on what object calls them.
    > 
    
    For example
    
    ```python
    class User(object):
        def sign_in(self):
            pass
    
    class Wizard(User):
        def __init__(self,name,power):
            self.name = name
            self.power = power
    #method called attack
        def attack(self):
            print(f'atacking with power of {self.power} now!')
    
    class Archer(User):
        def __init__(self, name, num_arrows):
            self.name = name
            self.num_arrows = num_arrows
    #method called attack
        def attack(self):
            print (f'attacking with arrows now:  Phweep - it was a hit!\narrows remaing: {self.num_arrows}.')
    
    wizard1 = Wizard('Harry', 60)
    archer1 = Archer('Robin', 25)
    #same method names....
    wizard1.attack()
    archer1.attack()
    #different outputs, because of different objects - this is polymorphism 
    >
    atacking with power of 60 now!
    attacking with arrows now:  Phweep - it was a hit!
    arrows remaing: 25.
    
    #another example
    for party in [wizard1, archer1]:
    	party.attack()
    >
    atacking with power of 60 now!
    attacking with arrows now:  Phweep - it was a hit!
    arrows remaing: 25.
    
    ```
    
    - So polymorphism allows us to have many forms.
    - It is the ability to redefine methods for these derived classes that is Wizard and Archer.
    - An object that gets instantiated can behave in different forms in different ways based on polymorphism.
    - This is useful because we are able to modify our classes to our specific needs but also not have to repeat ourselves in case we want to use something.
    
    <aside>
    🤔 no one is going to teach you exactly when to use what.
    However, the idea here is to understand that these powers exist with OP.
    
    </aside>
    
    - Exercise
        
        ```python
        class Pets():
            animals = []
            def __init__(self, animals):
                self.animals = animals
        
            def walk(self):
                for animal in self.animals:
                    print(animal.walk())
        
        class Cat():
            is_lazy = True
        
            def __init__(self, name, age):
                self.name = name
                self.age = age
        
            def walk(self):
                return f'{self.name} is just walking around'
        
        class Simon(Cat):
            def sing(self, sounds):
                return f'{sounds}'
        
        class Sally(Cat):
            def sing(self, sounds):
                return f'{sounds}'
        
        #1 Add nother Cat
        class Garfield(Cat):
            def sing(self, sounds):
                return f'{sounds}'
        
        #2 Create a list of all of the pets (create 3 cat instances from the above)
        my_cats = [Simon("Stronk Simon",5), Sally("Silly Sally", 2), Garfield("Lazy Garfield", 7)]
        
        #3 Instantiate the Pet class with all your cats use variable my_pets
        my_pets = Pets(my_cats)
        
        #4 Output all of the cats walking using the my_pets instance
        print(my_pets.walk())
        
        >
        Stronk Simon is just walking around
        Silly Sally is just walking around
        Lazy Garfield is just walking around
        None
        
        ```
        

---

# `super()`

- What is `super()`
    
    **`super()`** is a special function in Python that refers to the base class *(aka, as the parent class)* of the current class. 
    
    It is often used in the body of a class method to call a method defined in the base class.
    
- Here is an example of how **`super()`** can be used in a class method:
    
    ```python
    class User():
    	'''
    	Info:  This is a class that all characters in the game will have. The parent class
    	'''
    	def __init__(self, email):
    		self.email = email
    
    	def sign_in():                      
    		print('logged in')
    	
    
    class Wizard(User):                                                 
    	def __init__(self, name, power, email):
    		User.__init__(self, email)                                       #This is one way of doing it - using the User
    		self.name = name
    		self.power = power
    
    	def attack(self):
    		print(f'attacking with a giant mega-blast of {self.power}')
    
    class Archer(User):
    	def __init__(self, name, num_arrows, email):                          
    		super().__init__(email)                                          #This is a new way of doing it using the super() function
    		self.name = name
    		self.num_arrows = num_arrows
    
    	def attack(self):
    		print(f'attacking with a true-arrow, straight to the enemies heart:  arrows left {self.num_arrows}')
    
    Wizard1 = Wizard('Merlin', 'fire', 'merlin@gmail.com')
    Archer1 = Archer('Robin Hood', 12, 'r.hood@gmai.com')
    
    print(Wizard1.email)
    print(Archer1.email)
    
    <
    merlin@gmail.com
    r.hood@gmai.com
    ```
    
    ```python
    #Here is an example from ChatGPT-3
    
    class Shape:
        def __init__(self, sides):
            self.sides = sides
    
    class Triangle(Shape):
        def __init__(self, sides, height):
            # Call the __init__ method of the base class (Shape)
            super().__init__(sides)
            self.height = height
    ```
    
    <aside>
    ❗ It is important to note that **`super()`** only works correctly if it is called from a method defined in a subclass. If it is called from a method defined in the base class, it will not reference the base class as expected.
    
    </aside>
    
    If the above is the case, you can simply use the name of the base class followed by the method name.
    
    - For example:
        
        ```python
        class Shape:
            def draw(self):
                print("Drawing a shape")
        
        class Triangle(Shape):
            def draw(self):
                # Call the draw method of the base class (Shape)
                Shape.draw(self)
                print("Drawing a triangle")
        
        triangle = Triangle()
        triangle.draw()
        ```
        

<aside>
❗ It is important to note that this method of calling the base class method will work regardless of whether the method is called from a method in the base class or a method in a derived class. However, using **`super()`**  is generally preferred, as it is more concise and easier to read.

</aside>

# Object Introspection

<aside>
🤔

</aside>

- What is introspection in computer programming?
    
    > the ability to determine the type of an object at runtime.  (*run-time = when the code is running)*
    During that time you can determine the type of an object.
    
    Therefore because everything in python is an object we can ‘introspect’ an object & actually figure out what our code does
    Python allows us to do introspection with some nice helper functions.
    > 

For example:   using the `dir`

```python
class User(object):
    pass

class Wizard(User):
    def __init__(self,name,power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'atacking with power of {self.power} now!')

# introspection
wizard1 = Wizard('Harry', 2)
print(dir(wizard1))

>
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'attack', 'name', 'power']
```

This is known as introspection, and it is a useful tool for debugging and understanding the structure of objects in your code.

# Dunder Methods

<aside>
🤔 In Python, "dunder" (short for "double underscore") methods are special methods that have a name with two underscores on either side. 

These methods are used to define the behaviour of certain operations in Python, such as; 
*- object creation, 
- destruction, 
- operator overloading, 
- and string representation.*

</aside>

- Here are some common dunder methods in Python
    
    <aside>
    🗣 Important to note here
    There are many many dunder methods.  Just need to understand they exist.
    
    </aside>
    
    - **`__init__`**: This method is called when an object is created, and is used to initialize the attributes of the object.
    - **`__str__`**: This method is called when the **`str()`** function is applied to an object, and is used to return a string representation of the object.
    - **`__len__`**: This method is called when the **`len()`** function is applied to an object, and is used to return the length of the object.
    - **`__add__`**: This method is called when the **`+`** operator is applied to two objects, and is used to define how the objects should be added together.
    - **`__eq__`**: This method is called when the **`==`** operator is applied to two objects, and is used to define how the objects should be compared for equality.
- Here is an example of how dunder methods can be used in a class:
    
    <aside>
    🗣 Look at this!
    
    In this example, the `Point` class defines four dunder methods: **`init`**, **`str`**, **`len`**, and **`eq`**. 
    
    These methods allow the `Point` class to be initialized with a pair of coordinates, converted to a string representation, measured for length, and compared for equality, respectively.
    
    </aside>
    
    ```python
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y
    
        def __str__(self):
            return f'Point ({self.x}, {self.y})'
    
        def __len__(self):
            return 2
    
        def __add__(self, other):
            return Point(self.x + other.x, self.y + other.y)
    
        def __eq__(self, other):
            return self.x == other.x and self.y == other.y
    
    p1 = Point(1, 2)
    p2 = Point(3, 4)
    
    print(str(p1)) # prints "Point (1, 2)"
    print(len(p1)) # prints 2
    print(p1 + p2) # prints "Point (4, 6)"
    print(p1 == p2) # prints False
    ```
    

---

- 📹 Here is notes from the video 📽️
    
    [3. Data model](https://docs.python.org/3/reference/datamodel.html#special-method-names)
    

```python
class Toy():
	def __init__(self, color, age):
		self.color = color
		self.age = age
		self.my_dict = {
			"name":"Devon",
			"has_pets": False
		}
																															#Normally we never change a dunder method 
	def __str__(self):
		return f'{self.color}'

	def __len__(self):
		return 5

	def __call__(self):
		return ('Yes sir?')

	def __getitem__(self, i):
		return self.my_dict[i]

action_figure = Toy('Red', 0)                               #Here we instantiate our object. 

print(action_figure.__str__())                              #Here we are testing all the dunders we created/edited
print(len(action_figure))
print(str('action_figure'))
print(action_figure())
print(action_figure['name'])
print(action_figure['has_pets'])

>
Red
Red
action figure
Yes sir?
Devon
False
```

- Exercise
    
    ```python
    class SuperList(list):   #Code that allows us to use all our list methods 
    	
    	def __len__(self):   #Special dunder method, where __len__ will always return 1000
    		return 1000
    
    super_list1 = SuperList()
    
    len(super_list1)
    super_list1.append(5)
    print(super_list1[0])
    print(issubclass(list, object))
    
    >
    5
    True
    ```
    

# Multiple Inheritance

<aside>
🤔 In Python, multiple inheritance refers to the ability of a class to inherit attributes and methods from multiple base classes. This allows a derived class to inherit the characteristics of multiple base classes, and can be a powerful tool for code reuse and organization.

</aside>

<aside>
🗣 Some Programming Languages do not allow multiple inheritance - as can easily fuck things up if you don’t understand very well and things get complex.

</aside>

- Here is an example of how multiple inheritance can be used in Python:
    
    ```python
    class User():
        '''
        Info:  This is a class that all characters in the game will have. The parent class
        '''
        def sign_in():                      
            print('logged in')
        
    
    class Wizard(User):                                                 
        def __init__(self, name, power):                                       
            self.name = name
            self.power = power
    
        def attack(self):
            print(f'attacking with a giant mega-blast of {self.power}')
    
    class Archer(User):
        def __init__(self, name, num_arrows):                                                                
            self.name = name
            self.num_arrows = num_arrows
    
        def attack(self):
            print(f'attacking with a true-arrow, straight to the enemies heart:  arrows left {self.num_arrows}')
    
        def run(self):
            print('Ran with the wind in his favour')
    
    class HybridBorg(Wizard, Archer):                          #This class is inheriting both the functionality from Archer & Wizard
        def __init__(self, name, power, num_arrows):
            Archer.__init__(self, name, num_arrows)
            Wizard.__init__(self, name, power)
    
    HybridBorg1 = HybridBorg('Hanzo', 33, 100)
    
    print(HybridBorg1.run())
    ```
    
    > In this example, the `HybridBorg` class is derived from both the `Archer` and **`Wizards`** classes, which are themselves derived from the **`User`** class.
    > 

It is important to note that multiple inheritance can lead to complexity in your code, as it can be difficult to determine the order in which attributes and methods are inherited. It is generally recommended to use multiple inheritance sparingly, and to carefully consider whether it is the best design choice for your code.

So with great power comes great responsibility - be warned brother

---

# MRO  - Method Resolution Order

<aside>
❗ In Python, the Method Resolution Order (MRO) is the order in which the base classes of a class are searched for methods and attributes.

</aside>

- The MRO of a class can be accessed using the **`__mro__`** attribute, and is represented as a tuple of the base classes in the order they will be searched.
- This order is determined by the class hierarchy
- Used to resolve conflicts when a class inherits from multiple base classes that define the same method or attribute.

---

- For example:
    
    ```python
    class A:
        pass
    
    class B(A):
        pass
    
    class C(A):
        num = 1
    
    class D(B, C):
        pass
    
    print(D.__mro__) # prints 
    >
    (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
    ```
    
    > In this example, the MRO of the **`D`** class is **`(D, B, C, A, object)`**, which means that when a method or attribute is accessed on a **`D`** object, it will first look for the method or attribute in the **`D`** class, then in the **`B`** class, then in the **`C`** class, then in the **`A`** class, and finally in the **`object`** class.
    > 
    
    > It is important to note that the MRO is determined using a specific algorithm known as the C3 linearization algorithm, which ensures that the MRO is a valid linearization of the class hierarchy. This algorithm is used to avoid the "diamond problem", which occurs when multiple inheritance leads to ambiguous inheritance relationships.  ******see below figure for diamond problem visualized******
    > 
    
    ![Untitled](Objective%20Oriented%20Programming%209e58d0d0f0e244809759bc92fd44ed58/Untitled.png)