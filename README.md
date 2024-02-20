# python-complete-academy



https://www.w3schools.com/python/
https://www.tutorialspoint.com/python/index.htm
https://www.javatpoint.com/python-tutorial


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
















