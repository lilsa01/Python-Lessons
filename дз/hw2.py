#1

a = float(input("Введите первое число \n"))
b = float(input("Введите второе число \n"))
try:
  print(a/b)
except ZeroDivisionError:
  print("Деление на 0!")

#2

s = float(input("Введите сумму покупки \n"))
if s>20:
    fs=s*0.65
else:
    fs=s
print('Итоговая сумма покупки',round(fs,2))
print('Размер предоставленной скидки',round(s-fs,2))


#3

m=int(input('Введите номер месяца: '))
month=['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
if 1<=m<=12:
    print('Месяц -',month[m-1],'Время года - ', end='')
    if m==12 or 1<=m<=2:
        print('Зима')
    elif 3<=m<=5:
        print('Весна')
    elif 3<=m<=5:
        print('Лето')
    else:
        print('Осень')
else:
    print('Недопустимое число!')