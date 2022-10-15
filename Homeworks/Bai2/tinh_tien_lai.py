lai_suat = eval(input("Lãi suất 1 năm (%): "))
so_tien_gui = eval(input("Số tiền gửi: "))
so_thang_gui = eval(input("Số tháng gửi: "))

tien_lai = (so_tien_gui * so_thang_gui)*(lai_suat/100/12)
print("Tiền lãi =", tien_lai)
print("Tiền vốn + lãi = %i + %i = %i" %(so_tien_gui, tien_lai, so_tien_gui + tien_lai))