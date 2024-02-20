# python-complete-academy



https://www.w3schools.com/python/<br>
https://www.tutorialspoint.com/python/index.htm<br>
https://www.javatpoint.com/python-tutorial<br>


## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [data_types](#data_types)
4. [Python_Numbers](#Python_Numbers)
5. [python_operators](#python_operators)
6. [Operatori logici](#Operatori_logici)
7. [python conditions](#pythonconditions)
8. [loops](#loops)
9. [Functions](#Functions)



## Introduction
Briefly introduce your project here.

## Installation
Provide instructions on how to install your project.




## data_types


Python has the following data types built-in by default, in these categories:<br>
Text Type: 	str <br>
Numeric Types: 	int, float, complex<br>
Sequence Types: 	list, tuple, range<br>
Mapping Type: 	dict<br>
Set Types: 	set, frozenset<br>
Boolean Type: 	bool<br>
Binary Types: 	bytes, bytearray, memoryview<br>
None Type: 	NoneType<br>



1. **Integer (int):**
   ```python
   age = 25
   ```

2. **Float (float):**
   ```python
   temperature = 98.6
   ```

3. **String (str):**
   ```python
   name = "John Doe"
   ```

4. **Boolean (bool):**
   ```python
   is_student = True
   ```

5. **List:**
   ```python
   numbers = [1, 2, 3, 4, 5]
   ```

6. **Tuple:**
   ```python
   coordinates = (3.5, 7.2)
   ```

7. **Set:**
   ```python
   unique_numbers = {1, 2, 3, 4, 5}
   ```

8. **Dictionary:**
   ```python
   person = {'name': 'Alice', 'age': 30, 'city': 'New York'}
   ```

9. **NoneType (None):**
   ```python
   result = None
   ```
_____________________


## Python_Numbers

```python
x = 1    # int
y = 2.8  # float
z = 1j   # complex


print(type(x))
print(type(y))
print(type(z))
```

**casting**

Casting in python is therefore done using constructor functions:

    int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)<br>
    float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)<br>
    str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals<br>



```python
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

```

```python

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

```


```python

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0' 
```

______________________________

## python_operators


Python supports a variety of operators, which are symbols or keywords that perform operations on variables and values. Here are some common types of operators in Python:

1. **Arithmetic Operators:**
   ```python
   +   # Addition
   -   # Subtraction
   *   # Multiplication
   /   # Division (float)
   //  # Division (floor)
   %   # Modulus (remainder)
   **  # Exponentiation
   ```

2. **Comparison Operators:**
   ```python
   ==  # Equal to
   !=  # Not equal to
   <   # Less than
   >   # Greater than
   <=  # Less than or equal to
   >=  # Greater than or equal to
   ```

3. **Logical Operators:**
   ```python
   and  # Logical AND
   or   # Logical OR
   not  # Logical NOT
   ```

4. **Assignment Operators:**
   ```python
   =    # Assign value
   +=   # Add and assign
   -=   # Subtract and assign
   *=   # Multiply and assign
   /=   # Divide and assign
   %=   # Modulus and assign
   //=  # Floor division and assign
   **=  # Exponentiation and assign
   ```

5. **Identity Operators:**
   ```python
   is    # True if the operands are identical objects
   is not  # True if the operands are not identical objects
   ```

6. **Membership Operators:**
   ```python
   in    # True if a value is found in the sequence
   not in  # True if a value is not found in the sequence
   ```

7. **Bitwise Operators:**
   ```python
   &   # Bitwise AND
   |   # Bitwise OR
   ^   # Bitwise XOR
   ~   # Bitwise NOT
   <<  # Left shift
   >>  # Right shift
   ```




___________________________

# Operatori_logici 


1. **and:**
   - Returns True if both conditions on either side of the operator are true.
   ```python
   x = True
   y = False
   result = x and y  # result is False
   ```

2. **or:**
   - Returns True if at least one of the conditions on either side of the operator is true.
   ```python
   x = True
   y = False
   result = x or y  # result is True
   ```

3. **not:**
   - Returns True if the condition following the operator is false, and vice versa.
   ```python
   x = True
   result = not x  # result is False
   ```


```python
a = True
b = False

# Logical AND
result_and = a and b  # False

# Logical OR
result_or = a or b  # True

# Logical NOT
result_not = not a  # False
```


**user input**

In Python, you can use the `input()` function to get input from the user. The `input()` function takes a string as an argument, which is used as the prompt for the user. Here's a simple example:

```python
# Get user input and store it in a variable
user_name = input("Enter your name: ")

# Display the user's input
print(f"Hello, {user_name}!")
```

In this example, the `input("Enter your name: ")` statement prompts the user to enter their name. The entered value is then stored in the variable `user_name`, and the program displays a greeting using that input.

Keep in mind that the `input()` function always returns a string. If you need to get numeric input, you may need to convert the input to the desired data type (e.g., using `int()` for integers or `float()` for floating-point numbers).

```python
# Get numeric input from the user
user_age = int(input("Enter your age: "))
# Now user_age is an integer

# Perform some operation with the user's input
future_age = user_age + 5
print(f"In 5 years, you will be {future_age} years old.")
```

Remember to handle exceptions when converting user input to other data types, as the user might input something that cannot be converted.

```python
# Safely get numeric input from the user
try:
    user_height = float(input("Enter your height in meters: "))
except ValueError:
    print("Invalid input. Please enter a numeric value for height.")
```

This `try-except` block catches a `ValueError` if the user enters something that cannot be converted to a floating-point number.

Always validate and handle user input appropriately to ensure the robustness of your program.




____________________________

# python conditions

In Python, conditions are used to control the flow of a program by executing different code blocks based on whether a certain condition evaluates to True or False. The basic syntax for a conditional statement in Python is the `if` statement, and you can also use `elif` (short for "else if") and `else` to handle multiple conditions.


You can use relational operators (such as `<`, `>`, `<=`, `>=`, `==`, `!=`) 
and logical operators (`and`, `or`, `not`) to create conditions based on comparisons and boolean values.


Here's a simple example:

```python
# Example 1: Basic if statement
x = 10
if x > 5:
    print("x is greater than 5")

# Example 2: if-else statement
y = 3
if y > 5:
    print("y is greater than 5")
else:
    print("y is not greater than 5")

# Example 3: if-elif-else statement
z = 7
if z > 10:
    print("z is greater than 10")
elif z > 5:
    print("z is greater than 5 but not 10")
else:
    print("z is not greater than 5")

# Example 4: Nested if statements
a = 15
if a > 10:
    print("a is greater than 10")
    if a > 20:
        print("a is also greater than 20")
    else:
        print("a is not greater than 20")

# Example 5: Using logical operators
b = 25
if b > 10 and b < 30:
    print("b is between 10 and 30")

# Example 6: Ternary conditional expression
c = 8
result = "Even" if c % 2 == 0 else "Odd"
print(f"The number {c} is {result}")
```
______________________________________


# Loops


In Python, loops are used to repeatedly execute a block of code until a certain condition is met. There are two main types of loops in Python: `for` and `while`.

1. **`for` Loop:**
   The `for` loop is used to iterate over a sequence (such as a list, tuple, string, or range) or other iterable objects.

   ```python
   # Example 1: Iterate over a list
   fruits = ['apple', 'banana', 'orange']
   for fruit in fruits:
       print(fruit)

   # Example 2: Iterate over a range of numbers
   for i in range(5):
       print(i)
   ```

2. **`while` Loop:**
   The `while` loop is used to repeatedly execute a block of code as long as a specified condition is true.

   ```python
   # Example 1: Simple while loop
   count = 0
   while count < 5:
       print(count)
       count += 1

   # Example 2: Using a while loop to iterate over a list
   numbers = [1, 2, 3, 4, 5]
   index = 0
   while index < len(numbers):
       print(numbers[index])
       index += 1
   ```

3. **Loop Control Statements:**
   - `break`: Terminates the loop prematurely.
   - `continue`: Skips the rest of the code inside the loop for the current iteration.
   - `else`: Executed when the loop condition becomes False (applies to both `for` and `while` loops).

   ```python
   # Example: Using break and continue
   for i in range(10):
       if i == 3:
           break  # Exit the loop when i is 3
       if i == 1:
           continue  # Skip the rest of the code for i equals 1
       print(i)
   else:
       print("Loop finished")
   ```

___________________________________________


# Functions


In Python, a function is a block of reusable code that performs a specific task. Functions allow you to organize code into modular components, making it easier to read, understand, and maintain. Here's a basic overview of functions in Python:

### Defining a Function:

```python
def greet(name):
    """This function prints a greeting."""
    print(f"Hello, {name}!")

# Calling the function
greet("Alice")
```

In this example, we define a function called `greet` that takes a parameter `name` and prints a greeting. The triple-quoted string within the function is a docstring, providing documentation for the function.

### Function Parameters:

Functions can have parameters (input values) that allow them to accept different values when called.

```python
def add_numbers(x, y):
    """This function adds two numbers."""
    result = x + y
    return result

# Calling the function with arguments
sum_result = add_numbers(3, 5)
print("Sum:", sum_result)
```

### Return Statement:

Functions can return values using the `return` statement. If there is no `return` statement or if it is without an expression, the function returns `None` by default.

```python
def square(x):
    """This function returns the square of a number."""
    return x ** 2

# Calling the function and using the returned value
result = square(4)
print("Square:", result)
```

### Default Parameters:

You can set default values for parameters, making them optional when calling the function.

```python
def greet_person(name, greeting="Hello"):
    """This function greets a person with a custom or default greeting."""
    print(f"{greeting}, {name}!")

# Calling the function with and without the second argument
greet_person("Bob")             # Uses default greeting
greet_person("Alice", "Hi")     # Uses custom greeting
```

### Variable Number of Arguments:

You can use `*args` to pass a variable number of non-keyword arguments to a function.

```python
def sum_numbers(*args):
    """This function sums up all the given numbers."""
    total = sum(args)
    return total

# Calling the function with different numbers of arguments
result1 = sum_numbers(1, 2, 3)
result2 = sum_numbers(4, 5, 6, 7)
print("Sum 1:", result1)
print("Sum 2:", result2)
```









____________________________

# String 

```python

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


b= '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(b) 

```

**Strings are Arrays**
```python

a = "Hello, World!"
print(a[1])
```

**Looping Through a String**
```python

for x in "banana":
  print(x)
```


**String Length**

```python

a = "Hello, World!"
print(len(a))
```

**Check String**

To check if a certain phrase or character is present in a string, we can use the keyword in.


txt = "The best things in life are free!"
print("free" in txt)
_________________________________________


**Check String**

```python

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
```


________________________


In Python, classes and objects provide a way to structure and organize code in an object-oriented programming (OOP) paradigm. 
Here's a basic overview of classes and objects in Python:

### Classes:

A class is a blueprint for creating objects. It defines the attributes (characteristics) and methods (functions) that the objects created from the class will have. Here's a simple example:

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof!")

# Creating an instance (object) of the Dog class
my_dog = Dog(name="Buddy", age=3)

# Accessing attributes and calling methods
print(f"My dog's name is {my_dog.name} and is {my_dog.age} years old.")
my_dog.bark()
```

In this example, `Dog` is a class with attributes `name` and `age`, and a method `bark`. The `__init__` method is a special method called a constructor, which is executed when an object is created.

### Objects:

Objects are instances of a class. They represent specific instances of the class and can have unique attribute values. In the example above, `my_dog` is an object of the `Dog` class.

### Inheritance:

Inheritance allows a class (subclass) to inherit the attributes and methods of another class (superclass). It promotes code reusability.

```python
class Cat(Dog):
    def purr(self):
        print("Purr!")

# Creating an instance of the Cat class
my_cat = Cat(name="Whiskers", age=2)

# Inherited attributes and methods
print(f"My cat's name is {my_cat.name} and is {my_cat.age} years old.")
my_cat.bark()  # Inherited method
my_cat.purr()  # Additional method
```

### Encapsulation:

Encapsulation is the concept of restricting access to certain attributes or methods of a class. In Python, this is achieved using private and protected attributes.

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius  # Protected attribute

    def _calculate_area(self):  # Protected method
        return 3.14 * self._radius**2

# Creating an instance of the Circle class
my_circle = Circle(radius=5)

# Accessing protected attribute and method
print(f"Circle radius: {my_circle._radius}")
print(f"Circle area: {my_circle._calculate_area()}")
```

```python

class Employee:
   def __init__(self, name, age, salary):
      self.name = name # public variable
      self.__age = age # private variable
      self._salary = salary # protected variable
   def displayEmployee(self):
      print ("Name : ", self.name, ", age: ", self.__age, ", salary: ", self._salary)

e1=Employee("Bhavana", 24, 10000)

print (e1.name)
print (e1._salary)
print (e1.__age)
```


### Polymorphism:

Polymorphism allows objects of different classes to be treated as objects of a common base class. This can be achieved through method overriding.

```python
class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# Using polymorphism
def animal_sound(animal):
    animal.make_sound()

my_dog = Dog()
my_cat = Cat()

animal_sound(my_dog)  # Outputs "Woof!"
animal_sound(my_cat)  # Outputs "Meow!"
```

________________________

# try except 

In Python, the `try` and `except` blocks are used for exception handling. Exception handling allows you to catch and handle errors or exceptional situations in your code, preventing the program from terminating abruptly. Here's the basic syntax:

```python
try:
    # Code that may raise an exception
    result = 10 / 0  # This will raise a ZeroDivisionError
    # You can also explicitly raise an exception using the "raise" keyword
    # raise ValueError("This is a custom exception")

except ZeroDivisionError:
    # Code to handle the specific exception (ZeroDivisionError in this case)
    print("Cannot divide by zero!")

except Exception as e:
    # Code to handle other exceptions (all exceptions that inherit from the base Exception class)
    print(f"An error occurred: {e}")

else:
    # Optional: Code to be executed if no exception is raised
    print("Division successful!")

finally:
    # Optional: Code to be executed whether an exception is raised or not
    print("This block always runs, regardless of exceptions.")
```

Explanation of each block:

- The `try` block contains the code that may raise an exception.
- The `except` block catches and handles specific exceptions. Multiple `except` blocks can be used for different types of exceptions.
- The `else` block is optional and is executed if no exception occurs in the `try` block.
- The `finally` block is optional and is always executed, regardless of whether an exception occurred or not.

You can catch specific exceptions or use a more general `Exception` to catch all exceptions. It's generally a good practice to be as specific as possible when catching exceptions to avoid catching unexpected errors.

Here's an example using a try-except block with file handling:

```python
try:
    # Attempt to open a file
    file = open("example.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found!")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    if 'file' in locals():
        file.close()
```

This example attempts to open a file, reads its content, and prints it. If the file is not found, it catches the `FileNotFoundError`. The `finally` block ensures that the file is closed, whether an exception occurred or not.


















