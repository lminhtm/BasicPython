"""
j = int(input("Nhập số bắt đầu: "))
n = int(input("Nhập số kết thúc: "))
if j > n:
    n, j = j, n

while j <= n:
    i = 1
    while i <= 10:
        print(j, " x", i, "= ", j*i)
        i += 1
    j += 1
"""

for char in "Minh":
    print("Character: %c" %char)

animals = ["dog", "cat", "elephant", "bird", "lion"]
for index in range(len(animals)):
    print("Animal[%i] is %s" %(index, animals[index]))
for animal in animals:
    print("Animal[%i] is %s" %(animals.index(animal), animal))

count = 1
while count <= 5:
    print(count, "<= 5")
    count += 1
else:
    print(count, "> 5")

for letter in "Phuong":
    if letter == "o":
        break
    print("Letter:", letter)

"""
i = 10
while i > 0:
    if i % 2 == 0:
        print("Value", i)
    i -= 1
    if i == 5:
        break
print("end")
"""

print("Chuong trinh tim so nguyen to")
val = int(input("Nhap so nguyen duong: "))
if val > 2:
    i = 2
    while i < val:
        if val % i == 0:
            print("%i khong phai la so nguyen to" %val)
            break
        i += 1
    else:
        print("%i la so nguyen to" %val)
else:
    print("%i khong phai la so nguyen to" %val)

for letter in "Phuong":
    if letter == "o":
        continue
    print("Letter:", letter)

for letter in "Phuong":
    if letter == "o":
        pass
        print("Pass block")
    print("Letter:", letter)

print("Chuong trinh tinh tong so chan")
n = int(input("Nhap so nguyen: "))
sum = 0
for i in range(0, n + 1, 2):
   sum += i
print("Tong:", sum)
