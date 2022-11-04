"""
Bai6. NUMBERS
"""

import math
import random

# Basic
print(abs(-15))
print(max(1, 2, 3))
print(min(1, 2, 3))
print(round(12.23456, 3))
print(round(12.23456, -1))

# Math
print(math.fabs(-15.0))
print(math.ceil(5.25))
print(math.floor(5.25))
print(math.pow(2, 3))
print(math.sqrt(4))
print(math.modf(12.26))

# Random Number
print("Random Int Number: ", random.randrange(1, 20, 1))
print("Random Int Number: ", random.randrange(2, 15, 2))
print("Random Float Number(>0 and <1): ", random.random())
print("Random Float Number(>x and <y): ", random.uniform(10, 20))
