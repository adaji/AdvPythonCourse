import mysql.connector
from mysql.connector import errorcode
import datetime
import re
import requests
from bs4 import BeautifulSoup as bs

car_brand = input('Enter car brand: ')
car_name = input('Enter car name (optional): ')
if len(car_name) > 0:
    carstr = car_brand + '/' + car_name + '/'
else:
    carstr = car_brand + '/'
count = 0
page = 1
car_data = []
while (count < 20):
    r = requests.get('https://bama.ir/car/'+carstr+'?page='+str(page))
    soup = bs(r.text, 'html.parser')

    # mileages = soup.find_all('p', attrs={'class': 'price hidden-xs'})
    # prices = soup.find_all('span', attrs={'itemprop': 'price'})

    txt = soup.find_all('div', attrs={'class': 'listdata'})
    for x in txt:
        count += 1
        if count > 20:
            break
        mileage = x.find_all('p', attrs={'class': 'price hidden-xs'})
        mileage = re.findall(r'کارکرد (.*) کیلومتر', mileage[0].text)[0]
        price = x.find_all('span', attrs={'itemprop': 'price'})

        # Cleaning Data
        if mileage == 'صفر':
            mileage = '0'
        try:
            if 'در توضیحات' in price[0].text:
                car_data.append((count, mileage, 'Refer Desc'))
            else:
                car_data.append((count, mileage, price[0].text))
        except:
            car_data.append((count, mileage, 'Call'))

    if count / 12 >= page:
        page += 1
    if count > 20:
        break
# Site data fetched completely
# Connecting to databse
date = str(datetime.datetime.now())
config = {'user': 'root', 'password': 'mydbpassword',
          'host': '127.0.0.1', 'database': 'bama'}
cnx = cur = None
try:
    cnx = mysql.connector.connect(**config)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Something is wrong with your user name or password')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cur = cnx.cursor()

    for car in car_data:
        cur.execute('INSERT INTO carPrice VALUES (%s,%s,%s,%s,%s)',
                    (car_brand, car_name, car[1], car[2], date))

    cnx.commit()
finally:
    if cur:
        cur.close()
    if cnx:
        cnx.close()
# End insert into database
print('%d rows has been succesfully entered into databses.' % (count - 1))
