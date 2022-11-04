"""
Bai1. HELLO WORLD
"""

print('Hello world')  # First line
number = 100
average = 8.5
name = "Minh"
print(number)
print(average)
print(name)

x, y, z = 10, 15, 20
print("x + y + z = %i" % (x + y + z))

full_name = 'Minh Nguyen'
print(full_name)
print(full_name[0])
print(full_name[2:4])
print(full_name[4:])
print(full_name[:4])

greeting = 'Hello, '
print(greeting + full_name)
print((greeting + full_name) * 4)
print(len(full_name))

age = 25
height = 1.6
weight = 52.5
print("My name is %s. I'm %i years old. My height is %.2f(m) and my weight is %.2f(kg)" % (name, age, height, weight))

strInt = "12"
print(int(strInt) * 2)

# name = input("What is your name? ")
# print("My name is", name)

# toan = eval(input("Diem Toan: "))
# van = eval(input("Diem Van: "))
# print("Diem trung binh", (toan + van)/2)

print("Tuoi" + " " + str(age))
print("Tuoi", age)
print("Tuoi %d" % (age))

x = eval(input("Nhap x: "))
y = eval(input("Nhap y: "))
tong = x + y
hieu = x - y
tich = x * y
thuong = x / y
print("Tong = %d, Hieu = %d, Tich = %d, Thuong = %.2f" % (tong, hieu, tich, thuong))
