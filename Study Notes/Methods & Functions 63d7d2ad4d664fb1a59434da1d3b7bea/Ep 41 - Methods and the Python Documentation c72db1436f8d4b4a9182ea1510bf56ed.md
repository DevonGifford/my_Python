# Ep. 41 - Methods and the Python Documentation

```python
lst.append(6)
lst
[1, 2, 3, 4, 5, 6]
```

Methods are essentially functions built into objects. 

Later we will learn about how to create our own objects and methods using Object Oriented Programming (OOP) and classes.

Methods perform specific actions on an object and can also take arguments, just like a function. 

Brief introduction to methods and get you thinking about overall design methods that we will touch back upon when we reach OOP in the course.

Methods are in the form:

```python
object.method(arg1,arg2,etc...)
```

💡We can think of methods as having an argument 'self' referring to the object itself. You can't see this argument but we will be using it later.

Let's take a quick look at what an example of the various methods a list has:

```python
# Create a simple list
lst = [1,2,3,4,5]
```

Fortunately, with iPython and the Jupyter Notebook we can quickly see all the possible methods using the tab key. The methods for a list are:

- append
- count
- insert
- pop
- remove
- reverse
- sort
- extend

**append() allows us to add elements to the end of a list:**

**The count() method will count the number of occurrences of an element in a list:**

```python
# Check how many times 2 shows up in the list
lst.count(2)
1
```

💡You can always use Shift+Tab in the Jupyter Notebook to get more help about the method. 
    In general Python you can use the help() function:      `help(lst.count)`