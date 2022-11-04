"""
Bai6. STRINGS
"""

# Basic
str = "nguyen du"
print(str.capitalize())
print(str.title())
print("12345".isdigit())

# Center
str = "Happy Birthday"
print(str.center(30, "*"))      #********Happy Birthday********
print(str.center(20))           #   Happy Birthday

# Count & Find
str = "Happy New Year 2023"
print(str.count("New"))
print(str.count("p", 0, 10))
print(str.find("New"))
print(str.find("b", 3, 15))

# Replace
str = "She is beautiful. He is handsome"
print(str.replace("is", "was"))
print(str.replace("is", "was", 1))

# Strip
str = "    Happy New Year     "
print(str.strip())
str = "aaaaaaaaaaHappy New Yearaaaa"
print(str.strip("a"))

# Split
str = "Python is programing language"
print(str.split())
print(str.split("a"))
print(str.split(" ", 1))

# Inverse
str = "12345"
inverse_str = str[::-1]
print(inverse_str)
