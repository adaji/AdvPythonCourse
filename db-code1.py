import mysql.connector
from mysql.connector import errorcode

config = {'user': 'root', 'password': 'mydbpassword',
          'host': '127.0.0.1', 'database': 'employees'}


cnx = cur = None
data = []
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
    cur.execute('select * from people')
    for (name, weight, height) in cur:
        data.append([name, height, weight])
finally:
    if cur:
        cur.close()
    if cnx:
        cnx.close()


data.sort(key=lambda x: x[2])
data.sort(key=lambda x: x[1], reverse=True)

for x in data:
    print("%s %d %d" % tuple(x))
