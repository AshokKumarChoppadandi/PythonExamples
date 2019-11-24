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

"""
# Strings
# In Python, Strings can be declared with single or doubles, triple single or double quotes

str1 = 'This is string with single quotes'
str2 = "This is string with double quotes"
str3 = '''This is a string with triple single quotes'''
"""
'''
str4 = """This is a string with triple double quotes"""
print(str1)
print(str2)
print(str3)
print(str4)
'''
"""
# Ignoring escape sequences in Strings
escstr1 = r"This is a string without escape sequence \t\n"
print(escstr1)

# Appending the Strings
string1 = "test1"
string2 = "test2"
print(string1 + " " + string2)

charString = "Hello World"

# Length of the String
print("Length :", len(charString))

# Char at index 0
print("charString[0] :", charString[0])

# Last Char
print("charString[-1] :", charString[-1])

# Char from index 0 to 2 but not 3
print("charString[0:2] :", charString[0:3])

# Every Other character in the String - Print first char and skip the next
print("Every Other Char :", charString[0:-1:2])

# Every Other two characters in the String - Print first char and skip next two
print("Every Other Two Char :", charString[0:-1:3])

# Replace the chars in the string
charString2 = charString.replace("Hello", "Goodbye")
print(charString2)

# Chars 0 till index 8 and chars from index 9 to last
charString3 = charString2[:8] + "w" + charString2[9:]
print(charString3)

# Find a String exists in the String
print("world" in charString3)

# Find a String not exists in the String
print("world" not in charString3)

# Find the index of the String
print("Index of world :", charString3.find("world"))

# Trim / Strip empty spaces in Strings
print("     Hello World    ".strip())

# lstrip
print("     Hello World".lstrip())

# rstrip
print("Hello World    ".rstrip())

# Concat list of Strings
print(" ".join(["Hello", "World", "Welcome"]))

# Splitting Strings
print("HELLO WORLD WELCOME".split(" "))

# 'f' allows us to substitute the value of the variables and do calculations
int1 = int2 = 5
print(f"{int1} + {int2} = {int1 + int2}")

# Converting String to lower case
print("HELLO".lower())

# Converting String to upper case
print("hello".upper())

# Check string whether it is a AlphaNumeric
print("ABC 123".isalnum())
print("ABC123".isalnum())

# Check string whether it is a Alphabets
print("ABC D".isalpha())
print("ABCD".isalpha())
# Check string whether it is a Digit
print("123 4".isdigit())
print("1234".isdigit())
"""

"""
# Lists - Mutable pieces of Data
list1 = [1, "test", 3.14, False]

# Length of the list
print("Length :", len(list1))
# First value of the list
print("First Value :", list1[0])
# Last value of the list
print("Last Value :", list1[-1])

# Replacing index  1 value with 'TEST' string
list1[1] = "TEST"
print(list1)

# Replacing indices 1 and 2 but not 3 with values 'TEST1' and 100
list1[1:3] = ["TEST1", 100]
print(list1)

# Adding new elements from index 2 without disturbing the other values
list1[2:2] = ["TEST123", 3.143]
print(list1)

# Adding elements using insert at index 0 without disturbing the other values
list1.insert(0, "One")
print(list1)

# Creating a New list by adding two lists
list2 = list1 + [1, 2, 3, "TEST456"]
print(list2)

# Removing an element from last
print(list2.pop())

# Removing an element with an index value is 0
print(list2.pop(0))

# Removing an element with name
print(list2.remove("TEST123"))
print(list2)

# Multi dimensional list
list3 = [[1, 2], [3, 4], [5, 6]]
print(list3[0])
print(list3[1])
print(list3[2])
print(list3[0][0])
print(list3[0][1])
print(list3[1][0])
print(list3[1][1])
print(list3[2][0])
print(list3[2][1])

list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Find a value exists in the list
print("5 Exists :", 5 in list4)

# Value not exists in the list
print("15 Not Exists :", 15 not in list4)

# First value
print("First Value :", list4[0])

# Second value
print("Last Value :", list4[-1])

# Values from index 0 to 2 but not including 3
print("Last Value :", list4[0:3])

# Printing Every other value in the list
print("Every other value :", list4[0:-1:2])

# Reversing the list
print("Reverse List :", list4[::-1])

# Minimum value from the list
print("Minimum Value :", min(list4))

# Maximum value from the list
print("Maximum Value :", max(list4))
"""

