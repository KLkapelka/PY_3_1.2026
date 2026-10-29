my_list = [10, 20, 30, 40, 50, 60] # список
my_tuple = (10, 20, 30, 40, 50, 60) # кортэж

print("ИСХОДНЫЕ ДАННЫЕ:")
# type() и id() для обоих
print(f"Список: type = {type(my_list)}, id = {id(my_list)}")
print(f"Кортеж: type = {type(my_tuple)}, id = {id(my_tuple)}")


print("\nИЗМЕНЕНИЕ СПИСКА:")
# id списка до изменения
old_list_id = id(my_list)

# смена одного эллемента списка
my_list[0] = 999

# сравнение идентификатора до и после изменения
print(f"Список после изменения: {my_list}")
print(f"Старый id списка: {old_list_id}")
print(f"Новый id списка: {id(my_list)}")
print(f"id списка изменился? {old_list_id != id(my_list)}")


print("\nИЗМЕНЕНИЕ КОРТЕЖА:")
# создание невого кортежа, старый изменять нельзя
new_tuple = (999, 20, 30, 40, 50, 60)

# id старого и нового кортежа
old_tuple_id = id(my_tuple)
new_tuple_id = id(new_tuple)

print(f"Старый кортеж: {my_tuple}")
print(f"Новый кортеж: {new_tuple}")
print(f"Старый id кортежа: {old_tuple_id}")
print(f"Новый id кортежа: {new_tuple_id}")
print(f"id кортежа изменился? {old_tuple_id != new_tuple_id}")
