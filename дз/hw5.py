#1

import math
def f(x,y):
  return math.degrees(math.atan(x/y))
x1,x2 = map(float,input('Введите x1 и x2: ').split())
y1,y2 = map(float,input('Введите y1 и y2: ').split())
z1,z2 = map(float,input('Введите z1 и z2: ').split())
print(f(x1,x2))
print(f(y1,y2))
print(f(z1,z2))


#2

def p(n):
  s=bin(n)[2:]
  s1=s[:(len(s))//2]
  s2=s[(len(s)-1)//2+1:]
  return s1[::-1]==s2
def f(n):
  v=n
  d=2
  if n==1:
    return False
  else:
    while d<=n//2:
      if n%d==0:
        v=0
      d+=1
    if v==0:
      return False
    else:
      return p(v)
n = int(input('Введите n: '))
m=[]
for i in range(0,n+1):
  if f(i)==True:
      m.append(i)
print(m)