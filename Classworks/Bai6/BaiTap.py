# Kiem tra so toan chan, toan le
n = input("Nhap so nguyen duong: ")
count = 0
for char in n:
    if int(char) % 2 == 0:
        count += 1
if count == len(n):
    print("%s la so toan chan" %n)
elif count == 0:
    print("%s la so toan le" %n)
else:
    print("%s la so co chan co le" %n)

# Xuat chu so
n = input("Nhap so nguyen: ")
number_texts = ["Khong", "Mot", "Hai", "Ba", "Bon", "Nam", "Sau", "Bay", "Tam", "Chin"]
if n[0] == "-":
    print("Am", end=" ")
for char in n:
    if char.isdigit():
        number_text = number_texts[int(char)]
        print(number_text, end=" ")

# Format van ban
baitho= '''Quê    hương    là     con diều biếc
Tuổi         thơ con thả trên   đồng
Quê hương là   con đò nhỏ
Êm đềm     khua nước ven sông

    Quê hương là cầu tre nhỏ
Mẹ về nón lá   nghiêng che
        Là  hương    hoa đồng     cỏ     nội
Bay     trong giấc    ngủ đêm      hè'''
while "  " in baitho:
    baitho = baitho.replace("  ", " ")
baitho = baitho.replace("\n ", "\n")
print(baitho)

# Tinh thua so nguyen to
n = int(input("Nhập số nguyên n:"))
ketqua = str(n)+" = "
i = 2
while i <= n and n >= 1:
    if  n % i == 0:
        ketqua += str(i)+" * "
        n = n / i
    else:
        i += 1
print("%s"%(ketqua[:-3]))
