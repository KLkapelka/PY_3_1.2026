import sys

# словарь
line_dict = {"1": "Аид", "2": "Лололошка", "3": "Фляжка", "4": "Райз", "5": "Гусь"}

# значение по ключу
print(f"Значение по ключу '2': {line_dict['2']}")

# коллекции с одинаковым количеством элементов
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_set = {1, 2, 3, 4, 5}

# сравнение размера контейнеров
print(f"Размер списка: {sys.getsizeof(my_list)} байт")
print(f"Размер кортежа: {sys.getsizeof(my_tuple)} байт")
print(f"Размер множества: {sys.getsizeof(my_set)} байт")
print(f"Размер словаря: {sys.getsizeof(line_dict)} байт")
