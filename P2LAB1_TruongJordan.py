Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Jordan Hall-Truong
... # 3/8/2025
... # P2LAB1
... # Calculates the diameter, circumference, and area of a circle based on a given radius.
... 
... import math
... 
... radius = float(input("What is the radius of the circle? "))
... 
... diameter = 2 * radius
... circumference = 2 * math.pi * radius
... area = math.pi * radius**2
... 
... print(f"The diameter of the circle is {diameter:.1f}")
... print(f"The circumference of the circle is {circumference:.2f}")
