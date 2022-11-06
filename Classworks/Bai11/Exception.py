"""
Bai11. EXCEPTION
"""

# assert
def cal_avg(sem1, sem2):
    assert(sem1 >= 0 and sem2 >= 0), "Invalid input"
    return (sem1 + sem2 * 2) / 3
cal_avg(1, 1)

# except 1
try:
    x = eval(input("Nhap x: "))
    y = eval(input("Nhap y: "))
    z = x / y
except NameError as e:
    print("Error: ", e)
except ZeroDivisionError as e:
    print("Error: ", e)
else:
    print("x / y = ", z)

# except 2
try:
    x = eval(input("Nhap x: "))
    y = eval(input("Nhap y: "))
    z = x / y
except (NameError, ZeroDivisionError) as e:
    print("Error: ", e)
else:
    print("x / y = ", z)
finally:
    print("Did finish program")

# except 3 (raise)
try:
    x = eval(input("Nhap x: "))
    y = eval(input("Nhap y: "))
    if y == 0:
        raise ZeroDivisionError("Custom ZeroDivisionError")
    z = x / y
except (NameError, ZeroDivisionError) as e:
    print("Error: ", e)
else:
    print("x / y = ", z)

# except 4
def NhapSoNguyen():
    while True:
        try:
            n = int(input("Nhập vào 1 số nguyên: "))
        except:
            print("Chỉ nhập số nguyên. Vui lòng nhập lại")
        else:
            return n
n = NhapSoNguyen()
print(n)
