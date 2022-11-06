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
        reader = csv.reader(f)
        header = list(next(reader))
        rows = list(reader)
        for row in rows:
            print(row)
        return (header, rows)

def get_diem(lop, rows):
    ret = list(filter(lambda x: x[2] == lop and x[3].isdigit(), rows))
    return ret[0][3]

def cap_nhat_diem(rows):
    for row in rows:
        if row[3] == "?":
            row[3] = get_diem(row[2], rows)
    return rows

def xep_loai(header, rows):
    xep_loai = lambda d: "Xuat Sac" if d >= 9 else "Gioi" if d >= 8 else "Kha" if d >= 7 else "Yeu"
    header.append("XepLoai")
    new_rows = [header]
    for row in rows:
        row.append(xep_loai(float(row[3])))
        new_rows.append(row)
    return new_rows

def write_csv_file(file_name, rows):
    a = open(file_name, "w")
    writer = csv.writer(a)
    writer.writerows(rows)
    a.close()

data = read_csv_file("Files/HocSinh.csv")
header = data[0]
rows = data[1]
rows = cap_nhat_diem(rows)
rows = xep_loai(header, rows)
write_csv_file("Files/HocSinh2.csv", rows)
read_csv_file("Files/HocSinh2.csv")
