loai_phong = eval(input("Nhap loai phong (tu 1 den 8): "))
so_dem = eval(input("Nhap so dem: "))

gia_phong_loai_1 = 1260000
gia_phong_loai_2 = 1550000
gia_phong_loai_3 = 1830000
gia_phong_loai_4 = 1830000
gia_phong_loai_5 = 2120000
gia_phong_loai_6 = 2120000
gia_phong_loai_7 = 2540000
gia_phong_loai_8 = 4800000

gia_phong = 0
if loai_phong == 1:
    gia_phong = gia_phong_loai_1
elif loai_phong == 2:
    gia_phong = gia_phong_loai_2
elif loai_phong == 3:
    gia_phong = gia_phong_loai_3
elif loai_phong == 4:
    gia_phong = gia_phong_loai_4
elif loai_phong == 5:
    gia_phong = gia_phong_loai_5
elif loai_phong == 6:
    gia_phong = gia_phong_loai_6
elif loai_phong == 7:
    gia_phong = gia_phong_loai_7
elif loai_phong == 8:
    gia_phong = gia_phong_loai_8

if so_dem >= 4:
    tien_phong = so_dem * gia_phong * (1 - 0.3)
elif so_dem >= 2:
    tien_phong = so_dem * gia_phong * (1 - 0.25)
else:
    tien_phong = so_dem * gia_phong
print("Thanh tien =", tien_phong)
