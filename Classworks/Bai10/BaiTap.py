import os
import csv

# Duyet qua het cac file trong folder, doc file txt
def list_file(path, filetype):
    paths = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.lower().endswith(filetype.lower()):
                full_path = os.path.join(root, file)
                paths.append(full_path)
    print(paths)
    return paths
list_file("Files", "txt")

# Xu ly file CSV
# def read_csv_file(file_name):
#     with open(file_name) as f:
#         reader = csv.reader(f)
#         header = list(next(reader))
#         rows = list(reader)
#         for row in rows:
#             print(row)
#         return (header, rows)
#
# def get_diem(lop, rows):
#     ret = list(filter(lambda x: x[2] == lop and x[3].isdigit(), rows))
#     return ret[0][3]
#
# def cap_nhat_diem(rows):
#     for row in rows:
#         if row[3] == "?":
#             row[3] = get_diem(row[2], rows)
#     return rows
#
# def xep_loai(header, rows):
#     xep_loai = lambda d: "Xuat Sac" if d >= 9 else "Gioi" if d >= 8 else "Kha" if d >= 7 else "Yeu"
#     header.append("XepLoai")
#     new_rows = [header]
#     for row in rows:
#         row.append(xep_loai(float(row[3])))
#         new_rows.append(row)
#     return new_rows
#
# def write_csv_file(file_name, rows):
#     a = open(file_name, "w")
#     writer = csv.writer(a)
#     writer.writerows(rows)
#     a.close()
#
# data = read_csv_file("Files/HocSinh.csv")
# header = data[0]
# rows = data[1]
# rows = cap_nhat_diem(rows)
# rows = xep_loai(header, rows)
# write_csv_file("Files/HocSinh2.csv", rows)
# read_csv_file("Files/HocSinh2.csv")

import csv
from csv import reader
# Câu a đọc file csv và in từng dòng:
def read_csv_file(filename):
    with open(filename, 'r') as read_obj:
        csv_reader = reader(read_obj)
        header = next(csv_reader)
        for row in csv_reader:
            print(row)

# Câu b, cập nhật điểm cho học sinh bị thiếu điểm, biết các học sinh trong cùng lớp có điểm như nhau
def read_csv_file_to_list(filename):
    f = open(filename)
    data = []
    count = 0
    for row in csv.reader(f):
        if count == 0:
            row.append("XepLoai") # Tạo Cột xếp loại
            data.append(row)
        else:
            data.append(row)
        count += 1
    f.close()
    return data

data = read_csv_file_to_list('Files/HocSinh.csv')

def CapNhatDiemThieu(hs):
    if '12A1' in hs:
        return '9'
    elif '12A2' in hs:
        return '8'
    elif '12A3' in hs:
        return '7'
for hs in data:
    if hs[3]=='?':
        hs[3] = CapNhatDiemThieu(hs)

# Câu c tao cot du lieu moi XepLoai, 9: Xuat Sac, 8: Gioi, 7: Kha

for hs in data:
    if hs[3]=='9':
        hs.append('Xuat Sac')
    elif hs[3]=='8':
        hs.append('Gioi')
    elif hs[3]=='7':
        hs.append('Kha')

# Câu d: ghi dữ liệu vào file csv mới
def write_csv_file(filename, listContent):
    f = open(filename,'w+', newline='')
    for item in listContent:
        csv.writer(f).writerow(item)
    f.close()

read_csv_file('Files/HocSinh.csv')
write_csv_file('Files/HocSinh2.csv', data)
print()
read_csv_file('Files/HocSinh2.csv')