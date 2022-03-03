# Python Basics I

Actual: 6 hours
ETA: 4 hours
Reviewed: No
Section: Section 3
Summary: No
Type: Lecture, Notes
complete: Done

- Table of Contents

## Brief Introduction

- **4 things you need to learn with every programming language**
    - 1.  Terms
        
        - different words, definitions that you need to memorise (statements, variables etc.)
        
    - 2.  Data Types
        
         -  what data can a program hold?  what values/data types
        
    - 3.  Actions
        
         - store this data, recall this data and do this with that data
        
    - 4. Best practices
        
         - there are good ways and bad ways
        

## Python Data Types - *8 types + co.*

| Name | Type  | Description | example | Mutable? |
| --- | --- | --- | --- | --- |
| Integers | int | Whole numbers | 3, 300, 200 | ❌ |
| Floating points | float | Numbers with a decimal point | 2.6 or 100.00 | ❌ |
| Strings | str | Ordered sequence of characters, | ‘sammy’ or ‘$%3’ | ❌ |
| Lists | list | Ordered sequence of objects. | [10, “hello”, 200.3] | ✅ |
| Dictionaries | dict | Unordered key : Value pairs | {“mkey”:“value”:“name”:“Frank”} | ✅ |
| Tuples | tup | Ordered immutable sequence of objects | (10,”hello”,200.3) | ❌ |
| Sets | set | Unordered collection of unique objects | {“a”,”b”} | ✅ |
| Booleans | bool | Logical value indicating True or False | True or False | ❌ |
|  |  |  |  |  |

OTHER TYPES: 

- **Classes** - custom types
- **specialized data types** - modules (extensions we can add)
- **None** (means nothing, the absence of value)
- ****************complex**************** (don’t worry about it for now)

- Complex (used for complex math - we will probably never be used)

## Integers & Floating points

```python
print (2 ** 3) #means two to the power of 3 = 
print (5 // 4)  #returns an integer rounded down to an integer 
print (6 % 4)  #modulo - remainder of the division 
```

```python
# math functions

print 
type 
round 
abs returns the absolute value (i.e. no negatives)
bin returns the binary representation 
```

<aside>
☝️ First: **Developer Fundamental**

“Don’t read the dictionary” 
meaning that we do not need to memorise everything, google is our friend. 

</aside>

<aside>
☝️ **Operator precedence**
Different operators have precedence over others - basically meaning BODMAS

</aside>

## **Variables**

- What are variables?
    
    *A way to, 
    - store data on our computer* 
    - assigning ‘data’ to a ‘name’ 
    
- **Variables are also known as:**
    
    binding to a value or a ‘binding’ 
    
    🔦 Sometimes are called ‘names’ or ‘variable name’
    

- **Best practices for variables :**
    - snake_case
    - start with lowercase or underscore
    - Letters numbers keywords
    - Case sensitive
    - Don’t overwrite keywords
    - make it readable & understandable

<aside>
⚠️ Be careful of 
**constants** 
We put them all in capitals if you have something you never want them to change 

**double__underscore aka dunder**
Do not do this -will learn about this later

</aside>

**Here is a quick way to create variable names and data**

- ***********see example***********
    
    ```python
    a,b,c = 1,2,3
    print(a)
    print(b)
    print(c)
    
    	1
    	2
    	3
    ```
    

## Expressions & Statements

---

- Statement
    
    iq = 100
    user_age = iq / 5
    
    The whole thing is the statement 
    
- Expression
    
    user age = iq / 5
    expression
    
    The part after the variable name is the expression
    

## Augmented assignment operator

```python
some_value = 5
some_value = some_value + 2

print(some_value)
7

#instead of doing something like that, we can do this for short hand
some_value = 5
some_value += 2

print(some_value)

7
```

## Strings

---

### concatenation

- string concatenation = combining strings

```python
#creating strings with 'x' & "x" & '''x'''
username = "test"
password = 'test two'
long_string = '''
wow look at this

this is a string "this is so weird" she said why
'''
```

### Escape Sequence

This allows us to have special commands in our strings, or to tell the interpreter that this is part of the string.

```python
weather= "It's "kind of" cold"
#well that doesn't work, so we can do this 
weather = "It\'s \"kind of\" sunny"
#This is how we tell python whatever comesafter this is a string

#\t =  this will tell python to insert a tab
#\n =  this will tell python to start on a new line
```

### Formatted strings

Often you want to ‘inject’ a variable into your string for printing - known as string interpolation

**Two methods:**

1. **.format method**

have your string defined then use { } brackets  

`print (‘This is a string { } .format (‘INSERTED’))`

*`print ('The {2} {1} {0}'.format('fox','brown','quick'))`*

*`print('The {q} {b} {f}'.format(f='fox',b='brown',q='quick'))`*

