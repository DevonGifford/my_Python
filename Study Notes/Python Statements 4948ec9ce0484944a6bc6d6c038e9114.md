# Python Statements

Reviewed: No
Section: FINAL SUMMARY
Summary: No
Type: Other
complete: Future

# Ep.34 - If, Elif and Else Statements in Python

We often only want certain code to execute when a particular condition has been met.

e.g  **if** my dog is hungry *[condition has been met]*, then I will feed the dog *[action].*

**To control this flow of logic we use some keywords:**

- if
- elif
- else

Control Flow syntax makes use of colons and indentation (white spaces)

💡indentation system is crucial to Python and sets it apart from other programming languages

## Syntax of an **if** statement

`if some_condition`

`#execute some code`   

`elif some_other_condition`      *(check for multiple conditions before the else statement runs)*

`#do something different` 

`else:`                                         *(if the condition above was not true, then do the following)*

`#do something else`

💡 `loc`  = location 

# Ep.35 - For Loops in Python

Many objects in Python are 'iterable', meaning  we can iterate over every element in the object.

Such as every element in a list or every character in a string

We can use for loops to execute a block of code for every iteration

iterable - means you can "iterate" over the object (go through something)
*for example:
you can iterate over every character in a string, iterate over every item in a list, iterate over every key in a dictionary.
-  Therefore a dictionary is iterable, a string and a list are iterable
-  Therefore works with characters and integers*

### Syntax of a for loop

```python
my_iterable = [1,2,3]`               #  *"item_name" - variable name*     
`**for** iterm_name in my_iterable`   #  "*item name" is place holder, (can have any name*)
    `print(iterm_name)                #  therfore, could be "blah_blah"
1
2
3
```

💡  we can still execute some block of code for every single item in the list, even if the code itself is unrelated to the item

💡python coders often just use  a `_` for the variable name (in the example, `"item_name"`)
    they do this when it's of inconsequence what the name is, for readability purposes. 

## What can for loops do:

Odd & Even:

```python
mylist = [1,2,3,4,5,6,7,8,9,10]
for num in mylist:
		if num %2 = 1:
				print(f"odd number: {num}")
		else:
				print(f"even number: {num}")
```

Running tally, during multiple loops:

```python
list sum = 0
mylist = [1,2,3,4,5,6,7,8,9,10]

for num in mylsit:
		list_sum = list_sum + num
#now depending on where I tab the next line. I will get a different result 
			#if i indent, I will get a list with the code running until reaches end
			#if i don't indent, I will get the final result of the code
print (list_sum)
```

Iterate through strings:

```python
mystring = 'Hello World'

for variable in mystring:  #you don't even need a mystring (can use string)
		print (variable)
H
e
l
l
o

W
o
r
l
d
```

```python
#If you want the string to be split into words, you need to use the TAB .split() 
for variable in mystring.split():
		print(variable)
Hello
World
```

### For Loop with Tuples

tuple unpacking - used to unload tuples within a list 
*for example;*

`mylist = [(1,2),(3,4),(5,6)]
fora,b **in** (mylist)
       print(b)
2
4
6`

Example:

```perl
mylist = [(1,2),(3,4),(5,6)]

for a,b in mylist:
		print(a)  
		print(b)                  #Doing this is 'Tuple Unpacking'
1
2
3
4
5
6
```

### How to iterate through a dictionary

by default, when you iterate through a dictionary, you only iterate through the keys:

```python
dic = {'k1':1,'k2':2,'k3':3}

for item in d:
      prin(item)      #notice that by default, you only iterate through the keys

 k1
 k2
 k3
```

to iterate through the items themselves, you need to use:

```python
for items in d.items():
      print(item):
 ('k1', 1)
 ('k2', 3)
 ('k3', 3)

#Then we can use "Tuple Unpacking" to get indavidual either key or 
```

Therefore, we should use tuple unpacking technique to get the key:

```python
for key, value in d.items():   
           print (value)            #Obviously you can choose what you want to print
 1                                     #print(key)     or     print(value)
 2
 3
```

you can add strings to the print:

```python
for key,value in d.items():
    print(f'this is the key = {key} & this is the value = {value}')
```

💡This is easy now because the dictionaries are small, can get very complex 

# Ep.36 - While Loops in Python

While loops will continue to execute a block of code while some condition remains True.
*for example;*

