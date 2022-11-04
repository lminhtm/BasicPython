"""
Bai3. OPERATOR
"""

a = 5
b = 10
c = a + b

c += b
c -= b
c /= b
c *= b
c %= b
c **= b
c //= b
print(c)

list = [1, 2, 3, 5, 9]
print(a in list)
print(a not in list)

print(a is b)
print("ida:", id(a), "idb:", id(b))

salary = 7000
cond = 5000 <= salary <= 7000
print(cond)

depid = 70
cond = depid in [50, 70, 90]
print(cond)
