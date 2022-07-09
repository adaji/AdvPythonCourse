import re
import requests
from bs4 import BeautifulSoup as bs

r = requests.get('https://maktabkhooneh.org/plus/')
soup = bs(r.text, 'html.parser')

txt = soup.find_all('div', attrs={'class': 'course-name'})

maktab = []
tehuni = []
for x in txt:
    out = re.findall(r'\w+.*', x.text)
    if out[2] == 'مکتب\u200cخونه':
        maktab.append(out[0])
    elif out[2] == 'دانشگاه تهران':
        tehuni.append(out[0])

print('\n\nTehran University Courses:\n')
for x in tehuni:
    print(x)

print('\n\nMaktabkhooneh Courses:\n')
for x in maktab:
    print(x)
