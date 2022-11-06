# Cau6
import csv

def read_csv_file(file_name):
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = []
        for row in reader:
            rows.append(row)
            print(row)
        return (header, rows)

def get_luong(phong, rows):
    ret = list(filter(lambda x: x[2] == phong and x[3].isdigit(), rows))
    return ret[0][3]

def cap_nhat_luong(rows):
    for row in rows:
        if row[3] == "?":
            row[3] = get_luong(row[2], rows)
    return rows

def cap_nhat_overtime(rows):
    for row in rows:
        if row[4] == "1":
            luong = row[3]
            row[3] = str(round(float(luong) * 1.1))
            row.append("Yes")
        else:
            row.append("No")
    return rows

def write_csv_file(file_name, rows):
    a = open(file_name, "w+", newline="")
    writer = csv.writer(a)
    for row in rows:
        writer.writerow(row)
    a.close()

data = read_csv_file("Files/NhanSu.csv")
header, rows = data[0], data[1]
rows = cap_nhat_luong(rows)
rows = cap_nhat_overtime(rows)
header.append("Increase_Salary")
new_rows = [header]
for row in rows:
    new_rows.append(row)
write_csv_file("Files/NhanSu2.csv", new_rows)
print()
read_csv_file("Files/NhanSu2.csv")