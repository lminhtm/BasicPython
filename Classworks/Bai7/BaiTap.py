numbers = [1, 2, 4, 2, 3, 8, 9, 5, 6, 1, 6, 2, 1, 1, 1, 1, 1, 7, 3, 8]
while numbers.count(1) > 0:
    numbers.remove(1)
print(numbers)

numbers = [1, 2, 4, 2, 3, 8, 9, 5, 6, 1, 6, 2, 1, 1, 1, 1, 1, 7, 3, 8]
numbers2 = []
for number in numbers:
    if number not in numbers2:
        numbers2.append(number)
print(numbers2)
