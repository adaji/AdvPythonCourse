import mysql.connector
from mysql.connector import errorcode
import datetime
import re
import requests
from bs4 import BeautifulSoup as bs


def str2num(s):
    ls = list(s)
    for x in ls:
        if x == ',':
            ls.remove(x)
    return int(''.join(ls))


print('Start fetching data from bama.ir ...')

car_data = []
data = []
for page in range(80, 181):  # change to 200
    try:
        data.append(requests.get('https://bama.ir/car?page='+str(page)))
    except errorcode:
        print(errorcode)
        continue
    print(page)
print('Data collection ends!')
ii = 0
for r in data:
    ii += 1
    print(ii)
    soup = bs(r.text, 'html.parser')
    txt = soup.find_all('div', attrs={'class': 'listdata'})
    for x in txt:
        # Reading data for each car:
        url = 'https://bama.ir'  # 1- URL
        name = ''  # 2- Name
        year = -1  # 3- Year (How many years old?)
        mileage = -1  # 4- Mileage in km
        gearbox = -1  # 5- Gearbox (0: Manual, 1: Automatic)
        fuel = -1  # 6- Fuel (0: Oil, 1: Hybrid or Diesel, etc.)
        damage = -1  # 7- Damage (0: None, 1: Any)
        color = ''  # 8- Color
        city = ''  # 9- City
        price = 0

        # If no price data -> continue
        try:
            price_data = x.find('span', attrs={'itemprop': 'price'}).text.strip()
            if 'در توضیحات' == price_data:
                # Let's continue bellow - would not raise an exception
                pass
            else:
                price = str2num(price_data)  # if not numerical, it will raise an exception
        except:
            continue

        # Reading Begins Here:
        # 1- URL
        url = url + x.a['href']
        # _______ Go to specific page of the car
        new_req = requests.get(url)
        new_soup = bs(new_req.text, 'html.parser')
        # 2- Name
        try:
            name = re.findall(r'\/\d{4,4}\-(\w+\-\w+\-[A-Za-z0-9\.]*).*\-for\-sale$', url)[0]
        except:
            name = re.findall(r'\/\d{4,4}\-(\w+\-\w+).*\-for\-sale$', url)[0]
        # 3- Year
        title = new_soup.find('h1', attrs={'itemprop': 'name'})
        year = int(title.find('span', attrs={'itemprop': 'releaseDate'}).text)
        d = datetime.datetime.now()
        if year < 1750:
            year = d.year - year - 621
        else:
            year = d.year - year
        # 4- Mileage
        mileage = x.find('p', attrs={'class': 'price hidden-xs'})
        try:
            mileage = re.findall(r'کارکرد (.*) کیلومتر', mileage.text)[0]
        except:
            continue
        if mileage == 'صفر':
            mileage = '0'
        mileage = int(str2num(mileage))
        # 5- Gearbox (0: Manual, 1: Automatic)
        if re.search(r'اتوماتیک', new_soup.text) is None:
            gearbox = 0
        else:
            gearbox = 1
        # 6- Fuel (0: Oil, 1: Hybrid or Diesel, etc.)
        if re.search(r'بنزین', new_soup.text) is None:
            fuel = 1
        else:
            fuel = 0
        # 7- Damage (0: None, 1: Any)
        # if re.search(r'بدون رنگ', new_soup.text) is None:
        if x.find('span', attrs={'id': 'body-status'}).text.strip(' ،') == 'بدون رنگ':
            damage = 0
        else:
            damage = 1
        # 8- Color
        color = x.find('span', attrs={'id': 'ex-color'}).text.strip(' ،')
        # 9- City
        city = x.find('span', attrs={'class': 'provice-mobile'}).text.strip(' ،')
        # 10- Output : Price
        if price == 0:
            p_data = new_soup.find('div', attrs={'class': 'inforow addetaildesc'})
            price = str2num(re.findall(r' پیشنهادی فروشنده: (.*) تومان', p_data.text)[0])
        price = price / 1000000  # Number in Million Toman
        # Reading web is done

        # Start storing to variable - after loop, insert into database
        car_data.append([url, name, year, mileage, gearbox, fuel, damage, color, city, price])

# Storing to Database
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
        cur.execute("SELECT url FROM dataset WHERE url=%s", (car[0],))
        existing_car = cur.fetchone()
        if existing_car is not None:
            cur.execute("UPDATE dataset SET price = %s WHERE url=%s", (car[-1], car[0]))
        else:
            cur.execute('INSERT INTO dataset VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                        tuple(car))
    cnx.commit()
finally:
    if cur:
        cur.close()
    if cnx:
        cnx.close()

print('Fetching data is done!')
