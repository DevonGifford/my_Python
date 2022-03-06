# Modules in Python

Actual: 5 hours
ETA: 3 hours
Reviewed: No
Section: +extra, Section 11
Summary: Yes
complete: Done

# Modules in Python

<aside>
🤖 In Python, a module is a file that contains a collection of related functions, classes, and variables that can be used in other Python programs. 

Modules allow you to organize your code into logical units and reuse it in different programs.

</aside>

### To use a module in your code

you need to import it using the **`import`** statement. For example, to import the **`math`** module, which contains various mathematical functions, you would write:

```python
import math
```

Once you have imported a module, you can access the functions, classes, and variables defined in the module using the dot notation. For example, to use the **`sqrt()`** function from the **`math`** module, you would write:

```python
import math

x = math.sqrt(25)
print(x)  # 5.0
```

---

You can also import specific functions, classes, or variables from a module using the **`from`** keyword. For example, to import the **`sqrt()`** function from the **`math`** module, you could write:

```python
from math import sqrt

x = sqrt(25)
print(x)  # 5.0
```

---

- My notes from lectures
    - Modules allow us to use and organise “multiple” files - we can do this with modules
    - Used accross many programming languages
    - When writing modules, we use the same format as variables (lower and snake case)
    - Big projects need a way to work with many many files, thus need to be able to communicate
    - therefore first lines are always import statements

---

Modules are an important tool for organizing and reusing code in Python. 

They allow you to break your code up into logical units and use them in different programs, making it easier to manage and maintain your codebase.

# Packages in Python

<aside>
🤖 In Python, a package is a collection of modules that are organized into a hierarchy of directories. Packages allow you to group related modules together and structure your code in a logical way.

</aside>

### To use a package in your code

---

You need to import it using the **`import`** statement. For example, to import the **`math`** package, which contains various mathematical functions, you would write:

```python
import math
```

Once you have imported a package, you can access the modules and functions defined in the package using the dot notation. For example, to use the **`sqrt()`** function from the **`math`** package, you would write:

```python
import math

x = math.sqrt(25)
print(x)  # 5.0
```

You can also import specific modules or functions from a package using the **`from`** keyword. For example, to import the **`sqrt()`** function from the **`math`** package, you could write:

```python
from math import sqrt

x = sqrt(25)
print(x)  # 5.0
```

- My notes from lectures
    - A package is a folder, with multiple modules

---

Packages are an important tool for organizing and reusing code in Python. 

They allow you to group related modules together and structure your code in a logical way, making it easier to manage and maintain your codebase.

# Importing with Python

<aside>
🤖 There are several ways to import modules in Python, each with its own benefits and use cases. Here are some of the most common ways to import modules in Python:

</aside>

### **`import module_name`:**

---

This is the most basic form of importing a module. It allows you to import the module and use its functions, classes, and variables using the dot notation. 

For example:

```python
import math

x = math.sqrt(25)
print(x)  # 5.0
```

---

### **`from module_name import function_name`:**

---

This form of importing allows you to import a specific function from a module and use it directly in your code without using the dot notation. 

For example:

```python
from math import sqrt

x = sqrt(25)
print(x)  # 5.0
```

---

### **`from module_name import function_name as fn`:**

---

This form of importing allows you to import a specific function from a module and use it directly in your code under a different name. This can be useful if you want to avoid naming conflicts or if you want to use a shorter or more descriptive name for the function. 

For example:

```python
from math import sqrt as square_root

x = square_root(25)
print(x)  # 5.0
```

---

### **`from module_name import *`:**

---

This form of importing allows you to import all functions, classes, and variables from a module and use them directly in your code without using the dot notation. This can be convenient, but it is generally not recommended, as it can lead to naming conflicts and make it difficult to understand where imported symbols are coming from. For example:

```python
from math import *

x = sqrt(25)
print(x)  # 5.0
```

---

### **`import module_name as mn`:**

---

This form of importing allows you to import a module under a different name, which can be useful if you want to avoid naming conflicts or if you want to use a shorter or more descriptive name for the module. 

For example:

```python
import math as m

x = m.sqrt(25)
print(x)  # 5.0
```

---

---

These are just a few examples of the many built-in modules in Python. There are many other built-in modules available, each providing a specific set of functions and features. You can find a complete list of the built-in modules in the Python documentation.

---

<aside>
🤖 There are several ways to import packages in Python, each with its own benefits and use cases. Here are some of the most common ways to import packages in Python:

</aside>

### **`import package_name`**:

This is the most basic form of importing a package. It allows you to import the package and use its modules, functions, classes, and variables using the dot notation. For example:

```
Copy code
import math

x = math.sqrt(25)
print(x)  # 5.0

```

### **`from package_name import module_name`**:

This form of importing allows you to import a specific module from a package and use it directly in your code without using the dot notation. For example:

```
Copy code
from math import sqrt

x = sqrt(25)
print(x)  # 5.0

```

### **`from package_name.module_name import function_name`**:

