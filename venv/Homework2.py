l = "дпвоивннннннтммлд"
k = 1
c = 0
for i in range(len(l)-1):
  if l[i] == "н" and l[i+1] == "н":
    k += 1
  else:
    k = 1
  if k > c:
    c = k
print(c, l.replace("н" * c, "!" * c))

l = 'ввлцу(ояивм.щшй)додрн'
print(((l.split("("))[1].split(")"))[0])

l = "Аня шла по парку и акция и адаптация"
lst = l.split(" ")
for i in lst:
  if (i[0] == "а" or i[0] == "А") and i[-1] == "я":
    print(i, end=" ")