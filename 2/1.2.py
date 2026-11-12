names = ["Анна", "Григорий", "Антон", "Федя"]
estimation = [2, 3, 4, 5]

# zip() объединяет в пары: ("Анна", 2
for name, grade in zip(names, estimation):
    print(f"{name}: {grade}") # формирование строки