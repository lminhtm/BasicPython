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
def read_csv_file(file_name):
    with open(file_name) as f:
        for row in csv.reader(f):
            print(row)

def get_diem(lop, rows):
    ret = list(filter(lambda x: x[2] == lop and x[3].isdigit(), rows))
    return ret[0][3]

def cap_nhat_diem(file_name, new_file_name):
    f = open(file_name, "r")
    reader = csv.reader(f)
    header = list(next(reader))
    rows = list(reader)
    f.close()

    header.append("XepLoai")
    new_rows = [header]
    for row in rows:
        stt, name, lop, diem = row[0], row[1], row[2], row[3]
        xep_loai = lambda d: "Xuat Sac" if d >= 9 else "Gioi" if d >= 8 else "Kha" if d >= 7 else "Yeu"
        if diem == "?":
            diem = get_diem(lop, rows)
        new_rows.append([stt, name, lop, diem, xep_loai(float(diem))])

    a = open(new_file_name, "w")
    writer = csv.writer(a)
    writer.writerows(new_rows)
    a.close()

read_csv_file("Files/HocSinh.csv")
cap_nhat_diem("Files/HocSinh.csv", "Files/HocSinh2.csv")
print()
read_csv_file("Files/HocSinh2.csv")