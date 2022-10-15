loai_xe = eval(input("Loai xe (4 hoac 7 cho): "))
so_km = eval(input("So km di chuyen: "))
thoi_gian_cho = eval(input("Thoi gian cho (lam tron theo phut): "))

if loai_xe == 4 or loai_xe == 7:
    # Tien cho
    if thoi_gian_cho > 5:
        tien_cho = (thoi_gian_cho - 5) * 750
    else:
        tien_cho = 0

    # Tien di chuyen
    if loai_xe == 4:
        phi_mo_cua = 11000
        phi_30 = 15300
        phi_31 = 12100
    else:
        phi_mo_cua = 12000
        phi_30 = 16100
        phi_31 = 13800
    if so_km <= 31:
        tien_di_chuyen = phi_mo_cua + (so_km - 0.8) * phi_30
    else:
        tien_di_chuyen = phi_mo_cua + (31 - 0.8) * phi_30 + (so_km - 31) * phi_31

    # Tien cuoc
    tien_cuoc = tien_cho + tien_di_chuyen

    print("Tien cho = (%i - 5) * 750d = %i" % (thoi_gian_cho, tien_cho))
    print("Tien di chuyen = %.1f" % (tien_di_chuyen))
    print("Tien cuoc = %i + %i = %i" % (tien_cho, tien_di_chuyen, tien_cuoc))
else:
    print("Khong ho tro")


