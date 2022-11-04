"""
Bai10. FILE CSV
"""

import csv

# Open + read
def read_csv_file(filename):
    rows = []
    f = open(filename)
    for row in csv.reader(f):
        rows.append(row)
        print(row)
    f.close()
    return rows
data = read_csv_file("Files/iris_setosa.csv")
print(data, end="\n\n")

# Open + read with 'with'
def read_csv_file2(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        header = next(reader) # Ignore header
        rows = list(reader)
        return rows
data = read_csv_file2("Files/iris_setosa.csv")
print(data)

# Write
def write_csv_file(filename, content):
    with open(filename, "w", newline="") as f:
        for item in content:
            writer = csv.writer(f)
            writer.writerow(item)
write_csv_file("Files/file2.csv", [["a", "b", "c"], ["1", "2", "3"]])