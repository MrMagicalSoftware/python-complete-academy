# python-complete-academy



https://www.w3schools.com/python/<br>
https://www.tutorialspoint.com/python/index.htm<br>
https://www.javatpoint.com/python-tutorial<br>


**data types**


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


**Python Numbers**

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





















