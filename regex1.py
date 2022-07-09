import re

str = input()
res = re.search(r'^\D[\w\.]+@\w+\.[a-zA-Z]+$', str)
if res != None:
    print('OK')
else:
    print('WRONG')
