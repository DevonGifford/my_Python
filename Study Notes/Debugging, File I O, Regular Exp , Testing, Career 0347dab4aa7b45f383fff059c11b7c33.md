# Debugging, File I/O, Regular Exp., Testing, Career

Actual: 4 hours
ETA: 4 hours
Reviewed: No
Section: Section 12 to 16
Summary: No
complete: follow-up

# Debugging in Python

### Linting

Linting is the process of checking source code for programming errors, stylistic inconsistencies, and other issues that could lead to bugs or make the code harder to read or maintain. The term "lint" originally referred to a program that checked C code for potential problems, but it has since been adopted for many other programming languages, including Python.

- In Python, there are several popular linting tools, including:
    - Pylint
    - Flake8
    - Pyflakes
    - Black
        
        These tools analyze Python code and report potential issues such as unused variables, unused imports, missing docstrings, inconsistent naming conventions, and more. Linting can help improve code quality, readability, and maintainability, and is often used as part of a continuous integration or continuous delivery (CI/CD) pipeline to ensure that code changes adhere to a set of standards before they are merged into the main codebase.
        

### IDE/Editors

In addition to linting tools, many integrated development environments (IDEs) also provide built-in linting capabilities, highlighting potential issues in real time as you type your code. This can help you catch and fix issues early on, before they become larger problems.

### Reading the errors

There are about 10 - 20 most common errors - you should look them up as you come across them. 

---

## PDB *(built in module)*

Pdb stands for "Python Debugger". It is a built-in module in Python that provides a debugging environment for Python programs. It allows you to pause the execution of a program at any point and examine the values of variables and expressions in the code, helping you to track down bugs and other issues.

Pdb can be used either interactively, in which case it provides a command-line interface for interacting with the program being debugged, or it can be used programmatically, in which case you can use the **`pdb.set_trace()`** function to insert a breakpoint in your code at a specific point, and then step through the code line by line.

Here's an example of how to use pdb in interactive mode:

```python
import pdb

def my_function(x, y):
    result = x + y
    pdb.set_trace()  # insert a breakpoint
    result *= 2
    return result

print(my_function(3, 4))

```

When you run this code, it will pause at the breakpoint and drop you into the pdb debugger prompt. From here, you can examine the values of variables and expressions by typing them at the prompt, and you can also execute Python statements and commands using the full power of the Python language.

Here are some basic pdb commands:

- **`n`** or **`next`**: Execute the current line and move to the next line.
- **`s`** or **`step`**: Step into the next function call.
- **`c`** or **`continue`**: Continue execution until the next breakpoint or until the program finishes.
- **`q`** or **`quit`**: Quit the debugger.

Pdb can be a powerful tool for debugging complex programs, but it does require some familiarity with the Python language and debugging concepts.

