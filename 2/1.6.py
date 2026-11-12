import time
sizes = [10000, 100000, 1000000] # размеры списков

# проходим по каждому размеру
for size in sizes:
    print(f"\nразмер: {size}")
    print("цикл    comprehension")
    time_oll_list = 0 # ср. list
    time_oll_comp = 0 # ср. comp

    # 7 раз, по каждому sizes
    for j in range(7):

        # замер цикл + append()
        start_list = time.time() # старт
        res_list = [] # результаты ^2
        for i in range(size):
            if i % 2 == 0:
                res_list.append(i ** 2)
        end_list = time.time()  # конец
        time_list = end_list - start_list # сколько рабоал
        time_oll_list += time_list

        # замер list comprehension
        start_comp = time.time()  # старт
        res_comp = [i ** 2 for i in range(size) if i % 2 == 0]
        end_comp = time.time()  # конец
        time_comp = end_comp - start_comp # сколько рабоал
        time_oll_comp += time_comp

        # результат
        print(f"{time_list:.4f}    {time_comp:.4f}")

    # ср. время
    list = time_oll_list / 7
    comp = time_oll_comp / 7
    print(f"  ср. время цикла: {list:.4f} с")
    print(f"  ср. время comprehension: {comp:.4f} с")

