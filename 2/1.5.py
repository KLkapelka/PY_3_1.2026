students = [
    {"name": "Анна", "score": 85, "attempts": 2},
    {"name": "Григорий", "score": 45, "attempts": 1},
    {"name": "Антон", "score": 70, "attempts": 4},
    {"name": "Федя", "score": 90, "attempts": 3},
    {"name": "Лёша", "score": 60, "attempts": 2}
]

# append()
list = []
for i in students:
    if i["score"] >= 60 and i["attempts"] <= 3:
        list.append(i["name"])

# List comprehension
comp = [i["name"] for i in students if i["score"] >= 60 and i["attempts"] <= 3]

print(f"цикл: {list}")
print(f"comprehension: {comp}")
print(f"совпадают ли: {list == comp}")