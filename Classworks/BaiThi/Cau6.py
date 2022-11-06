# Cau6
import csv

def read_csv_file(file_name):
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = list(reader)
        for row in rows:
            print(row)
        return (header, rows)

def tinh_luong(phong, rows):
    ret = list(filter(lambda x: x[2] == phong and x[3].isdigit(), rows))
    return ret[0][3]

def cap_nhat_luong(rows):
    for row in rows:
        if row[3] == "?":
            row[3] = tinh_luong(row[2], rows)
    return rows

def cap_nhat_overtime(rows):
    for row in rows:
        if row[4] == "1":
            row[3] = str(round(float(row[3]) * 1.1))
            row.append("Yes")
        else:
            row.append("No")
    return rows

def write_csv_file(file_name, rows):
    with open(file_name, "w+", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

data = read_csv_file("Files/NhanSu.csv")
header, rows = data[0], data[1]
rows = cap_nhat_luong(rows)
rows = cap_nhat_overtime(rows)
header.append("Increase_Salary")
new_data = [header]
for row in rows:
    new_data.append(row)
write_csv_file("Files/NhanSu2.csv", new_data)
print()
read_csv_file("Files/NhanSu2.csv")
