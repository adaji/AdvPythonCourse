import random


class human:
    def __init__(self, name):
        self.name = name


class footbalist(human):
    team


nlist = ['حسین', 'مازیار', 'اکبر', 'نیما', 'مهدی', 'فرهاد', 'محمد', 'خشایار', 'میلاد', 'مصطفی',
         'امین', 'سعید', 'پویا', 'پوریا', 'رضا', 'علی', 'بهزاد', 'سهیل', 'بهروز', 'شهروز', 'سامان', 'محسن']

fl = []
ln = 21
for i in range(22):
    r = random.randint(0, ln)
    fl.append(footbalist(nlist.pop(r)))
    ln -= 1


A_count = 0
B_count = 0
for i in range(22):
    if random.randint(0, 1) == 0 and A_count < 11:
        fl[i].team = 'A'
        A_count += 1
    else:
        fl[i].team = 'B'
        B_count += 1

for i in range(22):
    print(fl[i].name, fl[i].team)
