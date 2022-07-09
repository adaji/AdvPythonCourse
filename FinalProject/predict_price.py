import mysql.connector
from mysql.connector import errorcode
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn import tree

# Downloading Data

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
    cur.execute("SELECT name, year, mileage, gearbox, fuel, damage, color, city FROM dataset")
    inp = cur.fetchall()
    cur.execute("SELECT price FROM dataset")
    out = cur.fetchall()
finally:
    if cur:
        cur.close()
    if cnx:
        cnx.close()


# Input data
new_car = [['hyundai-veracruz-ix55', 8, 160000, 1, 0, 0, 'سفید', 'تهران'],
           ['toyota-c-hr', 0, 2000, 1, 0, 0, 'سفید', 'تهران'],
           ['peugeot-405-glx', 0, 0, 0, 0, 0, 'خاکستری', 'تهران']]

for x in new_car:
    inp.append(x)
# Michasboonim tahe training data, badesh jodash mikonim, ghable TRAIN

# Start Pre-processing data
y = out

name = []
color = []
city = []
rest = []
for i in inp:
    name.append(i[0])
    rest.append(i[1:-2])
    color.append(i[-2])
    city.append(i[-1])

# Encode Name
values = np.array(name)
# integer encode
label_encoder = LabelEncoder()
integer_encoded = label_encoder.fit_transform(values)
# binary encode
name_ohe = OneHotEncoder(sparse=False)
integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
name_ohe = name_ohe.fit_transform(integer_encoded)

# Encode Color
values = np.array(color)
# integer encode
integer_encoded = label_encoder.fit_transform(values)
# binary encode
color_ohe = OneHotEncoder(sparse=False)
integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
color_ohe = color_ohe.fit_transform(integer_encoded)

# Encode City
values = np.array(city)
# integer encode
integer_encoded = label_encoder.fit_transform(values)
# binary encode
city_ohe = OneHotEncoder(sparse=False)
integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
city_ohe = city_ohe.fit_transform(integer_encoded)

x = np.column_stack((name_ohe, rest, color_ohe, city_ohe))

temp = np.split(x, [(-1)*len(new_car)])
x = temp[0]
new_car_enc = temp[1]
# Start training and testing
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)

# Encode New Car
answer = clf.predict(new_car_enc)
for i in range(len(answer)):
    print("The price of %s is approaximately %d Million Tomans." % (new_car[i][0], answer[i]))
