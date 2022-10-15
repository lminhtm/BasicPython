a = eval(input("Nhập a: "))
b = eval(input("Nhập b: "))
print("PT bậc nhất: %fx + %f = 0" %(a, b))

if a != 0:
    print("Nghiệm x =", -b / a)
elif b == 0:
    print("Vô số nghiệm")
else:
    print("Vô nghiệm")