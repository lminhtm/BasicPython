import os
import csv
from csv import reader

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
