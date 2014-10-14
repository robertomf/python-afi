# -*- coding: utf-8 -*-
from sqlalchemy import *
from sqlalchemy import exc  #por defecto no los incluye en el espacio de nombres

user='root'
pwd='E/BW9gFb'
host='localhost/Roberto%20Meijide/phpMyAdmin/'
database='test'


cad='mysql://'+user+':'+pwd+'@'+host+'/'+database
try:
    engine=create_engine(cad)
    engine.connect()  #establece una conexion
    engine.echo = True #True: Muestra las sentencias SQL que genera
except exc.OperationalError,e:
    print "ERROR: ", e.args[0]
    
metadata = MetaData(engine)

users = Table('clientes', metadata,
    Column('Id',Integer, primary_key=True,autoincrement=True),
    Column('Nombre', String(40)),
    Column('Apellidos', String(100)),
    Column('Edad', Integer),
    Column('Email',String(80)),
    Column('Password', String(20)),
)

## ##si se sabe previamente que la tabla esta creada
##users = Table('clientes', metadata, autoload=True)

if not users.exists():
    print 'Creamos la tabla datos'
    users.create()

i = users.insert()
i.execute(Nombre='Maria', Apellidos='Fdez Fdez',Edad=30, Email='ana@hotmail.com',Password='secret')
i.execute({'Nombre': 'Juan', 'Apellidos':'Diaz Fdez','Edad': 12,'Email':'juan@gmail.com','Password':'hola08'},
          {'Nombre': 'Teresa', 'Apellidos':'Diaz','Edad': 42,'Email':'maria@gmail.com','Password':'hola09'}
        )

s = users.select()
rs = s.execute()

row = rs.fetchone()
print 'ID:', row[0]
print 'Nombre:', row['Nombre']
print 'Edad:', row.Edad
print 'Password:', row[users.c.Password]

print '----------'
for row in rs:
    print 'Nombre= ',row.Nombre, ' Edad', row.Edad
        
    
s=users.select(users.c.Edad>20)
rs = s.execute()
for row in rs:
    print '----', row.Nombre, row.Apellidos, ' e-mail= ', row[users.c.Email]
    
def run(stmt):
    print '      ****     *****'
    rs = stmt.execute()
    for row in rs:
        print row
        
s=users.select( (users.c.Edad>20) & (users.c.Nombre!='Teresa') )
run(s)

s=users.select((users.c.Edad<20) | (users.c.Nombre!='Teresa') )
run(s)

s=users.select(~(users.c.Nombre=='Juan') )
run(s)
