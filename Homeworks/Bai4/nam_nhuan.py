nam = eval(input("Nhap nam: "))
if nam % 400 == 0 or (nam % 4 == 0 and nam % 100 != 0):
    print("Nam %i la nam nhuan" %nam)
else:
    print("Nam %i khong phai la nam nhuan" %nam)