while my pool is not full, keep filling my pool with water.
or
while my dogs are still hungry, keep feeding my dogs

## Syntax of while loop

```python
while some_boolean_conditiion_is_true:
       #do something
else:
       #do something different
```

💡be careful of the infinite loop - you can try interrupt or restart kernel if you get stuck
Actual example

```python
x = 0

while x < 10:
		print ('x is currently:  ', x)
		print ('x is still less than 10, adding to 1 to x')
		x += 1
else:
		print('All Done!')
```

result:

```python
x is currently:  0
 x is still less than 10, adding 1 to x
x is currently:  1
....repat...
x is still less than 10, adding 1 to x
All Done!
```

### **break, continue, pass**

We can use `break`, `continue`, and `pass` statements in our loops to add additional functionality for various cases. The three statements are defined by:

- **Pass**:                Does nothing at all.
    
                            *used to avoid syntax error (eg. unexpected EOF while parsing)*
    

```python
x = [1,2,3]

for item in x:
	#this is part of the example, if I press run now it will give the error.
	pass 
	#now that I have pass the code will run
```

💡another way to use the 'pass' - is if you want to run a script with an if function but you don't want to fill it out until later.  

- **Continue:**        Goes to the top of the closest enclosing loop.
                        *Meaning essentially skip this and continue with the script. *restart again*

```python
mystring = "Devon"
for letter in mystring
		if letter == 'e':
			continue 
		print(letter)
d
v
o
n
```

- Break:              Breaks out of the current closest enclosing loop
    
                            *stops the script*
    

```python
x = 0

while x < 5:
			if x 2:
				break
			print (x)
			x += 1
0
1
```

❗Thinking about `break` and `continue` statements, the general format of the `while` loop 
looks like this:

```python
while test:
    code statement
    if test:
        break
    if test:
        continue
else:
```

`break` and `continue` statements can appear anywhere inside the loop’s body, but we will usually put them further nested in conjunction with an `if` statement to perform an action based on some condition.

# Ep.37 - Useful Operators in Python

Python has a built in operators:

## Range

allows you to quickly *generate* a list of integers.

`range (0 , 11)`

there are 3 parameters you can pass

*`( start  ,  stop  ,  step size )*` 

❗range is a '*generator*' function - therefore to get a list out of it, you need to cast it into a list 

💡what is a generator?
a special type of function that will generate information and not need to save it to memory.

```python
list (range (0,10,2))
[0,2,4,6,8,]
#note how 10 is included, as the last step, but not included (just like notation)

for num in range(4):
		print(num)
0
1
2
3
```

❗ because this is an operator, you cant just do `range(0,10,2)`

## Enumerate

Keeping track of how many loops you've gone through is so common, that enumerate was created so you don't need to worry about creating and updating this `index_count` or `loop_count` variable

```python
index_count = 0

for letter in 'abcde':
    print("At index {} the letter is {}".format(index_count,letter))
    index_count += 1
At index 0 the letter is a
At index 1 the letter is b
At index 2 the letter is c
At index 3 the letter is d
At index 4 the letter is e
# Notice the tuple unpacking!
# This is so common, python has a operator ot do this 

for index,letter in enumerate('abcde'):
    print("At index {} the letter is {}".format(i,letter))
At index 0 the letter is a
At index 1 the letter is b
At index 2 the letter is c
At index 3 the letter is d
At index 4 the letter is e
```

## Zip

Sometimes when we get the format from `enumerate` we want to convert into a `list`
Therefore zips two lists together

```python
list (enumerate('abcde'))
[(0, 'a'), (1, 'b'), (2, 'c'), (3, 'e')]
```

❗This zips lists together like a literal zipper on a jumper

```python
mylist1 = [1,2,3,]  
mylist2 = ['a','b','c']
zip(mylist1,mylist2)
<zip at 0x1b4a0d9ad80>
#This zip generator is available in this location in your memory
#Therefore, to get a print out of the now combined list
```

❗Note that it only does up until `5` , even though there are more in `mylist2` the letter `'d'`

**∴** *To use the generator, we could just use a `for loop` (3 examples)*

```python
for item in zip(mylista,mylistb):
    print(item)
(1, 'a')
(2, 'b')
(3, 'c')
#Good to remember tuple unpacking
```

