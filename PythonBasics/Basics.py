# This is a comment
"""
This are Multi-line comments
"""

# importing the libraries

import sys
import math
import random
import threading
import time
from functools import reduce

"""
print('HELLO WORLD...!!!')
"""

"""
# Primitive DataTypes:
# integers, floats, complex numbers, strings, booleans

# Variable Declaration
a = 5
b = "This is a String"
c = 'This is also a String'
d = 5.5
e = True
f = 'z'

print(a, b, c, d, e, f)
"""

"""
# Variable declaration with it's types
a2: int = 5
b2: str = "This is a String"
c2: str = 'This is also a String'
d2: float = 5.5
e2: bool = True
f2: chr = 'z'

print(a2, b2, c2, d2, e2, f2)
"""

"""
# Reading input from Console
name = input("What is your name ???\n")
print("Hello: ", name)
"""
"""
# Multi-line Expressions
sum1 = (
    1 + 2
    + 3
)
print("Sum1", sum1)

sum2 = 1 + 2 \
    + 3
print("Sum2", sum2)
"""

"""
# Multiple Expressions in one line
v1 = 4; v1 += 2
print(v1)
"""

"""
# Assigning Same Value to multiple variables
val1 = val2 = 5
print("val1:", val1)
print("val2:", val2)
"""

"""
# To get the type of the Variable
test = 10
print("10 is of :", type(test))

# Maximum integer size that Python supports
print(sys.maxsize)

# Maximum float size that Python supports
print(sys.float_info.max)

# Float values up to 15 digit precision gives correct value beyond that gives wrong values
f1 = 1.1111111111111111
f2 = 1.1111111111111111
f3 = f1 + f2
print("f1 + f2 =", f3)

# Complex Numbers
c1 = 5 + 6j
print("Complex Number:", c1)

# Escape Sequence
escStr = "This is an String with Escape sequences \n \" \\ \t \'"
print(escStr)

escStr2 = '''This is an String with Escape sequences \n \" \\ \t \''''
print(escStr2)
"""

'''
escStr3 = """This is an String with Escape sequences \n \" \\ \t \'"""
print(escStr3)
'''

"""
# Type Casting
# Float to Integer
print("CAST1:", type(int(5.4)))
# Float to String
print("CAST2:", type(str(5.4)))
# Integer to Float
print("CAST3:", type(float(5)))
# This also convert into String
print("CAST4:", type(chr(50)))
# Converts Single Character to an Integer
print("CAST5:", type(ord('a')))
"""

"""
# Printing the Result with the required separator
print(4, 9, 1990, sep="/")
print(4, 9, 1990, sep="-")
print(4, 9, 1990, sep=":")
print(4, 9, 1990, sep="\t")
"""

"""
# Printing values with the required end line string
print("This line don't have new line character at the end of the line", end="")
print("THIS IS THE NEXT LINE")
"""

"""
# Printing different types of values
print("\n%4d, %s, %.2f %c" % (10, "TEST", 1.2345, 'A'))
print("\n%04d, %s, %.2f %c" % (10, "TEST", 1.2345, 'A'))
"""

# Arithmetic Operations
"""
print("10 + 4:", 10 + 4)
print("10 - 4:", 10 - 4)
print("10 * 4:", 10 * 4)
print("10 / 4:", 10 / 4)
print("10 % 4:", 10 % 4)
print("10 ** 4:", 10 ** 4)
print("10 // 4:", 10 // 4)

i1 = 5
i1 += 2
print("Final i1 =", i1)
"""

"""
# Math Functions
print("abs(-1):", abs(-1))
print("max(3,5):", max(3,5))
print("min(3,5):", min(3,5))
print("pow(3,5):", pow(3,5))
print("math.ceil(3.5):", math.ceil(3.5))
print("math.floor(3.5):", math.floor(3.5))
print("round(3.5):", round(3.5))
print("exp(1):", math.exp(1))
print("math.sqrt(9):", math.sqrt(9))
print("log(100):", math.log(100, 10))
print("radians(0):", math.radians(0))
print("degrees(pi):", math.degrees(math.pi))
"""

"""
# Random Number
print("Random number in 1 to 100:", random.randint(1, 101))
print("Random number in 1 to 100:", random.randint(1, 101))
print("Random number in 1 to 100:", random.randint(1, 101))
"""

"""
# NaN - Not a Number
# Inf - Infinity
print("Infinity > 0:", (math.inf > 0))
print("Infinity - Infinity:", (math.inf - math.inf))
print("Infinity - 100:", (math.inf - 100))
"""

"""
# Conditional Statements - if, if else, nested if, else if ladder
age = 60

# Logical Operators: <, >, <=, >=, ==, !=
if age < 18:
    print("Person is a Minor")
elif age > 18:
    print("Person is a Major")
elif age == 18:
    print("Person is of age 18")
else:
    print("Not a correct age")

# Relational Operators
if age <= 5:
    print("Kid")
elif (age > 5) and (age < 18):
    print("Minor")
elif (age >= 18) and (age < 30):
    print("Youth")
elif (age >= 30) and (age <= 45):
    print("Middle Aged")
else:
    print("Senior Citizen")
"""

"""
# Ternary Operation in Python
# condition_true if condition else condition_false
personAge = 21
person = "Major" if personAge > 10 else "Minor"
print("Person is :", personAge)
"""
















































