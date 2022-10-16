import math
"""
start = int(input("Nhap start: "))
end = int(input("Nhap end: "))
for number in range(start, end + 1):
    if number > 1:
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                break
        else:
            print(number, end=" ")
"""

"""
n = int(input("Nhap n: "))
n1 = 0
n2 = 1
for _ in range(0, n):
    print(n1, end=" ")
    fibo = n1 + n2
    n1 = n2
    n2 = fibo    12345 -> 54321
"""

n = int(input("Nhap n: "))
if n >= 1000:
    result = 0
    while n > 0:
        result += 10 * (i % 10 * length) * length
        n = n / 10
    print(result)
