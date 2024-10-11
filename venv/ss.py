import re

string = input()
nnn = re.findall('[Нн]+',string)
print(nnn)
nnn_len = map(len,nnn)
maximal_nnn = max(nnn_len)
string_replaced = string.replace('!','.')
print(string_replaced)