*= The quick brown fox*  

**Float formatting with the .format method** 

Float formatting follows “{value : width . precision f}” value width = white space precision = number of digits to print

Used to change the level of precision and the width of the numbers

1. **F-strings method (recommended)**
    
    Several benefits over .format method
    Also known as, ‘an f-string’.
    
    *`name = "Jose"
    print(f'Hello, his name is {name}')`*
    
    Hello, his name is Jose
    

```python
name = 'Devon'
age = 27

#Normal stringmay look like this:

print ('hi ' + name + '.  You are ' + str(age) + ' years old.')

#Formatted strings - python3 (the little f tells python this is a formatteds string

print (f'hi {name}.  You are {age} years old.')

#In python 2 and older - we had to use .format

print ('hi {0}.  You are {1} years old.'.format(name, age))
```

### String Indexes

Sequence of characters using the syntax of either single quotes or double quotes

*Having both option of quotes, we can use single quotes inside of double quotes *e.g don’t or I’m*

The actions use [ square brackets ] and  a number index to indicate positions of what you wish to grab

Character                   h        e          l          l         o     
Index                         0        1         2         3          4
Reverse Index            0       -4       -3       -2          -1       

```python
#we can index through the shelf (NB starts at 0)
Devon 
01234

name = Devon
print(name)
Devon

name = Devon
print(name[0:5:2])
Dvn

#aka as slicing
[start : stop : skip]
```

### Immutability

- Strings are immutable (cannot be sliced or changed)
- We have to create a new string

### Built-in Functions + Methods

```python
FUNCTIONS
str()
int()
len() # counts like humans do, meaning starts counting from 1 

METHODS
Python stirng methods

.format{}

quote = 'to be or not to be'

print = (quote.upper())
print = (quote.capatallze())
print = (quote.find('be'))
print = (quote.replace('be','me'))

#remember you are not creating new strings (they are immutable)
quote = print = (quote.replace('be','me'))

```

