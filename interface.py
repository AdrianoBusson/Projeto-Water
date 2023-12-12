import mysql.connector
import subprocess
import os

# Conexão com MYSQL
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123",
  database="openiot"
)

mycursor = mydb.cursor()

#Leitura dos dados no MYSQL
mycursor.execute("SELECT recvTimeTs,attrname,attrValue FROM `urn_ngsi-ld_Device_001_Device` WHERE attrname = 'ph' ORDER BY recvTimeTs DESC limit 1")
retorno = mycursor.fetchone()
r1 = retorno[2]
print(r1)

mycursor.execute("SELECT recvTimeTs,attrname,attrValue FROM `urn_ngsi-ld_Device_001_Device` WHERE attrname = 'dureza' ORDER BY recvTimeTs DESC limit 1")
retorno = mycursor.fetchone()
r2 = retorno[2]
print(r2)

mycursor.execute("SELECT recvTimeTs,attrname,attrValue FROM `urn_ngsi-ld_Device_001_Device` WHERE attrname = 'solidos' ORDER BY recvTimeTs DESC limit 1")
retorno = mycursor.fetchone()
r3 = retorno[2]
print(r3)

mycursor.execute("SELECT recvTimeTs,attrname,attrValue FROM `urn_ngsi-ld_Device_001_Device` WHERE attrname = 'cloraminas' ORDER BY recvTimeTs DESC limit 1")
retorno = mycursor.fetchone()
r4 = retorno[2]
print(r4)

mycursor.execute("SELECT recvTimeTs,attrname,attrValue FROM `urn_ngsi-ld_Device_001_Device` WHERE attrname = 'sulfato' ORDER BY recvTimeTs DESC limit 1")
retorno = mycursor.fetchone()
r5 = retorno[2]
print(r5)

mycursor.execute("SELECT recvTimeTs,attrname,attrValue FROM `urn_ngsi-ld_Device_001_Device` WHERE attrname = 'condutividade' ORDER BY recvTimeTs DESC limit 1")
retorno = mycursor.fetchone()
r6 = retorno[2]
print(r6)

mycursor.execute("SELECT recvTimeTs,attrname,attrValue FROM `urn_ngsi-ld_Device_001_Device` WHERE attrname = 'carbono' ORDER BY recvTimeTs DESC limit 1")
retorno = mycursor.fetchone()
r7 = retorno[2]
print(r7)

mycursor.execute("SELECT recvTimeTs,attrname,attrValue FROM `urn_ngsi-ld_Device_001_Device` WHERE attrname = 'trihalometanos' ORDER BY recvTimeTs DESC limit 1")
retorno = mycursor.fetchone()
r8 = retorno[2]
print(r8)

mycursor.execute("SELECT recvTimeTs,attrname,attrValue FROM `urn_ngsi-ld_Device_001_Device` WHERE attrname = 'turbidez' ORDER BY recvTimeTs DESC limit 1")
retorno = mycursor.fetchone()
r9 = retorno[2]
print(r9)

#roda comando no front-end console
os.chdir('/home/ubuntu/rollups-examples/frontend-console')
os.system('yarn start input send --payload \"'+ r1 + ',' + r2 + ',' + r3 + ',' + r4 + ',' + r5 + ',' + r6 + ',' + r7 + ',' + r8 + ',' + r9 +'\"')
