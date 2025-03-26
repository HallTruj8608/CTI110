Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>  # Jordan Hall-Truong
...  # 3/3/2025
...  # P1HW1
...  # Calculator
... 
... 
... print("-----Calculating Exponents-----")
... base = int(input("Enter an integer as the base value: "))
... exponent = int(input("Enter an integer as the exponent: "))
... result = base ** exponent
... print(f"{base} raised to the power of {exponent} is {result}")
... 
... print("-----Addition and Subtraction-----")
... starting = int(input("Enter a starting integer: "))
... add = int(input("Enter an integer to add: "))
... subtract = int(input("Enter an integer to subtract: "))
... final = starting + add - subtract
