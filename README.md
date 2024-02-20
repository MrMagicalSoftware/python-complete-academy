# python-complete-academy



https://www.w3schools.com/python/<br>
https://www.tutorialspoint.com/python/index.htm<br>
https://www.javatpoint.com/python-tutorial<br>


## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [datatypes](#datatypes)
4. [Python Numbers](#Python Numbers)
5. [Contributing](#contributing)
6. [License](#license)

## Introduction
Briefly introduce your project here.

## Installation
Provide instructions on how to install your project.




## data types


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


## Python Numbers

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

# python operators


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

# Operatori logici 


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





____________________________

# python consitions

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





















