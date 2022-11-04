# Khai bao
dict1 = {1: "one", 2: "two", 3: "three"}
dict2 = {"one": 1, "two": 2, "three": 3}

# Truy xuat
print(dict1[1])
print(dict2["one"])

# Thao tac
dict1[1] = "ONE"
dict1[4] = "four"
print("dict after modified:", dict1)
dict1.update(dict2)
print("dict after updated:", dict1)

# Xoa
del (dict1[1])
print("dict after deleted:", dict1)
dict1.clear()
print("dict after deleted:", dict1)

# Khoi tao
new_dict1 = dict1.copy()
list1 = ["Mot", "Hai", "Ba", "Bon"]
dict3 = dict.fromkeys(list1)
dict4 = dict.fromkeys(list1, 15)
print("dict from keys:", dict3, "\t\tdict from keys:", dict4)


