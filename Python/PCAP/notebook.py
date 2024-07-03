'''
--- The Math Module ---
# Syntax: import math, 'invoke-module' (ceil(x), floor(x), trunc(x), sqrt(x), factorial(x))
import math

# The ceil function rounds a number up to the nearest integer.
print(math.ceil(4.2))  # Output: 5
print(math.ceil(-4.2)) # Output: -4

# The floor function - rounds a number down to the nearest integer
print(math.floor(4.7))  # Output: 4
print(math.floor(-4.7)) # Output: -5

# The trunc function removes the decimal part and returns the integer of the number
print(math.trunc(4.7))  # Output: 4
print(math.trunc(-4.7)) # Output: -4

# The factorial function returns the factorial of a given non-negative integer. The factorial of a number n is the product of all positive integers less than or equal to n.
print(math.factorial(5))  # Output: 120
print(math.factorial(3)) # Output: 6

# The sqrt function returns the square root of a given number
print(math.sqrt(16)) # Output: 4, the result is given as a float
print(math.sqrt(100)) # Output: 10

# The hypt function calculates the hypotenuse or the square root of the sum of the squares of its arguments, i.e., it returns sqrt(x*x + y*y).
print(math.hypot(3, 4)) # Output:5.0, the result is given as a float



--- The Random Module ---
# The random module in Python provide functions to generate random numbers.
import math
import random
random.seed(0)
print(random.random()) # Output: 0.8444218515250481 a randomly generated float between 0.0 - 1.0
print(random.random()) # Output: 0.0.7579544029403025 a 'difeent' randomly generated float between 0.0 - 1.0

# The choice function Returns a random element from a non-empty sequence (like a list or a tuple).
numbers = [1,2,3,4,5,6,7,8,9,10]
names = ['Alan', 'Kate', 'Mary', 'Kate', 'Jo', 'John']
print(random.choice(numbers)) # Output: 7
print(random.choice(names)) # Output: Alan



# --- The Platform Module ---
# The platform module provides functions to retrieve information such as the operating system name, version, hardware architecture, and more
# Syntax: import math, platform (x)
import math, platform
print(platform.platform()) #Output: Prints the OS of the current platform
print(platform.platform(aliased = True, terse = True)) #Output: Prints a briefer form of the system

# The machine function returns the generic name of the processor which runs the OS
print(platform.machine()) # Output: arm64
# The processor function returns the real name of the processor which runs the OS
print(platform.processor()) #Output:arm

# the Implementation returns the name of the Python implementation. The default is C Python.
print(platform.python_implementation()) #Output: CPython

# python_version_tupple returns the the major part of the version, minor part of the version and the patch.
print(platform.python_version_tuple()) #Output: ('3', '11', '7')
'''



