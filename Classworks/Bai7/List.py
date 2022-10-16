# Khai bao
integers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
floats = [1.2, 4.5]
strings = ["cat", "elephant", "dog", "bird"]
mixs = ["cat", 1, 3.4, [2, 4]]

# Truy xuat
print("list1[0] =", integers[0])
print("list1[8] =", integers[8])
print("list1[end] =", integers[-1])

print("\nlist1[1:4] =", integers[1:4])
print("list1[6:end] =", integers[6:])
print("list1 first 5 items =", integers[:5])
print("list1 last 5 items =", integers[-5:])

# Tinh toan
print("\nTim a trong list3 =", "cat" in strings)
print("Tinh max =", max(integers))
print("Tinh min =", min(integers))
print("Tinh sum =", sum(integers))
print("Tinh avg =", sum(integers)/len(integers))

# Thao tac item
integers.append(333)
integers.extend([119, 117])
integers.insert(1, 222)
integers.remove(1) # not found -> error
print("\nList sau khi thao tác item", integers)
print("Count item in list: ", integers.count(1))
print("Index of item: ", integers.index(222)) # not found -> error
print("Pop last: ", integers.pop())
print("Pop at index: ", integers.pop(2))

# Thao tac list
del(integers[1])
print("\nSau khi xóa: ", integers)
print("Cộng list: ", integers + floats)
print("Dup list: ", strings * 3)
strings.reverse()
print("Đảo ngược list: ", strings)
print("Đảo ngược list: ", strings[::-1])
integers.sort()
print("Sort list: ", integers)

# List Comprehension
new_strings = [x.upper() for x in strings]
print("\nList Comprehension: ", new_strings)
new_strings2 = [x.upper() for x in strings if "a" in x]
print("List Comprehension 2: ", new_strings2)
new_strings3 = [x.upper() if "a" in x else x.lower() for x in strings]
print("List Comprehension 3: ", new_strings3)