This form of importing allows you to import a specific function from a module within a package and use it directly in your code without using the dot notation. For example:

```
Copy code
from math.trigonometry import sin

x = sin(0.5)
print(x)  # 0.4794

```

# `__name__`

---

<aside>
🤖 In Python, the **`__name__`** variable is a built-in variable that contains the name of the current module. It is commonly used to check whether a module is being run directly or imported from another module.

</aside>

The value of **`__name__`** is set to **`'__main__'`** when a module is being run directly. This can be used to create a main function that is only executed when the module is run directly, but not when the module is imported by another module.

Here is an example of using **`__name__`** to create a main function:

```python
def main():
    # code to be executed when the module is run directly
    print("This module is being run directly")

if __name__ == '__main__':
    main()
```

<aside>
🤔 In this example, the **`main()`** function is only called when the module is run directly, as the **`if`** statement checks whether **`__name__`** is equal to **`'__main__'`**. If the module is imported by another module, the **`if`** statement is False and the **`main()`** function is not called.

</aside>

---

The **`__name__`** variable is also set to the name of the module when the module is imported, so it can be used to determine which module is being imported. For example:

```python
import my_module

if __name__ == 'my_module':
    print("The my_module module is being imported")
```

<aside>
🤔 In this example, the **`if`** statement will be True when the **`my_module`** module is imported, and False when it is run directly.

</aside>

---

The **`__name__`** variable can be useful for creating modular and reusable code, as it allows you to control the behavior of a module depending on whether it is being run directly or imported by another module.

---

# Built-in Modules

There are many built-in modules in Python that provide a wide range of functions and features. Here are some of the most popular and widely used built-in modules in Python:

---

1. **`math`**: This module provides various mathematical functions, such as trigonometric functions, logarithmic functions, and functions for working with complex numbers.
2. **`random`**: This module provides functions for generating random numbers and shuffling sequences.
3. **`os`**: This module provides functions for interacting with the operating system, such as functions for reading and writing files, creating and deleting directories, and executing system commands.
4. **`sys`**: This module provides functions for interacting with the Python interpreter, such as functions for accessing command-line arguments and interacting with the standard input, output, and error streams.
5. **`datetime`**: This module provides functions for working with dates and times, such as functions for creating and manipulating date and time objects and formatting and parsing date and time strings.
6. **`json`**: This module provides functions for reading and writing JSON data, which is a popular data interchange format.

These are just a few examples of the many built-in modules in Python. There are many other built-in modules available, each providing a specific set of functions and features. You can find a complete list of the built-in modules in the Python documentation.

# Python Package Index [PyPI] or [PIP]

The Python Package Index (PyPI) is a repository of open-source software for the Python programming language. It is the official package repository for Python, and it contains a large collection of third-party packages that can be easily installed and used in your Python programs.

PyPI is maintained by the Python Software Foundation, and it is the primary source for a wide range of packages that cover a wide variety of applications and domains, including scientific computing, data analysis, machine learning, web development, and many others.

To use PyPI, you can use the **`pip`** package manager, which is included with Python by default. **`pip`** allows you to easily install packages from PyPI and manage their dependencies. For example, to install the **`numpy`** package, which is a popular library for scientific computing, you can use the following command:

```python

pip install numpy

```

You can also use **`pip`** to update and remove packages, as well as to list the packages that are installed on your system.

PyPI is an essential resource for Python developers, as it makes it easy to find and use a wide range of third-party packages that can save time and effort when developing Python programs.

### PIP Install

**`pip`** is a package manager for Python that is used to install and manage third-party packages from the Python Package Index (PyPI). **`pip`** is included with Python by default in Python 2.7.9 and later and Python 3.4 and later, so you may already have it installed on your system.

- To check if **`pip`** is installed on your system, try run the following command in terminal:
    
    ```
    Copy code
    pip --version
    
    ```
    
    If **`pip`** is installed, this command will print the version number of **`pip`** that is installed on your system. If **`pip`** is not installed, you will see an error message indicating that the **`pip`** command is not found.
    
