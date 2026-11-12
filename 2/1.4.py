words = ["asd", "aaaa", "asd", "ss", "ddd"]

# обычный цикл
dictionary = {}
for i in words:
    dictionary[i] = len(i) # слово - его длина

# dict comprehension
comp = {i: len(i) for i in words}

print(f"цикл: {dictionary}")
print(f"dict comprehension: {comp}")
print(f"совпадают ли: {dictionary == comp}")