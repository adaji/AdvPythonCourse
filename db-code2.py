import mysql.connector
from mysql.connector import errorcode

u = input("Username: ")
p = input("Password: ")

# Validation
u_exp = u.split('@')[0]
u_domain1 = u.split('@')[1].partition('.')[0]
u_domain2 = u.split('@')[1].partition('.')[2]

while not (u_exp.isidentifier() and u_domain1.isalnum() and u_domain2.isalpha() and p.isalnum()):
    print("Note: Wrong Email/Password Format!")
    print("      Email Example: ali.dajmar@anyletternumber.anyletter")
    print("      Password Example: abc478dcy - Only letters and numbers")

    u = input("Username: ")
    p = input("Password: ")

    u_exp = u.split('@')[0]
    stemp = u.split('@')[1].partition('.')
    u_domain1 = stemp[0]
    if stemp[2][-1].isprintable():
        u_domain2 = stemp[2]
    else:
        u_domain2 = stemp[2][:-1]
# End Validation
# Insert into database

config = {'user': 'root', 'password': 'mydbpassword',
          'host': '127.0.0.1', 'database': 'employees'}
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
    cur.execute('INSERT INTO login VALUES (%s,%s)', (u.casefold(), p))
    cnx.commit()
finally:
    if cur:
        cur.close()
    if cnx:
        cnx.close()
# End insert into database
print('Data has been succesfully entered into databses.')
