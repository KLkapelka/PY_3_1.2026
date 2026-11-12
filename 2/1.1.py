estimation = [5, 4, 3, 5, 2, 4] # список оценок

print("РУЧНОЙ")
count = 1
for i in estimation:
    print(f"№:{count}, оценка: {i}")
    count += 1

print("\nENUMERATE")
# enumerate() выдает индекс и значение. Нумерация с 1
for count, i in enumerate(estimation, 1):
    print(f"№:{count}, оценка: {i}")