"""
# Loops

# while loop
# Print number from 1 to 5
w1 = 1
while w1 < 5:
    print(w1)
    w1 += 1

# Print only even number from 1 to 10
w2 = 1
while w2 <= 10:
    if w2 % 2 == 0:
        print(w2)
    w2 += 1


# Print only even number from 1 to 8 - using break and continue
w3 = 1
while w3 <= 10:
    if w3 % 2 == 0:
        print(w3)
    elif w3 == 8:
        break
    else:
        w3 += 1
        continue
    w3 += 1


# Iterating through the list
wList1 = [1, 2, 3, 4, 5, 6]
# Destructive approach

while len(wList1):
    print(wList1.pop(0))

# Non Destructive approach
wList2 = [1, 2, 3, 4, 5, 6]
index = 0
listLength = len(wList2)

while index < listLength:
    print(wList2[index])
    index += 1
"""
"""
# For Loop
# Iterating through range of numbers
for x in range(1, 5):
    print(x, end="")
print()

fList1 = [1, "TEST", 100, True]
# Iterating through a List
for x in fList1:
    print(x, " ", end="")
print()

# Iterators

iList = [1, 2, 3, 4, 5, 6]
iter1 = iter(iList)
print(next(iter1))
print(next(iter1))
print(next(iter1))
"""

"""
# Range Function
# Creating a list of numbers using range function
rList1 = list(range(0, 5))
print(rList1)

# Creating a list of numbers using range function with interval of 2 numbers
rList2 = list(range(0, 10, 2))
print(rList2)

# Iterating through multi dimensional array / list
rList3 = [[1, 2, 3], ['A', 'B', 'C'], ['a', 'b', 'c']]

for x in range(0, 3):
    for y in range(0, 3):
        print(rList3[x][y])
"""
"""
# Tuples - Immutable collection of data
t1 = (1, "Test", 3.143)
# Length of the Tuple
print("Length :", len(t1))

# First value
print("First value :", t1[0])

# Last Value
print("Last Value :", t1[-1])

# Values from 0 to 1 but not 2
print("Values from 0 to 1 but not 2 :", t1[0:2])

# Every other value
print("Every other value :", t1[0:-1:2])
"""

"""
# Dictionaries are the list of Key Value pairs - Duplicate keys are not allowed
# Creating a Dictionary
students1 = {
    "1": "Student1",
    "2": "Student2",
    "3": "Student3"
}
print(students1)

students2 = dict([
    ("1", "Student1"),
    ("2", "Student2"),
    ("3", "Student3")
])
print(students2)

# Length of the Dictionary
print(len(students1))

# Getting a value of the Key
print(students1["2"])

# Adding or Changing the value of the Key
students1["3"] = "Student333"
students1["4"] = "Student4"
print(students1)

# Converting Dictionary to List of Key Value tuples
print(list(students1.items()))

# Get the list of keys from the Dictionary
print("Keys :", list(students1.keys()))

# Get the list of values from the Dictionary
print("Values :", list(students1.values()))

# Deleting a Key from Dictionary
del students1["2"]
print(students1)

students1.pop("4")
print(students1)

# Checking whether a key exists or not
print("2" in students1)
print("2" in students2)

# Iterating a Dictionary using for loop
# Iterates through all the keys
for x in students2:
    print(x)

# Iterates through all the Values
for x in students2.values():
    print(x)

# Printing the dictionary value automatically
dict1 = {"id": "1", "name": "TEST"}
print("%(id)s Name is %(name)s" % dict1)

dict2 = {"name": "NAME", "price": 10.053}
print("%(name)s price is RS. %(price).2f" % dict2)
"""

# Sets - An unordered list only have the Unique values
# Creating a Set

set1 = set([1, 2, "TEST"])
set2 = {1, 4, "TEST"}

print(set1)
print(len(set1))

# Adding two sets - Only distinct values
set3 = set1 | set2
print(set3)

# Adding an element to the set
set3.add(5.14)
print(set3)

# Remove or discard an element from the set 







































