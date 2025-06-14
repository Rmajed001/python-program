#Type conversion in Python is the process of converting one data type to another.

#There are two types of type conversion in Python:
#1. Implicit Type Conversion: This is automatically done by Python without any user involvement.
#2. Explicit Type Conversion: This is done by the user using built-in functions.
#casting types in Python is done using the built-in functions int(), float(), str(), etc.

a=int("2")  # Implicit conversion from string to integer
b=float("4.25")

sum=a+b
print("\n","Type of b is:", type(b),"\n")
print("sum of a and b is:", sum, "\n")

c=8.67
c=str(c)
print("Type of c is:", type(c), "\n")