import  math
from functools import reduce

# Doc file
def read_text_file(file_name):
    try:
        f = open(file_name)
        content = f.read()
    except UnicodeDecodeError as err:
        print("Encoding error: ", err)
        print("Retry opening file".center(30, "-"))
        try:
            a = open(file_name, encoding="utf-8")
            content = a.read()
        except:
            print("Read error: ", err)
        finally:
            a.close()
    except:
        print("Read error: ", err)
    finally:
        f.close()
        print(content)
        return content

# read_text_file("Files/quehuong.txt")

# Tinh Tong - Tich
def nhap_so_nguyen():
    while True:
        try:
            n = int(input("Nhập vào 1 số nguyên:"))
        except:
            print("Chỉ nhập số nguyên. Vui lòng nhập lại")
        else:
            return n

def cauA(n):  # S=1+2+3+...+n
    S = 0
    for i in range(1, n + 1):
        S = S + i
    print('S = 1 + 2 + 3 + ... + n = %d' % S)

def cauB(n):  # S=1+3+5+...+(2n+1)
    S = 0
    for i in range(0, n + 1):
        S = S + (2 * i + 1)
    print('S = 1 + 3 + 5 + ... + 2*n+1 = {}'.format(S))

def menu():
    n = 0
    while True:
        print('\n********** CHƯƠNG TRÌNH TÍNH TỔNG TÍCH ************')
        print('\t0. Nhập n')
        print('\t1. S = 1 + 2 + 3 + ... + n')
        print('\t2. S = 1 + 3 + 5 + ... + (2n+1)')
        print('\t3. Kết thúc chương trình')
        cmd = int(input('Chọn chức năng cần thực hiện (0-3): '))
        if cmd == 0:
            n = nhap_so_nguyen()
        elif cmd == 1:
            cauA(n)
        elif cmd == 2:
            cauB(n)
        elif cmd == 3:
            print('Tạm biệt')
            break
        else:
            print('Chương trình chỉ nhận các số từ 0 đến 3. Yêu cầu nhập lại')

menu()
