#Задача построить цикл от 0 до введенного числа (включительно) и посчитать сумму всех чисел,
# делимых без остатка на 3 или 5. Вывести число на консоль.
limit = int(input())
ls = [l for l in range(0, limit + 1) if l % 3 == 0 or l % 5 == 0 ]
print(sum(ls))