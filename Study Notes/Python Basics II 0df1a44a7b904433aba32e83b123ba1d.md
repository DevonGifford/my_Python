# Python Basics II

Actual: 9 hours
ETA: 4 hours
Reviewed: No
Section: Section 4
Summary: No
Type: Lecture, Notes
complete: Done

# Python Basics II

# Table of Contents

---

---

## Breaking the Flow

Up until this point Everything you have seen so far has consisted of **sequential execution**, in which statements are always performed one after the next, in exactly the order specified.…

But the world is often more complicated than that. Frequently, a program needs to skip over some statements, execute a series of statements repetitively, or choose between alternate sets of statements to execute.

That is where **control structures** come in. A control structure directs the order of execution of the statements in a program (referred to as the program’s [control flow](https://en.wikipedia.org/wiki/Control_flow)

Now we are going to look at the true power of programming

- Running multiply lines over and over
- Skipping lines
- Ideas of condition and conditional logic and what loops are and how to loop some of our own code

## Conditional Logic

<aside>
🤖 A **simple way to tell a computer to perform an action upon a certain condition being met**.  Using this logic, you can build a tree of commands that eventually takes the shape of an executable program.

</aside>

By using Indentations and Conditional Logic, we can better inform the computer what it is we want it to do 

In a Python program, the `if` statement is how you perform this sort of decision-making. It allows for **conditional** execution of a statement or group of statements based on the value of an expression.

<aside>
💡 Python: It’s All About the Indentation
Python follows a convention known as the [off-side rule](https://en.wikipedia.org/wiki/Off-side_rule), a term coined by British computer scientist Peter J. Landin. (The term is taken from the offside law in association football.) Languages that adhere to the off-side rule define blocks by indentation. Python is one of a relatively small set of [off-side rule languages](https://en.wikipedia.org/wiki/Off-side_rule#Off-side_rule_languages).

Recall from the previous tutorial on Python program structure that [indentation has special significance](https://realpython.com/python-program-structure/#whitespace-as-indentation) in a Python program. Now you know why: indentation is used to define compound statements or blocks. In a Python program, contiguous statements that are indented to the same level are considered to be part of the same block.

</aside>

![Untitled](Python%20Basics%20II%200df1a44a7b904433aba32e83b123ba1d/Untitled.png)

## Indentation in Python

Python relies on indentation (whitespace at the beginning of a line) to define scope in the code.  Other programming languages often use curly-brackets for this purpose.

```python
#If statement, without indentation (will raise an error):

a = 33
b = 200
if b > a:
print("b is greater than a") # you will get an error
```

## Truthy vs. Falsely

We use "*truthy*" and "*falsely*" to differentiate from the `bool` values `True` and `False`.   A "truthy" value will satisfy the check performed by `if` or `while` statements. As explained [in the documentation](https://docs.python.org/3/library/stdtypes.html#truth-value-testing), all values are considered "truthy" except for the following, which are "falsy":

- `None`
- `False`
- Numbers that are numerically equal to zero, including:
    - `0`
    - `0.0`
    - `0j`
    - `[decimal.Decimal(0)](https://docs.python.org/3/library/decimal.html#decimal.Decimal)`
    - `[fraction.Fraction(0, 1)](https://docs.python.org/3/library/fractions.html#fractions.Fraction)`
- Empty sequences and collections, including:
    - `[]` - an empty `list`
    - `{}` - an empty `dict`
    - `()` - an empty `tuple`
    - `set()` - an empty `set`
    - `''` - an empty `str`
    - `b''` - an empty `bytes`
    - `bytearray(b'')` - an empty `bytearray`
    - `memoryview(b'')` - an empty `memoryview`
    - an empty `range`, like `range(0)`
- objects for which
    - `obj.__bool__()` returns `False`
    - `obj.__len__()` returns `0`, given that `obj.__bool__` is undefined

- `==` vs `is`
    
    `is`     - this checks the location in the memory
    
    `==`    - this compares the two items   
    

## Ternary Operator

<aside>
❕ Also known as, “conditional expressions”

</aside>

The **ternary operator** is a way of writing conditional statements in Python.  As the name ternary suggests, this Python operator consists of *three* operands.

The ***ternary operator*** can be thought of as a simplified, one-line version of the if-else statement to test a condition.

These operators evaluate something based on a condition being true or not. 

- example
    
    ```python
    value_if_true if condition else value_if_false
    
    is_nice = True
    state = "nice" if is_nice else "not nice"
    ```
    
    It allows to quickly test a condition instead of a multiline if statement. Often times it can be immensely helpful and can make your code compact but still maintainable.
    
    ```python
    (if_test_is_false, if_test_is_true)[test]
    
    nice = True
    personality = ("mean", "nice")[nice]
    print("The cat is ", personality)
    # Output: The cat is nice
    ```
    
    This works simply because True == 1 and False == 0, and so can be done with lists in addition to tuples.
    
    The above example is not widely used and is generally disliked by Pythonistas for not being Pythonic. It is also easy to confuse where to put the true value and where to put the false value in the tuple.
    
    Another reason to avoid using a tuple ternary is that it results in both elements of the tuple being evaluated, whereas the if-else ternary operator does not.
    
- **Short Hand Ternary**
    
    In python there is also the shorthand ternary tag which is a shorter version of the normal ternary operator you have seen above.
    
    The first statement (True or “Some”) will return True and the second statement (False or “Some”) will return Some.
    
    This is helpful in case where you quickly want to check for the output of a function and give a useful message if the output is empty:
    
    ```python
    >>> True or "Some"
    True
    >>>
    >>> False or "Some"
    'Some'
    
    >>> output = None
    >>> msg = output or "No data returned"
    >>> print(msg)
    
    No data returned
    ```
    
    Or as a simple way to define function parameters with dynamic default values:
    
    ```python
    >>> def my_function(real_name, optional_display_name=None):
    >>>     optional_display_name = optional_display_name or real_name
    >>>     print(optional_display_name)
    >>> my_function("John")
    John
    >>> my_function("Mike", "anonymous123")
    anonymous123
    ```
    

## Short Circuiting

<aside>
💬 So basically this refers to when we have two things like in the example:
So like if we need to check if only one is true then no matter what the second one is, we will get a True or False answer.
Therefore we are “short-circuiting” the rest of the code (i.e. it doesn’t even check the rest of the code because already got the answer, the remaining code wont effect the end answer)

</aside>

```python
is_physically_fit = True
is_mentally_fit = True

if is_mentally_fit and is_physically_fit:
	print('balanced indavidual')
```

**Formal Definition** 

Refers to the **stoppage of execution of boolean operation if the truth value of expression has been determined already**. The evaluation of expression takes place from **left to right**. 

In python, short-circuiting is supported by various boolean operators and functions.

## Python Operators - Logical operators

Today we are looking at Logical operators:

- Python divides the operators in the following groups:
    - Logical operators
        
        ![Untitled](Python%20Basics%20II%200df1a44a7b904433aba32e83b123ba1d/Untitled%201.png)
        
    - Arithmetic operators
        
        ![Untitled](Python%20Basics%20II%200df1a44a7b904433aba32e83b123ba1d/Untitled%202.png)
        
    - Assignment operators
        
        ![Untitled](Python%20Basics%20II%200df1a44a7b904433aba32e83b123ba1d/Untitled%203.png)
        
    - Comparison operators
        
        ![Untitled](Python%20Basics%20II%200df1a44a7b904433aba32e83b123ba1d/Untitled%204.png)
        
    - Identity operators
        
        Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
        
        ![Untitled](Python%20Basics%20II%200df1a44a7b904433aba32e83b123ba1d/Untitled%205.png)
        
    - Membership operators
        
        ![Untitled](Python%20Basics%20II%200df1a44a7b904433aba32e83b123ba1d/Untitled%206.png)
        
    - Bitwise operators
        
        ![Untitled](Python%20Basics%20II%200df1a44a7b904433aba32e83b123ba1d/Untitled%207.png)
        

![Untitled](Python%20Basics%20II%200df1a44a7b904433aba32e83b123ba1d/Untitled%201.png)

## For Loops

- my little notes
    - ❓**What does it do?**
        
        Allows us to run lines of code over and over again (super useful)
        
        ---
        
        - ❗**For Loops works with:**   `strings`, `lists`, `sets`, `tuples`, and kind of `dictionaries`
            
            ```python
            for item in 'I am-':
            	print (item)
            	print (item)
            print (item)
            I
            
            a
            m
            -
            I
             
            a
            m
            -
            -
            
            # 'item' - is a variable - it could be anything 
            
            # 'I am' - is an iterable, this could be anything that is iterable
            
            #the final print - you can see the output will give multiple '-' characters.
            		#why?  :  
            ```
            
            ```python
            for item in (1,2,3):
            	for x in ['a','b','c']
            		print (item, x)
            
            1 a 
            2 b
            3 c
            ```
            
    
    - **❓How to create one?**
        
         `for`  this_is_our_variable   `in`  **‘This is called an iterable’ :**
        
        In natural language it reads as follow:
        `for` every item `in` the following “String/List/Tuple/Set” :  do something
        
    
    - ❓W**hat is an iterable?**
        
        **S**omething that is able to be looped over 
        
    
    - ❓W**hat is variable?**
    

---

- A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
- This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
- With the for loop we can execute a *set of statements*, **once** for *each item* in a list, tuple, set etc.

```python
##Loop through the letters in the word "banana":

for x in "banana":
  print(x)
```

<aside>
💡 The for loop does not require an indexing variable to set beforehand.

</aside>

---

### **Looping Through a String**

Even strings are iterable objects, they contain a sequence of characters:

```python
#Loop through the letters in the word "banana":

for x in "banana":
  print(x)
b
a
n
a
n
a
```

### **The Break Statement**

With the `break` statement we can stop the loop before it has looped through all the items:

```python
#Exit the loop when x is "banana":

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
apple
banana

#Exit the loop when x is "banana", but this time the break comes before the print:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
apple
```

### **The Continue Statement**

With the `continue` statement we can stop the current iteration of the loop, and continue with the next:

```python
#Do not print banana:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
apple
cherry
```

### **The range() Function**

To loop through a set of code a specified number of times, we can use the `range()` function,
The `range()` function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

```python
#Using the range() function:

for x in range(6):
  print(x)
0
1
2
3
4
5
```

<aside>
❗ Note that range(6) is not the values of 0 to 6, but the values 0 to 5.

</aside>

The `range()` function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: `range(2, 6)`, which means values from 2 to 6 (but not including 6):

```python
#Using the start parameter:
for x in range(2, 6):
  print(x)
2
3
4
5
```

The `range()` function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a 3rd parameter: `range(2, 30, **3**):`

```python
#Increment the sequence with 3 (default is 1):

for x in range(2, 30, 3):
  print(x)
2
5
8
11
14
17
20
23
26
29
```

### **Else in For Loop**

The `else` keyword in a `for` loop specifies a block of code to be executed when the loop is finished:

<aside>
❗ **Note:**
 The `else` block will NOT be executed if the loop is stopped by a `break` statement.

</aside>

```python
**Print all numbers from 0 to 5, and print a message when the loop has ended:**
for x in range(6):
  print(x)
else:
  print("Finally finished!")
>
0
1
2
3
4
5
Finally finished!

**Break the loop when x is 3, and see what happens with the else block:**

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
>
0
1
2
Finally finished!
```

### **Nested Loops**

A nested loop is a loop inside a loop.

The "inner loop" will be executed one time for each iteration of the "outer loop":

```python
**Print each adjective for every fruit:**

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
>
red apple
red banana
red cherry
big apple
big banana
big cherry
tasty apple
tasty banana
tasty cherry
```

### **The pass Statement**

`for` loops cannot be empty, but if you for some reason have a `for` loop with no content, put in the `pass` statement to avoid getting an error.

```python
for x in [0, 1, 2]:
  pass
>
```

## Iterable

- **What does it mean**
    
    Simply means, it is an object or a collection that can be iterated over
    
    iterable = list, tuple, set, string, *dictionary* 
    
    **iterated/iterate** = one by one check each item in the collection 
    
    You are iterating over something, you are looping over something
    
    “So iterable is the noun and iterated or iterate is the action of iterating over an iterable.”
    

Dictionaries are a little different

```python
**Print the keys...**
user = {
	'name': 'Devon',
	'age': 28,
	'is_ripped': True
}

for item in user:
	print (item)
>
name
age
is_ripped

Iterate through the values...❓❓❓
```

<aside>
💡 Well, dictionaries have three methods that are really, really useful when we want to loop over their keys and values.

### 3 methods of iterating over dictionaries

### 1.  `.items()`

Get the key value pair in a tuple 

💡This is very common pattern 

```python
user = {	
	'name': 'Devon',
	'age': 28,
	'is_ripped': True
}

for item in user.items():
	print (item)
>
('name', 'Devon')
('age', 28)
('is_ripped', True)

```

### 2.  `.values()`

This gives us the, as you guessed it, the values

```python
user = {	
	'name': 'Devon',
	'age': 28,
	'is_ripped': True
}

for item in user.values():
	print (item)
>
Devon
28
True
```

### 3.  `.keys()`

We already know how to get the keys (leaving it blannk) - this is the more elegant way

```python
user = {	
	'name': 'Devon',
	'age': 28,
	'is_ripped': True
}

for item in user.keys():
	print (item)
>
name
age
is_ripped
```

</aside>

<aside>
💡 another interesting thing three methods can do
and 
another common pattern when iterating over dictionaries 

if you want to print separately, the ‘key’ and the ‘value’ in a dictionary
*Well, we could use the .items() method to get a tuple 
and then with tuple unpacking we could get what we are looking for
For example:*

```python
for item in user.items():
	key, value = item;
	print (key, value)
>
name Devon
age 28
is_ripped True
```

*There is a shorthand way to do this….*

```python
for key, value in user.items():
	print(key, value)
>
name Devon
age 28
is_ripped True
```

</aside>

## PRACTICAL TEST

Instructions

---

Building a "list counter"

using looping, loop over this iterable list and sum up the total of the list

---

my work

```python
#  Building a "list counter"

#  using looping
#  loop over this iterable list and sum up the total of the list

my_list = [*range(1, 11)]
#this little star '*' is argument-unpacking operator 
  
# Print the list
print("here is my list:")
print(my_list)

#Print the list indiviudally
print("\n\nHere is my list again, but indiviudally")
for x in my_list:
  print(x)

print("\n\n\tokay \n\tokay \nwe got going something \n \n whats good now...\n\n")

#attempt 1 of trying to tally
for x in my_list:
  x+=1
  print(x)
  
print("...\nThis failed\nBecasue\nThis simply just added one to everything that was printed.  This would also be a way to cheat I think - just adding one manually and tallying, as opposed to tallying\n\n")

#attempt 2 of trying to tally - using the count() method maybe?

#Perhaps I need another counter list?
#so then I am worktin with
print(my_list)
counter = 0

#now...attempt 3 (commenting this out) 
#for x in my_list:
  #counter +=1 + x
 # print(counter)

print("...\nThis failed\nBecasue\nThis simply just added one to everything and then added 'x' This is interesting though\nI am curious what would happen if I were to run it without adding the random +1\nLets test it out...\n\n")

#now... attempt 4
print("Summing up the total of 'my_list'")
for x in my_list:
  counter +=x
  print(counter)

print("...\nThis FUCKING wokred!\nBut now I wonder...\nCan I do it without showing my calculations?\nLets find out...\n\n")

#now attempt 5 ... without showing my calculations
for x in my_list:
  counter +=x
print(counter)
```

```python
#output
Here is my list again, but indiviudally
1
2
3
4
5
6
7
8
9
10

okay, okay 
we got going something 
whats good now...

2
3
4
5
6
7
8
9
10
11
...
This failed
Becasue
This simply just added one to everything that was printed.  This would also be a way to cheat I think - just adding one manually and tallying, as opposed to tallying

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
...
This failed
Becasue
This simply just added one to everything and then added 'x' This is interesting though
I am curious what would happen if I were to run it without adding the random +1
Lets test it out...

#with calculations
Summing up the total of 'my_list'
1
3
6
10
15
21
28
36
45
55
...
#without calculations
55

This FUCKING wokred!
But now I wonder...
Can I do it without showing my calculations?
Lets find out...
```

## Range() - function

- Definition and Usage
    - a built in function
    - The `range()` function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
- Syntax
    
    ```python
    **Syntax**
    
    range(start, stop, step)
    
    **Create a sequence of numbers from 0 to 5, and print each item in the sequence:**
    
    x = range(6)
    for n in x:
      print(n)
    
    **some examples:**
    
    #Create a sequence of numbers from 3 to 5, and print each item in the sequence:
    x = range(3, 6)
    for n in x:
      print(n)
    
    #Create a sequence of numbers from 3 to 19, but increment by 2 instead of 1:
    x = range(3, 20, 2)
    for n in x:
      print(n)
    ```
    

<aside>
❗ Remember to use the negative to do some things in reverse 😉

</aside>

![Untitled](Python%20Basics%20II%200df1a44a7b904433aba32e83b123ba1d/Untitled%208.png)

## Enumerate() - function

- Definition and Usage
    
    Gives us an index counter of whatever we are trying to iterate over. 
    
    The `enumerate()` function takes a collection (e.g. a tuple) and returns it as an enumerate object.
    
    The `enumerate()` function adds a counter as the key of the enumerate object.
    
    <aside>
    ❗ Must be an iterable object - very useful if you need the index number of the item you are looping through
    
    </aside>
    
- Syntax
    
    ```python
    enumerate(iterable, start)
    
    my_list = (1,2,3)
    for i, char in enumerate(my_list):
      print(i, char)
    >
    0 1
    1 2
    2 3
    
    example
    
    #find the value of a specific index
    
    for i, char in enumerate(list(range(100)):
    	if char == 50:
    		print(f'index of 50 is {i}')
    
    #Convert a tuple into an enumerate object:
    
    x = ('apple', 'banana', 'cherry')
    y = enumerate(x)
    
    ```
    

![Untitled](Python%20Basics%20II%200df1a44a7b904433aba32e83b123ba1d/Untitled%209.png)

## While Loops

- Definition and Usage
    
    Python has two primitive loop commands:  `while loops`  &   `for loops`
    
    - when to use what?
        - Use a `for loop` when you know the loop should execute ‘x’ amount of times.   (simpler but less powerful)
        - Use a `while loop` for reading a file into a variable.
            - Use a while loop when asking for user input.
            - Use a while loop when the increment value is nonstandard or uncertain.
            - With the `while loop` we can execute a set of statements as long as a condition is true.
    
    <aside>
    ❗ Always use a break statement - you can damage a machine!  *(not really but okay)*
    
    </aside>
    
- Syntax and example
    
    ```python
    **Print i as long as i is less than 6:**
    
    i = 1
    while i < 6:
      print(i)
      i += 1                                                              #if I had a break here, it would not print the else statement below .  
    else:
    	print("I have completed the task for you sir")
    
    #Note: remember to increment i, or else the loop will continue forever.
    
    while True:
    	response = input('say something: ')
    	if (response == 'fuck off'):
    		break
    ```
    
    <aside>
    💡 The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1.
    
    Remember to increment i, or else the loop will continue forever.
    
    </aside>
    

---

- Break & Continue Statement
    - Break Statement
        
        With the `break` statement we can stop the loop even if the while condition is true:
        
        ```python
        Exit the loop when i is 3:
        
        i = 1
        while i < 6:
          print(i)
          if i == 3:
            break
          i += 1
        ```
        
    - Continue Statement
        
        With the `continue` statement we can stop the current iteration, and continue with the next:
        
        ```python
        **Continue to the next iteration if i is 3:**
        
        i = 0
        while i < 6:
          i += 1
          if i == 3:
            continue
          print(i)
        ```
        
- Else Statement
    
    With the `else` statement we can run a block of code once when the condition no longer is true:
    
    ```python
    **Print a message once the condition is false:**
    
    i = 1
    while i < 6:
      print(i)
      i += 1
    else:
      print("i is no longer less than 6")
    ```
    

## What is clean code & exercise’s

**Clean** 
- no unnecessary code
- no strange lists
- no random spaces, tabs or comments

**Readability** 
- be able to understand your own code, and explain your code to co-workers
- useful comments 
- naming variables well

**Predictable** 
- sometimes people try to look smart with code
- do not repeat yourself over and over, smarter way to clean up

---

- Exercise 1
    
    ```python
    #Exercise!
    #Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
    picture = [
      [0,0,0,1,0,0,0],
      [0,0,1,1,1,0,0],
      [0,1,1,1,1,1,0],
      [1,1,1,1,1,1,1],
      [0,0,0,1,0,0,0],
      [0,0,0,1,0,0,0]
    ]
    
    for row in picture:
      for pixel in row:
        if pixel == 0:
          print(' ', end='')
        else:
          print('*', end='')
      print('')
    ```
    
- Exercise 2
    
    ```python
    #Check for duplicates in list:
    #print all the duplicates, as a list 
    some_list = ['a','b','c','b','d','m','n','n']
    
    #for item in some_list:
    #  test = some_list.count(item);
    #  if test <= 1:
    #    pass
    #  else:
    #    dupes_list.append(item)
    #print(dupes_list)
    
    #now I just need one instance of 'b' & one instance of 'n'
    for item in some_list:
      if some_list.count(item) >= 2:
        if item not in dupes_list:
          dupes_list.append(item)
    
    print (dupes_list)
    
    >
    ['b', 'n']
    
    ```
    

## Functions

- 📽️✍️
    
    <aside>
    📽️ - we can create our own functions
    - functions exists in all programming languages
    - useful when we have to do things over and over 
    
    ❗remember interpreters go line by line - therefore - put your functions at the top of your code.
    
    `def` - lets the interpreter know we are about to define a function (def stands for define
    
    To use a function, we need to call on it *(kind of like we call on print but easier)*:
    just type what you said after the `def` + `()` at the end
    
    ---
    
    **A function should follow 2 rules**
    
    - should do one thing really well
    - should return something (rule of thumb for beginners)
    - Lets turn that exercise into a function
        
        ```python
        picture = [
          [0,0,0,1,0,0,0],
          [0,0,1,1,1,0,0],
          [0,1,1,1,1,1,0],
          [1,1,1,1,1,1,1],
          [0,0,0,1,0,0,0],
          [0,0,0,1,0,0,0]
        ]
        
        def christmas_tree():                               # we made it into a function
        	for row in picture:
        	  for pixel in row:
        	    if pixel == 0:
        	      print(' ', end='')
        	    else:
        	      print('*', end='')
        	  print('')
        
        christmas_tree()                                     # we called the function here
        
        >
        	 *   
          ***  
         ***** 
        *******
           *   
           *
        ```
        
    </aside>
    

---

- A function is a block of code which only runs when it is called on.
- You can pass data, known as parameters, into a function.
- A function can return data as a result or it can modify something

---

### Creating & Calling a Function

sometimes called invoking a function

- Creating a Function
    
    In Python a function is defined using the def keyword:
    
    ```python
    #Example
    def my_function():
      print("Hello from a function")
    ```
    
- Calling a Function
    
    To call a function, use the function name followed by parenthesis:
    
    ```python
    #Example
    def my_function():
      print("Hello from a function")
    
    my_function()
    ```
    

### Arguments

- 📹✍️
    
    **Arguments vs Parameters**
    
    - we can give functions many many parameters
    - we can use our parameters as variables in our
    
    ```python
    #parameters -are used when we define the function
    #arguments - are used when we call the function 
    
    def say_hello(name, surnam, parameter3, parameter4)
    	print(f'Helloooooo there, {name}{parameter4}')
    
    say_hello('Devon','argument2')
    ```
    

<aside>
💡 *`Arguments`* are often shortened to *`args`* in Python documentations.

</aside>

- Information can be passed into functions as arguments.
- Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
- The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:

```python
#Example
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
```

- **Parameters vs. Arguments?**
    
    The terms *parameter* and *argument* can be used for the same thing: information that are passed into a function.
    
    From a function's perspective:
    
    ❗  A parameter is the variable listed inside the parentheses in the function definition.
    
    ❗  An argument is the value that is sent to the function when it is called.
    
- **Default Arguments**
    
    The following example shows how to use default arguments (also known as default parameter value.)
    
    If we call the function without argument, it uses the default value:
    
    ```python
    #Example
    def my_function(country = "Norway"):
      print("I am from " + country)
    
    my_function("Sweden")
    my_function("India")
    my_function()
    my_function("Brazil")
    ```
    
- **Positional Arguments**
    
    ```python
    def my_function(child3, child2, child1):
      print("The youngest child is " + child3)
    
    my_function("Emil","Tobias", "Linus")
    
    #You can use just the position to determine what parameter it gets
    ```
    
- **Keyword Arguments**
    
    You can also send arguments with the *key* = *value* syntax.
    
    This way the order of the arguments does not matter.
    
    <aside>
    💡 The phrase *Keyword Arguments* are often shortened to *`kwargs`* in Python documentations.
    
    </aside>
    
    ```python
    def my_function(child3, child2, child1):
      print("The youngest child is " + child3)
    
    my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
    ```
    
- **Number of Arguments**
    
    By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.
    
    ```python
    #This function expects 2 arguments, and gets 2 arguments:
    
    def my_function(fname, lname):
      print(fname + " " + lname)
    
    my_function("Emil", "Refsnes")
    
    #If you try to call the function with 1 or 3 arguments, you will get an error:
    #This function expects 2 arguments, but gets only 1:
    
    def my_function(fname, lname):
      print(fname + " " + lname)
    
    my_function("Emil")
    ```
    
- **Arbitrary Arguments -  `*args`**
    
    ---
    
    If you do not know how many arguments that will be passed into your function, add a `*` before the parameter name in the function definition.
    
    This way the function will receive a *tuple* of arguments, and can access the items accordingly:
    
    ```python
    #If the number of arguments is unknown, add a * before the parameter name:
    
    def my_function(*kids):
      print("The youngest child is " + kids[2])
    
    my_function("Emil", "Tobias", "Linus")
    ```
    
- **Arbitrary Keyword Arguments -  `**kwargs`**
    
    ---
    
    If you do not know how many keyword arguments that will be passed into your function, add two asterisk: `**` before the parameter name in the function definition.
    
    This way the function will receive a *dictionary* of arguments, and can access the items accordingly:
    
    <aside>
    💡 *Arbitrary Kword Arguments* are often shortened to *`**kwargs`* in Python documentations.
    
    </aside>
    
    ```python
    #If the number of keyword arguments is unknown, add a double ** before the parameter name:
    
    def my_function(**kid):
      print("His last name is " + kid["lname"])
    
    my_function(fname = "Tobias", lname = "Refsnes")
    
    def super_func(*args, **kwargs):
    	total = 0
    	for items in kwargs.values():
    		total += items
    	return sum(args) + total
    
    print(super_func(1,2,3,4,5, num1=5, num2=10))
    
    ```
    
    <aside>
    ❕ Rule of order:  params, *args, default parameters, **kwargs
    
    </aside>
    
- **Passing a List as an Argument**
    
    You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
    
    E.g. if you send a List as an argument, it will still be a List when it reaches the function:
    
    ```python
    #Example
    def my_function(food):
      for x in food:
        print(x)
    
    fruits = ["apple", "banana", "cherry"]
    
    my_function(fruits)
    ```
    

---

---

- Return Values
    
    To let a function return a value, use the `return` statement:
    
    <aside>
    ❗ `return` exits the function - so anything after the ‘return statement’, will not be processed.
    
    </aside>
    
    ```python
    #Example
    def my_function(x):
      return 5 * x                 #The Return tells the interpreter to exit this function
                                   #No return will = "NONE"     
    
    print(my_function(3))
    print(my_function(5))
    print(my_function(9))
    ```
    
- The Pass Statement
    
    `function` definitions cannot be empty, but if you for some reason have a `function` definition with no content, put in the `pass` statement to avoid getting an error.
    
    ```python
    #Example
    def myfunction():
      pass
    ```
    
- Recursion
    
    Python also accepts function recursion, which means a defined function can call itself.
    
    Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.
    
    The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.
    
    In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0).
    
    To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it.
    
    ```python
    #Recursion Example
    
    def tri_recursion(k):
      if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
      else:
        result = 0
      return result
    
    print("\n\nRecursion Example Results")
    tri_recursion(6)
    ```
    

---

- exercise
    
    ```python
    age = input("What is your age?: ")
    
    if int(age) < 18:
    	print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
    	print("Powering On. Enjoy the ride!");
    elif int(age) == 18:
    	print("Congratulations on your first year of driving. Enjoy the ride!")
      
    #1. Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age. 
    # Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?
    
    #2 Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
    #checkDriverAge(92);
    #it returns "Powering On. Enjoy the ride!"
    #also make it so that the default age is set to 0 if no argument is given.
    
    def checkDriverAger(age=0):
    #  age = input("What is your age?: ")
      print(f"So you are {age} years old.  Let's take a look\nOkay got it...")
      if int(age) < 18:
    	   print("Sorry, you are too young to drive this car. Powering off")
      elif int(age) > 18:
    	  print("Powering On. Enjoy the ride!");
      elif int(age) == 18:
    	  print("Congratulations on your first year of driving. Enjoy the ride!")
      else:
        print('so you are still a baby')
    
    checkDriverAger(22)
    checkDriverAger()
    
    >
    So you are 22 years old.  Let's take a look
    Okay got it...
    Powering On. Enjoy the ride!
    
    So you are 0 years old.  Let's take a look
    Okay got it...
    Sorry, you are too young to drive this car. Powering off
    
    ```
    
    ```python
    #this function  I thought was interesting.... 
    #have a look at the cat_bouncer function
    
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
    def cat_bouncer(*args):
            return max(args)
    
    # 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
    print(f"The oldest and most wisest cat is {cat_bouncer(kitty_one.age,kitty_two.age,kitty_three.age)} years old there chap")
    ```
    
    ```python
    def higest_even(li):
    	'''
    	Info:  This will find the largest even number in a list
    	'''
    	even_list = []
    	for items in li:
    		if items %2 == 0:
    			even_list.append(items)
    
    	return (max(even_list))
    
    print(higest_even([1,2,3,4,8,10,11]))
    ```
    

## Methods vs. Function

Methods are like already built in functions

You can create your own methods (apparently)

[Python Built-in Functions](https://www.w3schools.com/python/python_ref_functions.asp)

## Docstrings

unique thing we can do with functions

allows us to add a “comments” to our functions 

in fact most interpreters will let you see this comment if you hover over, or start typing functions

```python
def test(a):
	'''
	Info:  this is a uselessfunction
	'''
	print(a)

Test('!!!')
```

## Walrus Operator

(this was actually just an example of looking at new features)

way to minimize code.

<aside>
❕ **The := operator is officially known as the assignment expression operator
-**  The assignment expression **allows you to assign True to walrus , and immediately print the value**
During early discussions, it was dubbed the walrus operator because the := syntax resembles the eyes and tusks of a sideways walrus. You may also see the := operator referred to as the colon equals operator.

</aside>

```python
#This is a way to assign a variable in a function 

while ((n := len(a)) > 1):
	print(n)
	a = a[:-1]
print(a)
```

## Scope

Scope = What variable do I have access too

Name error or not defined error - this might be because of the scope 

so variables inside of functions are not accessible outside the function.

Therefore it’s not in the “global scope”. 

**Hierarchy when invoking a  function** 

1. **Local** - Start with local scope (inside the function that is called on)
2. **Parents** - Is there a parent of the function (i.e. is this a function in a function?)
3. **Global scope** - the indentation of nothing
4. **Built-in** - some functions are built into Python, eg. SUM

Global KeyWord

```python
def count():
	total += 1
	return total
print(count())
> ERROR

def count():
	global total 
	total += 1
	return total

```

Dependency Injection

```python
def count(total):
	total += 2
	return total

print(count(count(count(total))))

#Looks more confusing but the instructor argues this is nicer - he says noobs would disagree
```

Why do we even need scope??

Yes and No.
But this way it costs less CPU processing power 

---

## nonlocal Keyword

New Keyword

Refers to the parent local

If you want to call onto a a variable used in a parent function. 

if you want to use a variable that is not global but is outside the scope of local fucntion

```python
def outer():
	x = "local"
	def inner():
	non local x
	x -- "nonlocal"
	print("inner:",x)
```

## TEMPLATE