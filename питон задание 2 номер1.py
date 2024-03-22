from itertools import *
c = 0
for i in product('ГЕПАРД', repeat=5):
    if i.count('Г')==1 and i[0]!='А' and i[-1]!='Е':
        c += 1
print(c)
