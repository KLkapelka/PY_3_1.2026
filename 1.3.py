import timeit
sizes = [100, 1000000, 10000000]

# по каждому размеру
for size in sizes:
    # список и множество с одинаковыми данными от 0 до size-1
    my_list = list(range(size))
    my_set = set(range(size))

    # значение, которое есть в коллекции
    val_exists = size - 1
    # значение, которого нет в коллекции
    val_missing = -1

    # замер, поиск в списке, повторов 100
    time_list_exists = timeit.timeit(lambda: val_exists in my_list, number=100)
    time_list_missing = timeit.timeit(lambda: val_missing in my_list, number=100)

    # замер, поиск в множестве, повторов 100
    time_set_exists = timeit.timeit(lambda: val_exists in my_set, number=100)
    time_set_missing = timeit.timeit(lambda: val_missing in my_set, number=100)

    print(f"\nРазмер: {size} элементов")
    print(f"Список, значение есть:    {time_list_exists:.6f}")
    print(f"Список, значения нет:     {time_list_missing:.6f}")
    print(f"Множество, значение есть: {time_set_exists:.6f}")
    print(f"Множество, значения нет:  {time_set_missing:.6f}")
