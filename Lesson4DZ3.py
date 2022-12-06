"""'3. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму."""
lst = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Исходный список: {lst}")
new_lst = []
[new_lst.append(i) for i in lst if i not in new_lst]
print(f"Список из неповторяющихся элементов: {new_lst}")