- If **`pip`** is not installed on your system, you can install it by following these steps:
    1. Download the latest version of Python from the official Python website (**[https://www.python.org/downloads/](https://www.python.org/downloads/)**). Make sure to download a version that is compatible with your operating system.
    2. Install Python by following the instructions provided with the installer. Make sure to select the option to add Python to your system path during the installation process.
    3. Once Python is installed, you can use the **`pip`** command to install packages from PyPI. For example, to install the **`numpy`** package, you can use the following command:
        
        ```
        Copy code
        pip install numpy
        
        ```
        

# Virtual Environments

- What are Virtual Environments:
    
    Virtual environments in Python are isolated Python environments that allow you to install and manage packages without affecting the global Python installation or packages installed in other virtual environments. *This is especially useful when working on multiple projects that require different versions of Python or different sets of packages.*
    
    A virtual environment contains its own Python interpreter, as well as a set of packages installed using the **`pip`** package manager. 
    
    When you activate a virtual environment, the shell environment is updated to use the Python interpreter and packages installed in that environment.
    
- To create a virtual environment:
    
    you can use the **`venv`** module, which is included with Python 3.3 and later. Here's an example of how to create and activate a virtual environment:
    
    1. Open a terminal or command prompt.
    2. Navigate to the directory where you want to create the virtual environment.
    3. Run the following command to create a virtual environment named **`myenv`**:
        
        ```
        Copy code
        python3 -m venv myenv
        
        ```
        
        This will create a new directory named **`myenv`** in the current directory, containing a Python interpreter and some other files.
        
    4. To activate the virtual environment, run the following command:
        
        ```
        bashCopy code
        source myenv/bin/activate
        
        ```
        
        This will update the shell environment to use the Python interpreter and packages installed in the **`myenv`** virtual environment.
        
    
    Once you have activated a virtual environment, you can use **`pip`** to install packages just like you would in a global Python installation. When you're finished working with the virtual environment, you can deactivate it by running the following command:
    
    ```
    Copy code
    deactivate
    
    ```
    
    This will restore the shell environment to its previous state.
    

# Useful Modules

- `array`
    
    The **`array`** module in Python provides a way to create and manipulate arrays, which are similar to lists but are more efficient for storing and manipulating large amounts of numerical data.
    
    Arrays in the **`array`** module are homogeneous, meaning that all elements in the array must be of the same data type. The supported data types include integers, floating-point numbers, and bytes.
    
    Here's an example of how to create an array of integers using the **`array`** module:
    
    ```python
    
    import array
    
    # Create an array of integers
    arr = array.array('i', [1, 2, 3, 4, 5])
    
    # Print the array
    print(arr)  # array('i', [1, 2, 3, 4, 5])
    
    ```
    
    In this example, we created an array of integers by passing the data type code **`'i'`** to the **`array`** function, followed by a list of integers. The **`'i'`** data type code specifies that the array should store signed integers.
    
    Once an array is created, you can manipulate its elements using the same indexing and slicing syntax as a list:
    
    ```python
    
    # Change the value of an element
    arr[0] = 10
    
    # Print a slice of the array
    print(arr[2:4])  # array('i', [3, 4])
    
    ```
    
    The **`array`** module also provides several methods for manipulating arrays, such as **`append`**, **`extend`**, and **`remove`**. For example:
    
    ```python
    
    # Append a value to the end of the array
    arr.append(6)
    
    # Extend the array with another array
    arr.extend([7, 8, 9])
    
    # Remove the first occurrence of a value from the array
    arr.remove(3)
    
    # Print the modified array
    print(arr)  # array('i', [10, 2, 4, 5, 6, 7, 8, 9])
    
    ```
    
    Overall, the **`array`** module is a useful tool for efficiently storing and manipulating large amounts of numerical data in Python.
    
- `datetime`
    
    The **`datetime`** module in Python provides classes for working with dates, times, and time intervals. The **`datetime`** module includes the following classes:
    
    - **`datetime.date`**: Represents a date (year, month, day).
    - **`datetime.time`**: Represents a time of day (hour, minute, second, microsecond).
    - **`datetime.datetime`**: Represents a date and time (year, month, day, hour, minute, second, microsecond).
    - **`datetime.timedelta`**: Represents a duration or difference between two dates or times.
    
    Here are some examples of how to use the **`datetime`** module:
    
    ```python
    Import datetime
    
    # Get the current date and time
    now = datetime.datetime.now()
    print(now)  # 2022-01-01 12:30:45.123456
    
    # Create a date object for a specific date
    d = datetime.date(2022, 1, 1)
    print(d)  # 2022-01-01
    
    # Create a time object for a specific time
    t = datetime.time(12, 30, 45, 123456)
    print(t)  # 12:30:45.123456
    
    # Create a datetime object for a specific date and time
    dt = datetime.datetime(2022, 1, 1, 12, 30, 45, 123456)
    print(dt)  # 2022-01-01 12:30:45.123456
    
    # Calculate the difference between two dates or times
    delta = datetime.timedelta(days=1)
    tomorrow = now + delta
    print(tomorrow)  # 2022-01-02 12:30:45.123456
    
    ```
    
    The **`datetime`** module also includes many methods for manipulating dates, times, and time intervals. For example, you can format a date or time as a string using the **`strftime`** method:
    
    ```python
    # Format a datetime object as a string
    formatted = dt.strftime('%Y-%m-%d %H:%M:%S')
    print(formatted)  # 2022-01-01 12:30:45
    
    ```
    
    You can also parse a string into a datetime object using the **`strptime`** method:
    
    ```python
    
    # Parse a string into a datetime object
    parsed = datetime.datetime.strptime('2022-01-01 12:30:45', '%Y-%m-%d %H:%M:%S')
    print(parsed)  # 2022-01-01 12:30:45
    
    ```
    
    Overall, the **`datetime`** module is a powerful tool for working with dates, times, and time intervals in Python.