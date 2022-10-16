so_kw = eval(input("So kw tieu thu: "))
gia_bac1 = 1484
gia_bac2 = 1533
gia_bac3 = 1786
gia_bac4 = 2242
gia_bac5 = 2503
gia_bac6 = 2587

"""
if so_kw <= 50:
    tien_dien = so_kw * gia_bac1
elif so_kw <= 100:
    tien_dien = 50 * gia_bac1\
                + (so_kw - 50) * gia_bac2
elif so_kw <= 200:
    tien_dien = 50 * gia_bac1\
                + (100 - 50) * gia_bac2\
                + (so_kw - 100) * gia_bac3
elif so_kw <= 300:
    tien_dien = 50 * gia_bac1\
                + (100 - 50) * gia_bac2\
                + (200 - 100) * gia_bac3\
                + (so_kw - 200) * gia_bac4
elif so_kw <= 400:
    tien_dien = 50 * gia_bac1\
                + (100 - 50) * gia_bac2\
                + (200 - 100) * gia_bac3\
                + (300 - 200) * gia_bac4\
                + (so_kw - 300) * gia_bac5
else:
    tien_dien = 50 * gia_bac1\
                + (100 - 50) * gia_bac2\
                + (200 - 100) * gia_bac3\
                + (300 - 200) * gia_bac4\
                + (400 - 300) * gia_bac5\
                + (so_kw - 400) * gia_bac6
"""

tien_dien = 0
so_kw_bac_thang = so_kw
if so_kw_bac_thang > 400:
    tien_dien += (so_kw - 400) * gia_bac6
    so_kw_bac_thang = 400
if so_kw_bac_thang > 300:
    tien_dien += (so_kw_bac_thang - 300) * gia_bac5
    so_kw_bac_thang = 300
if so_kw_bac_thang > 200:
    tien_dien += (so_kw_bac_thang - 200) * gia_bac4
    so_kw_bac_thang = 200
if so_kw_bac_thang > 100:
    tien_dien += (so_kw_bac_thang - 100) * gia_bac3
    so_kw_bac_thang = 100
if so_kw_bac_thang > 50:
    tien_dien += (so_kw_bac_thang - 50) * gia_bac2
    so_kw_bac_thang = 50
if so_kw_bac_thang > 0:
    tien_dien += so_kw_bac_thang * gia_bac1
print("Tien dien phai tra =", tien_dien)