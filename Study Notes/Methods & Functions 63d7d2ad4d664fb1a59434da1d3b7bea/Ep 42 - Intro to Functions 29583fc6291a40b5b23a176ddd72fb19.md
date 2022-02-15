# Ep.42 - Intro to Functions

Creating clean repeatable code is a key part of becoming an effective programmer.

**Functions** allow us to create blocks of code that can be easily executed many times, without needing to constantly rewrite the entire bloc of code

Formally:

useful device that groups together a set of statements so they can be run more than once. They can also let us specify parameters that can serve as inputs to the functions

## Why even use functions?

You should use functions when you plan on using a block of code multiple times.

Function will allow you to call the same block of code without having to write it multiple times.

## **Function Topics**

- def keyword
- simple example of a function
- calling a function with ()
- accepting parameters
- print versus return
- adding in logic inside a function
- multiple returns inside a function
- adding in loops inside a function
- tuple unpacking
- interactions between functions

# Ep.43 - def Function

Creating a function requires a very specific syntax including the def keyword, correct indentation, and proper structure.

[https://miro.com/app/board/uXjVOZFF0TI=/](https://miro.com/app/board/uXjVOZFF0TI=/)

```python
def say_hello():
    print('hello')
```

### Calling a function with ()

Call the function:

```python
say_hello()
hello
```

❗If you forget the parenthesis (), it will simply display the fact that say_hello is a function. Later on we will learn we can actually pass in functions into other functions! But for now, simply remember to call functions with ().

## **Accepting parameters (arguments)**

function that greets people with their name.

```python
def greeting(name):
    print(f'Hello {name}')

greeting('Jose')

Hello Jose
```

## **Using return**

so far we have only used print, but if we actually want to save the resulting variable we need to use the return keyword.

allows a function to *return* a result that can then be stored as a variable, or used in whatever manner a user wants.

example:

```python
def add_num(num1,num2):
    return num1+num2

add_num(4,5)

9

# Can also save as variable due to return
result = add_num(4,5)
print(result)

9

#  What happens if we input two strings?
add_num('one','two')
'onetwo'
```

### ❓What is the difference between ***‘return’*** vs ***‘print’***

The return keyword allows you to actually save the result of the output of a function as a variable.  The print() function simply displays the output to you, but doesn’t save it for a future use. 
some examples:

```python
def print_result(a,b):
    print(a+b)

def return_result(a,b):
    return a+b

print_result(10,5)
15

# You won't see any output if you run this in a .py script
return_result(10,5)
15
```

But what happens if we actually want to save this result for later use?

```python
my_result = print_result(20,20)
40

my_result
type(my_result)
NoneType
```

❗ Notice how `print_result()` doesn't let you actually save the result to a variable! It only prints it out, with `print()` returning None for the assignment!

```python
my_result = return_result(20,20)
my_result
40

my_result + my_result
80
```

Adding Logic to Internal Function Operations