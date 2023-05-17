#Проверка числа на отношение к нулю
number=int(input('Введите число: '))
if number == 0:
    print(number,'Это число ноль')
elif number > 0:
    print(number,'Это число больше 0')
else:
    print(number,'Это число меньше 0')