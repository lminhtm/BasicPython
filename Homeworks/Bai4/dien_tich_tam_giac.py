import math

a, b, c = eval(input("Nhập cạnh a, b, c: "))
p = (a + b + c)/2
S = math.sqrt(p * (p - a) * (p - b) * (p - c))
print("Dien tich tam giac:", S)