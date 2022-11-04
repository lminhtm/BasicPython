# Bai Tap 1: Tim so dien thoai
s = '''
Hôm nay công ty có 5 khách hàng mới. Thông tin của khách hàng như sau:
Khách hàng 1: Nguyễn Trọng Duy. SDT: 097,797,23868.
Khách hàng 2: Lê Trọng     Đạt. SDT: 093,210,9990.
Khách hàng 3: Nguyễn  Tấn    Ngọc  Tâm. SDT: 090,930.8018.
Khách hàng 4: Nguyễn    Minh  Khôi. SDT: 091,3xx,6895.
Khách hàng 5: Nguyễn   Thị   Thanh   Nhạn. SDT: 135.504.2483.
'''
s = s.replace(",", "").replace(".", "")
phones = []
for word in s.split():
    def is_so_dien_thoai(c):
        if len(c) == 10 and c[0] == '0' and c.isdigit():
            return True
    if is_so_dien_thoai(word):
        phones.append(word)
        print(word)
print("Trong van ban vua nhap co", len(phones), "so dien thoai di dong")

# Bai Tap 2: Phuong trinh bac nhat ax + b = 0
s = lambda a, b: "vo so nghiem" if a == b == 0 else "vo nghiem" if a == 0 and b != 0 else -b/a
print("3x + 6 = 0 -> x =", s(3, 6))
print("0x + 0 = 0 -> x =", s(0, 0))
print("0x + 6 = 0 -> x =", s(0, 6))

# Bai Tap 3: Xep loai
xeploai = lambda d:"Xuất sắc" if d >=9 else "Giỏi" if d >=8 else "Khá" if d>=7 else "Trung bình" if d >=5 else "Yếu"
print("Xep loai:", xeploai(4.5))

# Bai Tap 4: Nhap lieu nhanh
x, y, z = map(eval, input("Nhap vao 3 so x, y, z: ").split())

# Bai Tap 5: Nam nhuan
list_nam = [2000, 2002, 2005, 2010, 2020, 2022]
print("Nam nhuan: ", list(filter(lambda x: x % 4 == 0, list_nam)))
