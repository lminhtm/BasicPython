# Khai bao
set1 = {1, 2, 3, 4, 5}
set2 = set()
print(set1)

# Thao tac
set2.add("orange")
set2.add("strawberry")
item = set2.pop()
print(set2)

# Thao tac so hoc
set3 = {3, 5, 7, 9}
print("Union set:", set1 | set3)
print("Intersection set:", set1 & set3)
print("Difference set:", set1 - set3)

# Xoa
set1.discard(1)
set1.remove(2) # can throw error
