"""
Bai4. CONDITION
"""

diem_tb = eval(input("Nhap diem trung binh: "))

"""
if diem_tb >= 0 and diem_tb <= 10:
    if diem_tb < 5:
        print("Yeu / Kem")
    elif diem_tb < 6:
        print("Trung binh")
    elif diem_tb < 7:
        print("Trung binh - Kha")
    elif diem_tb < 8:
        print("Kha")
    elif diem_tb < 9:
        print("Gioi")
    else:
        print("Xuat sac")
else:
    print("Diem khong hop le")
"""

if diem_tb >= 0 and diem_tb <= 10:
    if diem_tb >= 9:
        print("Xuat sac")
    elif diem_tb >= 8:
        print("Gioi")
    elif diem_tb >= 7:
        print("Kha")
    elif diem_tb >= 6:
        print("Trung binh - Kha")
    elif diem_tb >= 5:
        print("Trung binh")
    else:
        print("Yeu / Kem")
else:
    print("Diem khong hop le")
