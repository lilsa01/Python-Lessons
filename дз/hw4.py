#1

s = input('Введите строку: ')
k=m=0
for i in range(len(s)):
    if s[i]=='н':
        k+=1
    else:
        m=max(m,k)
        k=0
s=s.replace('н','!')
print('Максимальное количество подряд идущих букв «н»:', m)
print('Преобразованная строка:', s)

#2

s = input('Введите строку: ')
for i in '[{':
  s=s.replace(i,'(')
for i in '}]':
  s=s.replace(i,')')
for i in range(len(s)):
    if s[i]=='(':
        a=i
    elif s[i]==')':
        b=i
print(s[a+1:b])


#3

s = input('Введите строку: ')
s=s.split()
a=''
for i in s:
    if i[0].lower()=='а'and i[-1]=='я':
        a+= i + ' '
print(a)