so_tien = eval(input("Số tiền muốn đổi: "))

so_to_1 = so_tien // 500000
tien_con_lai = so_tien % 500000

so_to_2 = tien_con_lai // 200000
tien_con_lai = tien_con_lai % 200000

so_to_3 = tien_con_lai // 100000
tien_con_lai = tien_con_lai % 100000

so_to_4 = tien_con_lai // 50000
tien_con_lai = tien_con_lai % 50000

print("Số tờ 500,000:", so_to_1)
print("Số tờ 200,000:", so_to_2)
print("Số tờ 100,000:", so_to_3)
print("Số tờ 50,000:", so_to_4)
print("Tiền còn lại:", tien_con_lai)