[https://docs.python.org/3/library/pdb.html](https://docs.python.org/3/library/pdb.html)

---

### Special mention for PEP-8

PEP 8, sometimes spelled PEP8 or PEP-8, is **a document that provides guidelines and best practices on how to write Python code**.  The primary focus of PEP 8 is to improve the readability and consistency of Python code.

*It was written in 2001 by Guido van Rossum, Barry Warsaw, and Nick Coghlan*

---

[How to Write Beautiful Python Code With PEP 8 – Real Python](https://realpython.com/python-pep8/#:~:text=PEP%208%2C%20sometimes%20spelled%20PEP8,and%20consistency%20of%20Python%20code.)

# File I/O

(********input - output)********

---

### Working with files in Python

```python
my_file = open('test.txt')

print(my_file.read())

print(my_file.read()
my_file.seek(0)

print(my_file.readline())  #results in the first line
print(my_file.readline())  #results in the second line

print(my_file.lines())  #results in a list of all lines 
my_file.close()    #need to close the file (best practice)
```

remember to close your file at the end - this is a best practice

### Read, Write & Append

```python
with open('test.txt') as my_file:
	print(my_file.lines())      #This was we dont have to use the myfile.close
```

- `writing`
    
    
    ```python
    with open('test.txt', mode='r') as my_file:    # r = read
    
    with open('test.txt', mode='r + w') as my_file:  # w = write
    	text = my_filewrite('hey there')
    
    #remember that the cursor resets so if you try write something new.
    #if something exists, then we will overwrite it.
    
    ```
    
    if we just had `mode = ‘w’` and a file did not exist - it will automatically create a new file
    
    if we had `mode = 'r + w'` and the file did not exist - we will get an error
    
- `append`
    
    ```python
    with open('test.txt', mode= 'w') as my_file:  # w = write
    	text = my_filewrite('hey there')
    ```
    

### File Paths

accessing files in different folders/file_paths

```python
with open('/thisfolder/thatfolder/test.txt', mode= 'w') as my_file:  # w = write
	text = my_filewrite('hey there')
```

- `pathlib`
    
    **`pathlib`** is a Python module that provides an object-oriented interface to manipulate filesystem paths in a way that is more intuitive and safer than working with plain strings. It was introduced in Python 3.4 and provides a unified API for working with paths on different operating systems.
    
    Prior to **`pathlib`**, the **`os.path`** module was commonly used to work with filesystem paths in Python. However, **`os.path`** uses string operations to manipulate paths, which can lead to platform-specific bugs and make code harder to read and maintain.
    
    **`pathlib`** provides a more object-oriented approach, where paths are represented as objects of the **`Path`** class, and you can use various methods and properties to manipulate them. For example, you can join paths using the **`/`** operator, get the parent directory using the **`.parent`** property, and check if a path exists using the **`.exists()`** method.
    
    Here's an example of how to use **`pathlib`** to list all files in a directory:
    
    ```
    pythonCopy code
    from pathlib import Path
    
    # create a Path object for the directory to list
    directory = Path('/path/to/directory')
    
    # use the glob() method to find all files in the directory
    for file_path in directory.glob('*'):
        if file_path.is_file():
            print(file_path)
    
    ```
    
    In this example, we create a **`Path`** object for the directory we want to list, and then use the **`glob()`** method to find all files in the directory. The **`glob()`** method returns an iterator of **`Path`** objects that match the specified pattern (**`'*'`** in this case, which matches all files), and we loop through this iterator and print the path of each file.
    
    **`pathlib`** provides many other useful methods and properties for working with paths, including resolving relative paths, creating new directories or files, and more. It is a powerful tool for working with filesystem paths in Python, and is often considered a more elegant and safer alternative to the traditional **`os.path`** module.
    

### File IO Errors

common practice is to put in a try except else block 

```python
try:
	with open('my_other_file.txt', mode = 'r') as my_file:
		print(my_file.read())
except FileNotFoundError as err:
	print("Yo dude, this file dont exists my doggie")
	raise err
```

---

- exercise - offline translator
    
    ```python
    #insert activiy here
    ```
    

# Regular Expressions

### What are regular expressions?

Regular expressions, also known as regex or regexp, are a sequence of characters that define a search pattern. They are used to search for and manipulate strings of text, and are an essential tool for data processing, text mining, and data analysis.

- Regular expressions are like a language onto themselves.  There are many of them and not necessary to memorise, but need to know they exist
- Regular expressions are a powerful tool for working with text data, and can be used for a wide range of applications, including data cleaning, data extraction, and data validation.
- not unique to python

In Python, regular expressions are implemented using the **`re`** module - *This module provides a set of functions and classes that allow you to search for and manipulate text using regular expressions.*

To use regular expressions in Python, you first need to define a pattern that you want to match against. This pattern is expressed using a combination of special characters and regular characters that define the search pattern.

---

### Regular expressions are useful for:

- doing validations
    - entered right email
    - password requirements
    - string exists in text

---

- For example
    
    the regular expression pattern **`r'\d+'`** matches any sequence of one or more digits. The **`r`** at the beginning of the string indicates that this is a raw string, which means that backslashes are treated as literal characters rather than escape sequences.
    
    You can use regular expressions to search for a pattern in a string using the **`search()`** function, which returns a match object if the pattern is found, or **`None`** if it is not found. For example, to search for the pattern **`\d+`** in the string **`abc123def`**, you can use the following code:
    
    ```python
    import re
    
    match = re.search(r'\d+', 'abc123def')
    if match:
        print('Match found:', match.group())
    else:
        print('Match not found')
    
    ```
    
    This will output **`Match found: 123`**, because the pattern **`\d+`** matches the sequence of digits **`123`** in the string **`abc123def`**.
    
- More examples
    
    ```python
    import re
    
    string = 'search inside of this text please!'
    
    print (re.search('this', string))  #output:  memory 
    
    a = re.search('this', string)
    print (a.span())    #where the string occurs as a tuple
    print (a.start())   #where it starts
    print (a.end())     #wereit ends
    print (a.group())   #returns part of string where there was a match 
    ```
    
    in the example above, if the text did not exist in searched range.  ******(i.e. - ‘tHiS’)****** 
    then a would return a ‘none’ and we would have an error ‘None Type’
    
    So, what can we do?
    
    ```python
    import re
    pattern = re.compile('this')
    string = 'search inside of this text please!'
    
    a = pattern.search(string)
    b = pattern.findall(string)
    c = pattern.fullmatch(string)
    d = pattern.match(string) 
    
    print(a.group())  #return the item
    print(b)          #return all instances inside a list
    print(c)          #will only return if exact string otherwise results in none
    print(d)          #searchig the first part if extra stuff comes, its okay we get a match
    ```
    

---

### Here is a list of info

[Python RegEx](https://www.w3schools.com/python/python_regex.asp)

- Here is a tool to use when finding a regular expression:
    
    [regex101: build, test, and debug regex](https://regex101.com/)
    

<aside>
❗ `r` = raw string, this is telling the interpreter that everything after this is a raw string and therefore should not be interpreted with python interpreter

</aside>

# Testing in Python

So we use testing to see if our code is working or not.  Obviously we have covered some things that help us with this, such as;

- linting
- pyflakes
- IDE’s

But now we use something else, called Unit Testing, and this is a step above the aforementioned 

<aside>
❗ Usually run on a second file, and the consumers never sees this file.

</aside>

---

## Unit Testing

```python

```

### What is Unit Testing?

Unit testing is a software testing technique in which individual units or components of a software application are tested in isolation to ensure that they are working as expected. The purpose of unit testing is to validate that each unit or component of the application is functioning correctly and to identify and fix defects early in the development process.

In unit testing, a unit or component is typically a single function or method, or a small group of functions or methods that work together to perform a specific task. Each unit is tested in isolation using a testing framework, such as pytest or unittest, to ensure that it returns the expected output for a given set of inputs.

Unit testing is typically automated, which means that the tests can be run repeatedly and quickly, often as part of a continuous integration and deployment *(CI/CD - Continuous Integration/Continuous Development)* pipeline. This helps to ensure that any changes made to the codebase do not introduce new defects or break existing functionality.

### Unit testing has several benefits for software development, including:

1. Improved code quality: By identifying defects early in the development process, unit testing helps to ensure that the code is of high quality and meets the specified requirements.
2. Faster development cycles: Unit testing allows defects to be identified and fixed quickly, reducing the time required for development cycles.
3. Easier maintenance: Unit tests serve as a form of documentation for the code, making it easier for developers to understand and maintain the code over time.
4. Increased confidence: By ensuring that each unit of the application is functioning correctly, unit testing increases the confidence that the application as a whole is working as intended.

Overall, unit testing is an essential component of modern software development practices and is widely used to ensure that software applications are of high quality, reliable, and bug-free.

---

- Simple example
    
    here's an example of a unit test in Python using the **`unittest`** module. Suppose we have a simple function **`add_numbers()`** that takes two numbers as arguments and returns their sum:
    
    ```python
    def add_numbers(a, b):
        return a + b
    ```
    
    We can write a unit test for this function using the **`unittest`** module as follows:
    
    ```python
    import unittest
    import main
    
    class TestAddNumbers(unittest.TestCase):
        def test_add_numbers(self):
            self.assertEqual(add_numbers(2, 3), 5)
            self.assertEqual(add_numbers(-1, 1), 0)
            self.assertEqual(add_numbers(0, 0), 0)
    ```
    
    In this example, we define a class **`TestAddNumbers`** that inherits from **`unittest.TestCase`**, which provides several assert methods for testing. We then define a test method **`test_add_numbers()`** that contains three assertions, each of which tests a different scenario for the **`add_numbers()`** function.
    
    The **`self.assertEqual()`** method is used to test that the actual result of the function call is equal to the expected result. If any of the assertions fail, the test will fail and provide an error message indicating which assertion failed.
    
    To run the test, we can use the **`unittest.main()`** function:
    
    ```python
    if __name__ == '__main__':
        unittest.main()
    ```
    
    When this script is run, the **`unittest`** module will discover and run all test cases defined in the script, and report the results. If all tests pass, the output will look like:
    
    ```
    ----------------------------------------------------------------------
    Ran 1 test in 0.000s
    
    OK
    ```
    
    If any tests fail, the output will indicate which tests failed and why.
    
- Practical examples from Boot Camp
    - First try -basic example
        
        
        ```python
        #main.py
        def do_stuff(num):
            '''This is a simple function we are using to practice creating Unit Tests in another file'''
            try:
                return int(num) + 5
            except ValueError as err:
                print("There has been a ValueError here good sir!")
                return err                              #using raise here seems to result in an error when trying to run the test (ValueError)  I am not exactly sure why
        ```
        
        ![Untitled](Debugging,%20File%20I%20O,%20Regular%20Exp%20,%20Testing,%20Career%200347dab4aa7b45f383fff059c11b7c33/Untitled.png)
        
        ```python
        #unit_test.py
        import unittest
        import main
        
        class TestMain(unittest.TestCase):
            def test_do_stuff(self):
                '''Testing if integer is given'''
                test_param = 10
                result = main.do_stuff(test_param)
                self.assertEqual(result, 15)
        
            def test_do_stuff2(self):
                '''Testing if string is given'''
                test_param = 'asdf'
                result = main.do_stuff(test_param)
                self.assertIsInstance(result, ValueError)
        
        unittest.main()
        ```
        
    - Second try - more basic examples
        
        
        ```python
        #test_me.py
        def do_stuff(num):
            '''This is a simple function we are using to practice creating Unit Tests in another file'''
            try:
                if num:
                    return int(num) + 5
                else:
                    return 'Please enter a number'
            except ValueError as err:
                print("There has been a ValueError here good sir!")
                return err          
                #using raise here seems to result in an error when trying to run the test (ValueError)  I am not exactly sure why
        ```
        
        ![Untitled](Debugging,%20File%20I%20O,%20Regular%20Exp%20,%20Testing,%20Career%200347dab4aa7b45f383fff059c11b7c33/Untitled%201.png)
        
        <aside>
        ❗ `-m` - this is how we would test multiple files
        
        </aside>
        
        <aside>
        ❗ `-v` - stands for vebose
        
        </aside>
        
        ```python
        #unit_test.py
        import unittest             #we need to import the built-in module 'unittest'
        import test_me                 #we need to import the file we want to test.  (i.e. - 'test_me.py')
        
        class TestMain(unittest.TestCase):
            def test_do_stuff(self):                            #Test no.1
                '''Testing what happens if an integer is given'''
                test_param = 10
                result = test_me.do_stuff(test_param)
                self.assertEqual(result, 15)
        
            def test_do_stuff2(self):                           #Test no.2
                '''Testing what happens if a string is given'''
                test_param = 'asdf'
                result = test_me.do_stuff(test_param)
                self.assertIsInstance(result, ValueError)
        
            def test_do_stuff3(self):                           #Test no.3
                '''Testing what happens if we have a NONE type'''
                test_param = None
                result = test_me.do_stuff(test_param)
                self.assertEqual(result, 'Please enter a number')
        
            def test_do_stuff4(self):                           #Test no.4
                '''Testing what happens if we enter an empty string'''
                test_param = ''
                result = test_me.do_stuff(test_param)
                self.assertEqual(result, 'Please enter a number')
        
        if __name__ == '__main__':                                  #this is standard practice 
            unittest.main()                                         #this is how we run the test
        ```
        
        <aside>
        ❗ the `if __name__ == '__main__'` statement is for the case when you are running those files directly. By using this, it prevents an error when executing the tests using `python -m unittest` and also allows you to run just one specific test file by running `python test.py`
        
        </aside>
        
        <aside>
        ❗ if you run the command `python -m unittest` then it will search in the current directory and all subdirectories looking for files that match the pattern `test*.py` which means files that have a .py extension and begin with test. This is called test discovery and is a feature of the unittest module.
        
        </aside>
        
    - `def setUp(self):`
        - written at the start of “ Test Class “
        - if we needed certain variables before running the test - this would be easy way of adding them
        - e.g  Name = Devon, Surname = Gifford, email = devongifford@outlook.com
        
    - `def tearDown(self):`
        - run at the end of a method
        - clean up some variables or re-set some variables

---

### More information & documentation:

[Getting Started With Testing in Python – Real Python](https://realpython.com/python-testing/#more-advanced-testing-scenarios)

[unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html)

# Career of a Python Developer

- There are different routes and options to go down
    - Software Engineer
    - Python Developer
    - Data Scientist/Data Analyst
    - Research Analyst
    - Backend Developer
    - Testing/Auotomation
    
- Endorsements on LinkedIn
    
    If you are looking to improve your LinkedIn profile and have others endorse your skills, we have a private ZTM **[LinkedIn group here](https://www.linkedin.com/groups/12121940/).** LinkedIn allows you to have recruiters message you with lots of job opportunities. You can **join the group by clicking on "LinkedIn Group"** and then go ahead and endorse some of the member's skills (other people will do the same for you as they join).If you have any questions, reach out in our private Discord chat community in the **#job-hunting** channel!**UPDATE!!!** **Zero to Mastery is officially a recognized school!** What does this mean for you? It means that you can add it as an educational institution on LinkedIn as part of your profile to wow those employers *(as your education history)*. **[Check it out here](https://www.linkedin.com/school/64685953/)**. To add it to your profile:
    
    *Step 1: Go to personal LinkedIn profile*
    
    *Step 2: Scroll down to the Education section*
    
    *Step 3: Click the **+***
    
    *Step 4: Type in **Zero To Mastery Academy***
    
- [Master the Coding Interview: Data Structures + Algorithms | Udemy](https://www.udemy.com/course/master-the-coding-interview-data-structures-algorithms/)

[https://zerotomastery.io/career-paths/](https://zerotomastery.io/career-paths/)