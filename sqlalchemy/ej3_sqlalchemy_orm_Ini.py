#!/usr/bin/env python
# -*- coding: utf-8 -


from sqlalchemy import *
from sqlalchemy.orm import *

user='usuario'
pwd='tupassword'
host='localhost'
database='tu_base_datos'



cad='mysql://'+user+':'+pwd+'@'+host+'/'+database
try:
    engine=create_engine(cad)
    engine.connect()  #establece una conexion
    engine.echo = False #True: Muestra las sentencias SQL que genera
except exc.OperationalError,e:
    print "ERROR: ", e.args[0]
    
metadata = MetaData(engine)

users_table = Table('users', metadata,
    Column('user_id', Integer, primary_key=True),
    Column('name', String(50)), 
    Column('age', Integer),
)

if not users_table.exists():
    users_table.create()


#Las clases tienen que ser Clases de Nuevo Estilo, sino 
# el codigo falla
class User(object):
    def __init__(self, user_id=None, name=None, age=None):#, password=None):
        self.user_id=user_id
        self.name = name
        self.age = age

    def __repr__(self):
        return '(%s, %i)'%(self.name,self.age)
    



# mapamos la tabla user
usermapper = mapper(User, users_table)

session = create_session()

##Query
user=User()
user.name='Ana'
user.age=15

session.add(user)

user=User()
user.name='Carl'
user.age=30

session.add(user)
session.flush()

# Consulta Select all
query=session.query(User) #crea un objeto de tipo Query para la clase User

# Obtiene todos los objetos User de la tabla
for user in query.all():
    print user.name, user.age

print '****'
# Selecciona el primer usuario con nombre "Ana"
mary = session.query(User).filter_by(name='Ana').first()
print mary.user_id, mary.name, mary.age
print '****' 
# selecciona los usuarios con nombre "Mary" o "Carl"
users = session.query(User).filter(User.name.in_(['Ana', 'Carl'])).all()

for u in users:
    print u.user_id, u.name, u.age
 
# selecciona todos los usuarios y muestra el resultado ordenado por edades
for instance in session.query(User).order_by(User.age):
    print instance.name, instance.age