```python
for item1, item2 in zip(mylist1,mylist2):
    print('For this tuple, first item was {} and second item was {}'.format(item1,item2))
For this tuple, first item was 1 and second item was a
For this tuple, first item was 2 and second item was b
For this tuple, first item was 3 and second item was c
For this tuple, first item was 4 and second item was d
For this tuple, first item was 5 and second item was e
```

```python
list(zip(mylista,mylistb)
[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]
```

💡We can zip multiple lists together

## Operator

we can use the `in` keyword to quickly check if an object is in a list

```python
'x' in ['x','y','z']
True

'x' in [1,2,3]
False
```

## In and Not in

we can use this operator, to check if some object or variable `is` or `is not` present in a list.

💡This works in *lists* and *strings,* as seen below

```python
#In operator 
'd' in ['a','b','c']
False

2 in mylist
True 
```

```python
#Not in operator
'x' not in ['x','y','z']
False

'x' not in [1,2,3]
True
```

💡This works in dictionaries too!

```python
dictionary = {'key':420}

420 in dictionary.keys()
False

420 in dictionary.values()
True
```

## Min & Max

Quickly check the minimum or maximum of a list with these functions.

```python
mylist = [10,20,30,40,100]
min(mylist)
10
max(mylist)
100
```

## Random

Python comes with a built in random library. 
There are a lot of functions included in this random library

To import form library you need to use the TAB key
*for example,* `from randomimport`[TAB BUTTON] > then select what you want to import 

### random.shuffle

```python
from random import shuffle
# This shuffles the list "in-place" meaning it won't return anything, 
# instead it will effect the list passed
shuffle(mylist)
mylist
[40, 10, 100, 30, 20]
```

### random.randit

```python
from random import randint
#Return random integer in range [a, b], including both end points
randint (0,100)
25

thenum = randint(0,100)
thenum
91
```

## Input

```python
input('Enter Something into this box:  ')
Enter something into this box: <great job!>
'great job!'
```

Sometimes we want to save the details, or call on them again
**∴ we can do the following:**

```python
users_name = input('Write your name:  ')
Write your name: <Devon>
user_name
Devon
```

❗whatever you type in the box,  python accepts as a string
Therefore to transform we need to, either

```python
#  if we are expecting a floating point or want a floating point
float (result)
#  if we expect an integer or want a number without a decimal
int (result)
```

# Ep.38 - List Comprehensions in Python

In addition to sequence operations and list methods, Python includes a more advanced operation called a **list comprehension**.

List comprehensions allow us to build out lists using a different notation. 
*You can think of it as essentially a one line for loop built inside of brackets.*

    **∴  instead of having code that runs like this:**

```python
mystring = 'hello'
mylist = []
for any_variable in mystring:
		mylist.append(letter)

mylist
['h','e','l','l','o']
```

          **∴  we could instead:**

```python
mylist = [any_variable for any_variable in 'hello']   
mylist                            #isntead of hello we could use mystring
['h','e','l','l','o']
```

### operations in list comprehension

```python
mylist = [num**2 for num in range(0,11) if x%2==0]
mylist
[0,4,16,36,64,100]
```

```python
celcius = [0,10,20,34.5]
fahrenheit = [((9/5)*temp + 32) for temp in celcius
fahrenheit
[32.0,50.0,68.0,94.1]
```

### **`if` & `elif` statement inside of a list comprehension**

❗remember the format will be different and can get confusing

```python
results = [ x if x%2 else 'ODD' for x in range (0,11) ]
['ODD', 1, 'ODD', 3, 'ODD', 5, 'ODD', 7, 'ODD', 9, 'ODD']
```

💡You can also use nested loops in a list comprehension 

```python
#example of nested loop as we know it

order = []

for x in  [2,4,6]: 
		 for y in [1,10,1000]:
				mylist.apppend(x*y)
order
[2,20,2000,4,40,4000,6,60,600]
```

```python
#now inside a list comprehension 

order = [x*y for in [2,4,6] for y in [1,10,1000]]
order
[2,20,2000,4,40,4000,6,60,600]
```

❗While list comprehension may be slightly less writing, you sacrafice greatly on readability.  When returning to this code, it may be difficult to read

### Python abs() function

**used to return the absolute value of a number**, i.e., it will remove the negative sign of the number.

The absolute value of a number is the number's distance from 0. 

This makes any negative number positive, while positive numbers are unaffected. 

For example, 
abs(-9) would return 9,
abs(2) would return 2.