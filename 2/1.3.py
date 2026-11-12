list = [] # список
for i in range(101):
    if i % 2 == 0: # чётно?
        list.append(i ** 2) # ^2 +

# генератор списка
comp = [i ** 2 for i in range(101) if i % 2 == 0]

print(f"цикл: {list}")
print(f"comprehension: {comp}")
print(f"совпадают ли: {list == comp}")