[https://docs.python.org/3/library/functions.html](https://docs.python.org/3/library/functions.html)

---

<aside>
☝️ **Type conversion**

you can convert strings to **int** or **float** or whatever, just something to know 

</aside>

## Booleans

- Can only be True or False
- 1 is True
- 0 is False
- Booleans are operators that allow you to convey True or False statements Important for control flow & logic

Important that you use capital F and T - wont work with lower case

`Booleans type = bool`

```python
names = Devon
is_cool = False

is_cool = True 

```

## List’s

### Introduction / Overview

- Lists are ordered sequences that can hold a variety of object types
- They use brackets and commas to separate objects in the list. [1,2,3,4,5]
- Lists support indexing and slicing. Lists can be nested and also have a variety of useful methods that can be called oof of them

(Arrays)(Data Type)

<aside>
☝️ Data Structure

A way for us to organise and store data 
(pros & cons of accessing different data structure)

</aside>

- Can use strings, integers, Booleans
- uses [ ] - *square brackets*
- lists are mutable - *meaning that they can be amended and changed*
- modifying vs copying lists - an important concept to keep in mind (see below)

---

### List Slicing

- Can use list slicing
- lists are mutable - *meaning that they can be amended and changed*

```python
#List Slicing
amazon_cart = [
'notebook',
'chair',
'pen',
'calander'
]

amazon_cart[0] = 'daily planner'
	print(amazon_cart[0])

> daily planner
```

### Creating a copy with ‘list slicing’

```python
#Creating a copy with List Slicing
amazon_cart = [
'notebook',
'chair',
'pen',
'calander'
]

amazon_cart[0] = 'daily planner'
new_cart = amazon_cart [:]  #This creates a copy
new_cart = amazon_cart      #This turns this list into the first list.
```

### Matrix

An array with another array inside of them (or an array within an array, in array, in array
This is a way how computers kind of create images on screens

```python
Matrix = [
[1,2,3],
[2,4,6],
[7,8,9]
]

print(matrix[0][[1])
>2
```

### List Methods

- Some methods
    - put items at the start of a list
        
        `newlist[0]='One'`
        
    - Put items at the end of the list
        
        `newlist.append('six')`
        
    - Take items off at the end of the list
        
        `newlist.pop()`
        
    - How do I remove something from the middle
        
        `newlist.pop(2)`
        
- Some more methods
    
    ```python
    basket = 1,2,3,4,5
    
    #adding
    new_basket = basket.append(100)
    
    #insert
    #modifies the list 
    new_basket = basket.insert(4,100)
    
    #extend
    #adds thins to the end of the list
    new_basket = basket.insert([100])
    
    #pop
    basket.pop()          #removes whatever is at the end of the list
    basket.pop(0)         #removes whatever is at that index
    
    #removing
    basket.remove(5)      #removes the '5' from the list - removes the value
    
    #clear
    basket.clear()        #removes everything from the list
    ```
    
    - Sort and reverse
        - `newlist.sort() numlist.reverse()`
    
    ![Untitled](Python%20Basics%20I%2035d88854efd94a79919c1f4e1e5702e1/Untitled.png)
    
    ![Untitled](Python%20Basics%20I%2035d88854efd94a79919c1f4e1e5702e1/Untitled%201.png)
    
- Even more methods
    
    ```python
    basket.index(2)                        #this will show you what index this (x) is at
    	basket.index('d',0,2)                #this will start looking for (d) within the paramaters of the 0,2 index)
    
    	print('x' in basket) 
    	>True
    
    basket.count('a')                     #counts how many times (x) shows up in the list
    
    basket.sort()                         #sorts the list alphabetically (does not amend the array)
    (sorted(basket))                      #sorts the basket and creates a new array
    
    new_list = basket.copy                #creates a copy
    
    basket.reverse()                      #show the list in reverse
    ```
    

### Common List Patters

```python
#Reverse with slicing
print(basket[::-1]  #this creates a new array

#Generate a list quickly using 'Range'
print(list(range(1,100)))
> [1,2,3...,99]

#join strings and lists together to make a sentences 
new_sentence = ' '.join(['hi','my','name','is','Devon')
print(new_sentence)
hi my name is Devon  #This put my ' ' inbetween every item in the list
```

### List Unpacking

```python
#list unpacking 
#what if we wanted to assaign a variable to each item in the list

a,b,c *any_variable_name_we_want = [1,2,3,4,5,6,7,8,9]
	print(any_variable_name_we_wante)
	> [4,5,6,7,8,9]

a,b,c *the_remaining_other, d = [1,2,3,4,5,6,7,8,9]

print(a)
print(b)
print(c)
print(other)
print(d)

1
2
3
[4,5,6,7,8]
9
```

![Untitled](Python%20Basics%20I%2035d88854efd94a79919c1f4e1e5702e1/Untitled%202.png)

![Untitled](Python%20Basics%20I%2035d88854efd94a79919c1f4e1e5702e1/Untitled%203.png)

### Select an object from in a list in a list

If there is a list within a list, for example:                                                          `list = [1,2,[3,4,’hello’]]`

and you want to grab something from the list in the lilst, for example:            `‘hello’`

run a script calling that list and what you want from that list:                          `list[2][2] or list [2][-1]`

---

## Type conversion List’s

![Untitled](Python%20Basics%20I%2035d88854efd94a79919c1f4e1e5702e1/Untitled%204.png)

![Untitled](Python%20Basics%20I%2035d88854efd94a79919c1f4e1e5702e1/Untitled%205.png)

<aside>
☝️ Developer Fundamentals
#this is how I comment in python
#it’s really good to add valuable comments in your code
- Only add comments when you need too
- More comments are not always useful

</aside>

Secret Password exercise

![Untitled](Python%20Basics%20I%2035d88854efd94a79919c1f4e1e5702e1/Untitled%206.png)

![Untitled](Python%20Basics%20I%2035d88854efd94a79919c1f4e1e5702e1/Untitled%207.png)

### None

We have seen this in the output sometimes  (a.k.a as null in other languages)

Sometimes it can be useful 

```python
weapons = None  
```

---

💡 Some people use ‘NONE’ in a cell as a place holder

## Dictionaries

### Overview

- The key-value pair allows users to quickly grab objects without needing to know an index location.
- Dictionaries use { } and : to signify the keys and their associated values. 
`{ ‘key1’ : ’value1’ , ‘key2’ : ‘value2’ }`
- **Dictionaries characteristics:**
    - Uses curly brackets {}
    - Has a ‘key’ : ‘value’
    - Unordered key value pair
    - Dictionary keys are always immutable
    - Dictionary keys have to be unique (or else they will get be overwritten)

```python
#Print the "brand" value of the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
```

<aside>
💡 As of Python version 3.7, dictionaries are ***ordered***. In Python 3.6 and earlier, dictionaries are ***unordered***

When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
Unordered means that the items does not have a defined order, you cannot refer to an item by using an index.

</aside>

### Dictionary Items

Dictionary items are ordered, changeable, and does not allow duplicates.

Dictionary items are presented in ‘*key : value’* pairs, and can be referred to by using the key name.

- Ordered or Unordered?
    
    As of Python version 3.7, dictionaries are *ordered*. In Python 3.6 and earlier, dictionaries are *unordered*.
    
    When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
    
    Unordered means that the items does not have a defined order, you cannot refer to an item by using an index.
    
- Changeable
    
    Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
    
- Duplicate Not Allowed
    
    Dictionaries cannot have two items with the same key:
    
    Duplicate values will overwrite existing values:
    

---

- Dictionary Data Types
    
    The values in dictionary items can be of any data type:
    
- The dict() contructor
    
    It is also possible to use the dict() constructor to make a dictionary.
    

---

### Access Items

You can access the items of a dictionary by referring to its key name, inside square brackets:

💡 There is also a method called `get()` that will give you the same result:

```python
#Get the value of the "model" key:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

#Get the value of the "model" key:
x = thisdict.get("model")
```

- Get Keys
    
    The `keys()` method will return a list of all the keys in the dictionary.
    The list of the keys is a *view* of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.
    
    ```python
    #Get a list of the keys:
    
    x = thisdict.keys()
    
    #Add a new item to the original dictionary, and see that the keys list gets updated as well:
    car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    
    x = car.keys()
    
    print(x) #before the change
    
    car["color"] = "white"
    
    print(x) #after the change
    ```
    
- Get Values
    
    The `values()` method will return a list of all the values in the dictionary.
    
    The list of the values is a *view* of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list.
    
    ```python
    #Get a list of the values:
    x = thisdict.values()
    
    #Make a change in the original dictionary, and see that the values list gets updated as well:
    car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    
    x = car.values()
    
    print(x) #before the change
    
    car["year"] = 2020
    
    print(x) #after the change
    
    #Add a new item to the original dictionary, and see that the values list gets updated as well:
    
    car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    
    x = car.values()
    
    print(x) #before the change
    
    car["color"] = "red"
    
    print(x) #after the change
    ```
    
- Get Items
    
    The `items()` method will return each item in a dictionary, as tuples in a list.
    
    ```python
    #Get a list of the key:value pairs
    
    x = thisdict.items()
    
    #The returned list is a view of the items of the dictionary, meaning that any changes done to the dictionary will be reflected in the items list.
    #Make a change in the original dictionary, and see that the items list gets updated as well:
    
    car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    
    x = car.items()
    
    print(x) #before the change
    
    car["year"] = 2020
    
    print(x) #after the change
    
    #Add a new item to the original dictionary, and see that the items list gets updated as well:
    
    car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    
    x = car.items()
    
    print(x) #before the change
    
    car["color"] = "red"
    
    print(x) #after the change
    ```
    
- Check if key exists
    
    To determine if a specified key is present in a dictionary use the `in` keyword:
    
    ```python
    #Check if "model" is present in the dictionary:
    
    thisdict = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
    }
    if "model" in thisdict:
      print("Yes, 'model' is one of the keys in the thisdict dictionary")
    ```
    

### Change Items

- Change Values
    
    You can change the value of a specific item by referring to its key name:
    
    ```python
    #Change the "year" to 2018:
    
    thisdict = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
    }
    thisdict["year"] = 2018
    ```
    
- Update Dictionary
    
    The `update()` method will update the dictionary with the items from the given argument.
    
    The argument must be a dictionary, or an iterable object with key:value pairs.
    
    ```python
    #Update the "year" of the car by using the update() method:
    
    thisdict = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
    }
    thisdict.update({"year": 2020})
    ```
    

### Add & Remove Items

- Add
    
    Adding an item to the dictionary is done by using a new index key and assigning a value to it:
    
    ```python
    thisdict = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
    }
    thisdict["color"] = "red"
    print(thisdict)
    ```
    
    - Update Dictionary
        
        The `update()` method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.
        
        The argument must be a dictionary, or an iterable object with key:value pairs
        
        ```python
        Add a color item to the dictionary by using the update() method:
        
        thisdict = {
          "brand": "Ford",
          "model": "Mustang",
          "year": 1964
        }
        thisdict.update({"color": "red"})
        ```
        
- Remove
    
    There are several methods to remove items from a dictionary:
    
    ```python
    The pop() method removes the item with the specified key name:
    
    thisdict = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
    }
    thisdict.pop("model")
    print(thisdict)
    ```
    
    ```python
    The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
    
    thisdict = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
    }
    thisdict.popitem()
    print(thisdict)
    ```
    
    ```python
    The del keyword removes the item with the specified key name:
    
    thisdict = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
    }
    del thisdict["model"]
    print(thisdict)
    ```
    
    ```python
    The del keyword can also delete the dictionary completely:
    
    thisdict = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
    }
    del thisdict
    print(thisdict) #this will cause an error because "thisdict" no longer exists.
    ```
    
    ```python
    The clear() method empties the dictionary:
    
    thisdict = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
    }
    thisdict.clear()
    print(thisdict)
    ```
    

### Loop & Copy Dictionaries

- Loop
    
    You can loop through a dictionary by using a `for` loop.
    
    When looping through a dictionary, the return value are the *keys* of the dictionary, but there are methods to return the *values* as well.
    
    ```python
    #Print all key names in the dictionary, one by one:
    
    for x in thisdict:
      print(x)
    ```
    
    ```python
    #You can also use the values() method to return values of a dictionary:
    
    for x in thisdict.values():
      print(x)
    
    #You can use the keys() method to return the keys of a dictionary:
    
    for x in thisdict.keys():
      print(x)
    
    #Loop through both keys and values, by using the items() method:
    
    for x, y in thisdict.items():
      print(x, y
    ```
    
- Copy
    
    You cannot copy a dictionary simply by typing `dict2 = dict1`, because: `dict2` will only be a *reference* to `dict1`, and changes made in `dict1` will automatically also be made in `dict2`.
    
    There are ways to make a copy, one way is to use the built-in Dictionary method `copy()`.
    
    ```python
    #Make a copy of a dictionary with the copy() method:
    
    thisdict = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
    }
    mydict = thisdict.copy()
    print(mydict)
    ```
    
     Another way to make a copy is to use the built-in function `dict()`
    
    ```python
    #Make a copy of a dictionary with the dict() function:
    
    thisdict = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
    }
    mydict = dict(thisdict)
    print(mydict)
    ```
    

---

### Nested Dictionaries

A dictionary can contain dictionaries, this is called nested dictionaries.

```python
#Create a dictionary that contain three dictionaries:

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

#Or, if you want to add three dictionaries into a new dictionary:
#Create three dictionaries, then create one dictionary that will contain the other three dictionaries:

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
```

---

### Dictionary Methods

![Untitled](Python%20Basics%20I%2035d88854efd94a79919c1f4e1e5702e1/Untitled%208.png)

- some examples
    - .get
        
        ```python
        user = {
        	'basket':[1,2,3]
        	'greet':'hello'
        }
        
        #Lets say we wanted to check if we have the age for a user, we could check using this 
        print (user['age'])      ❌
        	>ERROR                 #this is bad, we dont want errors - this breaks the code.
        
        print (user.get('age'))  ✅
        	>NONE                  #this is good as we got what we wanted.
        
        #Next scenario, lets say if the user had no age, didnt exist - we could give it a default of something 
        user = {
        	'basket':[1,2,3]
        	'greet':'hello'
        }
        
        print (user.get.('age', 21))
        	>55                            #if there was no age
        ```
        
        ```python
        user2 = dict(name="John Doe")
        	print(user2)
        	>{'name':'John Doe'}
        ```
        
    
    ### **Pull something from a dictionary within a dictionary**
    
    `mydictionary = {'k1':{'k2':'hello'}} 
    mydictionary = [‘k1’][‘k2’] 
    ‘hello’`
    

---

<aside>
❗ **Data Structure**
Data structures are **the fundamental constructs around which you build your programs**
Each data structure provides a particular way of organizing data so it can be accessed efficiently, depending on your use case.

</aside>

<aside>
❗ **Data Types**
Data types are **the classification or categorization of data items**
It represents the kind of value that tells what operations can be performed on a particular data. Since everything is an object in Python programming, data types are actually classes and variables are instance (object) of these classes.

</aside>

---

<aside>
❓ Why can’t you sort a dictionary
*They are mappings and not sequences*

</aside>

---

<aside>
🔍 list vs dictionary
**A list is an ordered sequence of objects, whereas dictionaries are unordered sets**
However, the main difference is that items in dictionaries are accessed via keys and not via their position

**Dictionaries**   –          objects retrieved by key name, but are unordered and cannot be sorted

**Lists**   –         objects retrieved by location, but are ordered sequences that can be indexed or sliced

`prices_lookup = {'apple':2.99,'oranges':1.99,'milk':4}
prices_lookup['oranges']
1.99`

</aside>

## Tuples

### Overview

- Tuples are used to store multiple items in a single variable.
- A tuple is a collection which is ordered and **unchangeable**.
- written with round brackets.

<aside>
❗ Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are :
[List](https://www.w3schools.com/python/python_lists.asp), [Set](https://www.w3schools.com/python/python_sets.asp), and [Dictionary](https://www.w3schools.com/python/python_dictionaries.asp) - all with different qualities and usage.

</aside>

- Example
    
    ```python
    thistuple = ("apple", "banana", "cherry")
    print(thistuple)
    ```
    

### Tuple Items

---

Tuple items are ordered, unchangeable, and allow duplicate values.

Tuple items are indexed, the first item has index `[0]`, the second item has index `[1]` etc.

- Ordered
    
    When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
    
- Unchangeable
    
    Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
    
    ---
    
- Allow Duplicates
    
    Since tuples are indexed, they can have items with the same value:
    
    - example
        
        ```python
        #Tuples allow duplicate values:
        thistuple = ("apple", "banana", "cherry", "apple", "cherry")
        print(thistuple)
        ```
        
    

---

- **Tuple Length**
    
    To determine how many items a tuple has, use the `len()` function:
    
    # 
    
- ************************************************The tuple() Constructor************************************************
    
    It is also possible to use the tuple() constructor to make a tuple.
    
    ```python
    thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
    print(thistuple)
    ```
    
- **Create Tuple With One Item**
    
    To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
    
    - example
        
        ```python
        thistuple = ("apple",)
        print(type(thistuple))
        
        #NOT a tuple
        thistuple = ("apple")
        print(type(thistuple))
        ```
        

---

- Tuple Items - Data Types
    
    Tuple items can be of any data type
    
    A tuple can contain different data types:
    
    ```python
    #any data type
    #String, int and boolean data types:
    
    tuple1 = ("apple", "banana", "cherry")
    tuple2 = (1, 5, 7, 9, 3)
    tuple3 = (True, False, False)
    
    #A tuple can contain different data types
    #A tuple with strings, integers and boolean values:
    
    tuple1 = ("abc", 34, True, 40, "male")
    ```
    

---

---

### Accessing Tuples

- Access tuple
    
    items by referring to the index number, inside square brackets:
    
    ```python
    #Print the second item in the tuple:
    
    thistuple = ("apple", "banana", "cherry")
    print(thistuple[1])
    ```
    
- Negative Indexing
    
    <aside>
    ❗ Negative indexing means start from the end.
    
    - `1` refers to the last item, `2` refers to the second last item etc.
    </aside>
    
    Print the last item of the tuple:
    
    ```python
    #Negative Indexing - Print the last item of the tuple:
    thistuple = ("apple", "banana", "cherry")
    print(thistuple[-1])
    
    ```
    
- Range of Indexes
    
    You can specify a range of indexes by specifying where to start and where to end the range.
    When specifying a range, the return value will be a new tuple with the specified items.
    
    ```python
    #Range of Indexes
    #You can specify a range of indexes by specifying where to start and where to end the range.
    #When specifying a range, the return value will be a new tuple with the specified items.
    thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
    print(thistuple[2:5])
    ```
    
- Check if Item Exists
    
    To determine if a specified item is present in a tuple use the in keyword:
    
    Check if "apple" is present in the tuple:
    
    ```python
    thistuple = ("apple", "banana", "cherry")
    if "apple" in thistuple:
      print("Yes, 'apple' is in the fruits tuple")
    ```
    

### Update Tuples

- Change Tuple Values
    
    Once a tuple is created, you cannot change its values. Tuples are **unchangeable**, or **immutable** as it also is called.
    
    But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
    
    ```python
    #Convert the tuple into a list to be able to change it:
    x = ("apple", "banana", "cherry")
    y = list(x)
    y[1] = "kiwi"
    x = tuple(y)
    
    print(x)
    ```
    
- Add Items
    
     Since tuples are immutable, they do not have a build-in `append()` method, but there are other ways to add items to a tuple.
    
    1. **Convert into a list**: 
    Just like the workaround for *changing* a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.
    
    ```python
    #Convert the tuple into a list, add "orange", and convert it back into a tuple:
    
    thistuple = ("apple", "banana", "cherry")
    y = list(thistuple)
    y.append("orange")
    thistuple = tuple(y)
    ```
    
    2. **Add tuple to a tuple**
    You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:
    
    ```python
    #Create a new tuple with the value "orange", and add that tuple:
    
    thistuple = ("apple", "banana", "cherry")
    y = ("orange",)
    thistuple += y
    
    print(thistuple)
    ```
    
- Remove Items
    
    <aside>
    ❗ **Note:** You cannot remove items in a tuple.
    
    </aside>
    
    Tuples are **unchangeable**, so you cannot remove items from it, 
    
    <aside>
    💡 but you can use the same workaround as we used for changing and adding tuple items:
    
    </aside>
    
    ```python
    #Convert the tuple into a list, remove "apple", and convert it back into a tuple:
    
    thistuple = ("apple", "banana", "cherry")
    y = list(thistuple)
    y.remove("apple")
    thistuple = tuple(y)
    ```
    
    <aside>
    💡 Or you can delete the tuple completely:
    
    </aside>
    
    ```python
    #The del keyword can delete the tuple completely:
    
    thistuple = ("apple", "banana", "cherry")
    del thistuple
    print(thistuple) #this will raise an error because the tuple no longer exists
    ```
    

### **Unpack Tuples**

When we create a tuple, we normally assign values to it. This is called "packing" a tuple:

But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":

```python
#Packing a tuple:

fruits = ("apple", "banana", "cherry")

#Unpacking a tuple:

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
```

<aside>
💡 **Note:**
 The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.

</aside>

- **Using Asterisk***
    
    If the number of variables is less than the number of values, you can add an `*` to the variable name and the values will be assigned to the variable as a list:
    
    ```python
    #Assign the rest of the values as a list called "red":
    
    fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
    
    (green, yellow, *red) = fruits
    
    print(green)
    print(yellow)
    print(red)
    ```
    
    If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.
    
    ```python
    #Add a list of values the "tropic" variable:
    
    fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
    
    (green, *tropic, red) = fruits
    
    print(green)
    print(tropic)
    print(red)
    ```
    

### Loop, Join & Multiply Tuples

- Loop through a Tuple
    
    ```python
    You can loop through the tuple items by using a for loop.
    Iterate through the items and print the values:
    
    thistuple = ("apple", "banana", "cherry")
    for x in thistuple:
      print(x)
    
    ```
    
    - **Loop Through the Index Numbers**
        
        You can also loop through the tuple items by referring to their index number.
        Use the range() and len() functions to create a suitable iterable.
        
        ```python
        Print all items by referring to their index number:
        
        thistuple = ("apple", "banana", "cherry")
        for i in range(len(thistuple)):
          print(thistuple[i])
        ```
        
    - Using a While Loop
        
        You can loop through the list items by using a `while` loop.
        
        Use the `len()` function to determine the length of the tuple, then start at 0 and loop your way through the tuple items by referring to their indexes.
        
        Remember to increase the index by 1 after each iteration.
        
        ```python
        Print all items, using a while loop to go through all the index numbers:
        
        thistuple = ("apple", "banana", "cherry")
        i = 0
        while i < len(thistuple):
          print(thistuple[i])
          i = i + 1
        ```
        
- Join Tuples
    
    To join two or more tuples you can use the `+` operator:
    
    ```python
    Join two tuples:
    
    tuple1 = ("a", "b" , "c")
    tuple2 = (1, 2, 3)
    
    tuple3 = tuple1 + tuple2
    print(tuple3)
    ```
    
- Multiply Tuples
    
    If you want to multiply the content of a tuple a given number of times, you can use the `*`
     operator:
    
    ```python
    Multiply the fruits tuple by 2:
    
    fruits = ("apple", "banana", "cherry")
    mytuple = fruits * 2
    
    print(mytuple)
    ```
    

---

### Tuple Methods

![Untitled](Python%20Basics%20I%2035d88854efd94a79919c1f4e1e5702e1/Untitled%209.png)

## Sets

### Overview

- Sets are used to store multiple items in a single variable.
- Sets are written with curly brackets.

```python
thisset = {"apple", "banana", "cherry"}
print(thisset)
```

<aside>
💡  **Note:** 
Set *items* are unchangeable, but you can remove items and add new items.

</aside>

<aside>
💡 **Note:**
Sets are unordered, so you cannot be sure in which order the items will appear.

</aside>

### Set Items

Set items are unordered, unchangeable, and do not allow duplicate values.

- **Unordered**
    
    Unordered means that the items in a set do not have a defined order.
    
    Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
    
- **Unchangeable**
    
    Set items are unchangeable, meaning that we cannot change the items after the set has been created.
    
    Once a set is created, you cannot change its items, but you can remove items and add new items.
    
- **Duplicates Not Allowed**
    
    Sets cannot have two items with the same value.
    
    - example
        
        ```python
        Duplicate values will be ignored:
        
        thisset = {"apple", "banana", "cherry", "apple"}
        
        print(thisset)
        ```
        

---

- Set Length
    
    Get the Length of a Set
    To determine how many items a set has, use the len() function.
    
    ```python
    Get the number of items in a set:
    
    thisset = {"apple", "banana", "cherry"}
    
    print(len(thisset))
    ```
    
- The set() constructor
    
    It is also possible to use the set() constructor to make a set.
    
    ```python
    Using the set() constructor to make a set:
    
    thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
    print(thisset)
    ```
    

---

- Set Items - Data Types
    
    Set items can be of any data type & A set can contain different data types:
    
    ```python
    String, int and boolean data types:
    
    set1 = {"apple", "banana", "cherry"}
    set2 = {1, 5, 7, 9, 3}
    set3 = {True, False, False}
    
    A set with strings, integers and boolean values:
    
    set1 = {"abc", 34, True, 40, "male"}
    ```
    
    From Python's perspective, sets are defined as objects with the data type 'set':
    
    <class 'set'>
    
    ```python
    What is the data type of a set?
    
    myset = {"apple", "banana", "cherry"}
    print(type(myset))
    ```
    

---

### Access Set Items

You cannot access items in a set by referring to an index or a key.

But you can loop through the set items using a `for` loop, or ask if a specified value is present in a set, by using the `in` keyword.

```python
#Loop through the set, and print the values:
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#Check if "banana" is present in the set:

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)
```

<aside>
❗ Change Items

Once a set is created, you cannot change its items, but you can add new items.

</aside>

### Add & Remove Set Items

- Add
    - Add Items
        
        To add one item to a set use the add() method.
        
        ```python
        #Add an item to a set, using the add() method:
        
        thisset = {"apple", "banana", "cherry"}
        thisset.add("orange")
        
        print(thisset)
        ```
        
    - Add sets
        
        To add items from another set into the current set, use the `update()`
         method.
        
        ```python
        #Add elements from tropical into thisset:
        thisset = {"apple", "banana", "cherry"}
        tropical = {"pineapple", "mango", "papaya"}
        
        thisset.update(tropical)
        
        print(thisset)
        ```
        
    - Add Any Iterable
        
        The object in the `update()`
         method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
        
        ```python
        thisset = {"apple", "banana", "cherry"}
        mylist = ["kiwi", "orange"]
        
        thisset.update(mylist)
        
        print(thisset)
        ```
        
- Remove
    
    To remove an item in a set, use the `remove()`, or the `discard()` method.
    
    <aside>
    💡 **Note:**
     If the item to remove does not exist, `remove()` will raise an error.
    
    </aside>
    
    ```python
    #Remove "banana" by using the remove() method:
    
    thisset = {"apple", "banana", "cherry"}
    thisset.remove("banana")
    
    print(thisset)
    
    #Remove "banana" by using the discard() method:
    
    thisset = {"apple", "banana", "cherry"}
    thisset.discard("banana")
    
    print(thisset)
    ```
    
    <aside>
    💡 **Note:**
     If the item to remove does not exist, `discard()` will **NOT** raise an error.
    
    </aside>
    
    You can also use the `pop()` method to remove an item, but this method will remove the *last* item. Remember that sets are unordered, so you will not know what item that gets removed.
    
    The return value of the `pop()` method is the removed item.
    
    ```python
    #Remove the last item by using the pop() method:
    
    thisset = {"apple", "banana", "cherry"}
    x = thisset.pop()
    
    print(x)
    print(thisset)
    ```
    
    <aside>
    💡 **Note:**
     Sets are *unordered*, so when using the `pop()` method, you do not know which item that gets removed.
    
    </aside>
    
    ```python
    #The clear() method empties the set:
    
    thisset = {"apple", "banana", "cherry"}
    thisset.clear()
    
    print(thisset)
    
    #The del keyword will delete the set completely:
    
    thisset = {"apple", "banana", "cherry"}
    
    del thisset
    print(thisset)
    ```
    

### Loop & Join Sets

- Loop sets
    
    You can loop through the set items by using a `for` loop:
    
    ```python
    Loop through the set, and print the values:
    
    thisset = {"apple", "banana", "cherry"}
    
    for x in thisset:
      print(x)
    ```
    
- Join sets
    
    There are several ways to join two or more sets in Python.
    
    You can use the `union()` method that returns a new set containing all items from both sets, or the `update()` method that inserts all the items from one set into another:
    
    ```python
    #The union() method returns a new set with all items from both sets:
    
    set1 = {"a", "b" , "c"}
    set2 = {1, 2, 3}
    
    set3 = set1.union(set2)
    print(set3)
    
    #The update() method inserts the items in set2 into set1:
    
    set1 = {"a", "b" , "c"}
    set2 = {1, 2, 3}
    
    set1.update(set2)
    print(set1)
    ```
    
    <aside>
    💡 **Note:**
     Both `union()` and `update()` will exclude any duplicate items.
    
    </aside>
    
    - **Keep ONLY the Duplicates**
        
        ```python
        #The intersection_update() method will keep only the items that are present in both sets.
        #Keep the items that exist in both set x, and set y:
        
        x = {"apple", "banana", "cherry"}
        y = {"google", "microsoft", "apple"}
        
        x.intersection_update(y)
        
        print(x)
        
        #The intersection() method will return a new set, that only contains the items that are present in both sets.
        #Return a set that contains the items that exist in both set x, and set y:
        
        x = {"apple", "banana", "cherry"}
        y = {"google", "microsoft", "apple"}
        
        z = x.intersection(y)
        
        print(z)
        ```
        
    - **Keep All, But NOT the Duplicates**
        
        ```python
        #The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
        #Keep the items that are not present in both sets:
        
        x = {"apple", "banana", "cherry"}
        y = {"google", "microsoft", "apple"}
        
        x.symmetric_difference_update(y)
        
        print(x)
        
        #The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.
        #Return a set that contains all items from both sets, except items that are present in both:
        
        x = {"apple", "banana", "cherry"}
        y = {"google", "microsoft", "apple"}
        
        z = x.symmetric_difference(y)
        
        print(z)
        ```
        

---

### Set Methods

![Untitled](Python%20Basics%20I%2035d88854efd94a79919c1f4e1e5702e1/Untitled%2010.png)