# Cau5
import math

def check_tam_giac_hop_le(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    return False

def check_tam_giac_vuong(a, b, c):
    return a*a == b*b + c*c or b*b == a*a + c*c or c*c == a*a + b*b

def check_tam_giac_can(a, b, c):
    return a == b or a == c or b == c

def check_tam_giac_deu(a, b, c):
    return a == b == c

def chu_vi_tam_giac(a, b, c):
    return a + b + c

def dien_tich_tam_giac(a, b, c):
    p = chu_vi_tam_giac(a, b, c)/2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

a, b, c = map(eval, input("Nhập vào 3 cạnh của tam giác a, b, c: ").split())
if check_tam_giac_hop_le(a, b, c):
    p = chu_vi_tam_giac(a, b, c)
    s = dien_tich_tam_giac(a, b, c)

    print("%i, %i và %i là ba cạnh của 1 tam giác" %(a, b, c))
    print("Chu vi tam giác là: ", p)
    print("Diện tích tam giác là: ", s)
    print("Ba đường cao của tam giác lần lượt là: (%.1f, %.1f, %.1f)" %(2*s/a, 2*s/b, 2*s/c))
    if check_tam_giac_vuong(a, b, c):
        print("Tam giác này là tam giác vuông")
    elif check_tam_giac_deu(a, b, c):
        print("Tam giác này là tam giác đều")
    elif check_tam_giac_can(a, b, c):
        print("Tam giác này là tam giác cân")
    else:
        print("Tam giác này là tam giác thường")
else:
    print("%i, %i và %i không phải là ba cạnh của 1 tam giác" %(a, b, c))
