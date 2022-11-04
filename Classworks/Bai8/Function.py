import  math
from operator import add
from functools import reduce

# Function
def tinh_diem_trung_binh(hk1, hk2):
    return (hk1 + hk2 * 2)/3
print("Diem trung binh:", tinh_diem_trung_binh(8, 10))

# Keyword argument
tinh_diem_trung_binh(hk2 = 10, hk1=8)

# Default argument
def choose_drink(price, drink = "coffee"):
    print("Price", price, "with", drink)

# Variable-length argument
def in_loi_chao(loi_chao, *danh_sach_ten):
    for ten in danh_sach_ten:
        print(loi_chao, ten)
in_loi_chao("Hello", "Mai", "Lan")

# Lambda
s = lambda x, n: math.pow(math.pow(x, 2) + 1, n)  # (x * x + 1) ^ n
print("s(2, 3) =", s(2, 3))

s = lambda a, b: "vo so nghiem" if a == b == 0 else "vo nghiem" if a == 0 and b != 0 else -b/a
print("3x + 6 = 0 -> x =", s(3, 6))
print("0x + 0 = 0 -> x =", s(0, 0))
print("0x + 6 = 0 -> x =", s(0, 6))

# Built-in Function (map)
list1 = [1, 2, 3, 4, 5]
s = lambda x: x ** 2
list2 = list(map(s, list1))
list3 = list(map(lambda x1,x2: x1 + x2, list1, list2))
list4 = list(map(add, list1, list2))
print("list2 (map):", list2, "\t\tlist3 (map):", list3, "\t\tlist4 (map):", list4)

# Built-in Function (filter)
list5 = list(filter(lambda x: x % 2 == 0, list1))
print("list5 (filter):", list5)

# Built-in Function (reduce)
sum1 = reduce(lambda a, b: a + b, list1)
sum2 = reduce(add, list(filter(lambda x: x % 2 == 0, list1)))
print("sum1 (reduce):", sum1, "\t\tsum2 (reduce):", sum2)
