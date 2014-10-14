#!/usr/bin/env python
# -*- coding: utf-8 -


from sqlalchemy import *
from sqlalchemy.orm import mapper, relationship,create_session
import sys

def conectar(user='usuario', pwd='tu_pwd', host='localhost',database='afi'):
  cad='mysql://'+user+':'+pwd+'@'+host+'/'+database
  try:
    engine=create_engine(cad)
    engine.connect()  #establece una conexion
    engine.echo = False #True: Muestra las sentencias SQL que genera
    return engine
    
  except exc.OperationalError,e:
    print "ERROR: ", e.args[0]
    return None

def crear_tablas(metadata):
  autor = Table('Autor', metadata,
    Column('id_autor', Integer, primary_key=True),
    Column('nombre', String(50),), 
    Column('email', String(100),unique=True), #si quisieramos que fuese unica: unique=True
  )
  if not autor.exists():
    autor.create()
    
  obra=Table('Obra',metadata,
    Column('id_obra',Integer,primary_key=True),
    Column('titulo',String(50)),
    Column('precio',Float),
    Column('id_autor',Integer,ForeignKey(autor.c.id_autor)),
  )
  
  if not obra.exists():
    obra.create()
  return [autor,obra]
  
#el nombre de los atributos de la clase tienen que coincider con las columnas
# de la tabla

class Autor(object):
  def __init__(self,nombre=None,email=None):
    self.nombre=nombre
    self.email=email
  
class Obra(object):
  def __init__(self,titulo='bla bla', precio=0,autor=None):
    self.titulo=titulo
    self.precio=precio
    self.autor=autor

    
if __name__=='__main__':
  engine=conectar()
  if engine==None:
    print 'Problemas al conectar'
    sys.exit()
    
  metadata = MetaData(engine)
  autor_tabla,obra_tabla=crear_tablas(metadata)
  
  
  #Información sobre atributos mapeados, tales como 
  #relaciones con otras clases, se propercionan mediante el 
  #diccionario properties
  
  #mapea Autor con autor_tabla
  mapper(Autor, autor_tabla,properties={'obras':relationship(Obra)})
  #mapea Obra con obra_tabla
  mapper(Obra,obra_tabla, properties={'autor':relationship(Autor)})
  



  #creamos dos instnacias de Autor
  juan=Autor( nombre='Juan', email='juan@hotmail.com')
  eva=Autor(nombre='Eva',email='eva@gmail.com')

  #creamos tres instancias de Obra
  obra1=Obra(titulo="Hola",precio=50.5,autor=juan)
  obra2=Obra(titulo="Escultura 1",precio=200, autor=eva)
  obra3=Obra(titulo="Pintura 2", precio=100,autor=juan)
  
  #creamos una sesion
  session = create_session()
  #anhadimos las instancias de tipo Obra a la sesion. De
  #este modo tambien se anhaden las instancias de tipo Autor (por
  # la relacion que hemos indicado)

  session.add(obra1)
  session.add(obra2)
  session.add(obra3)
  #session.add(juan)

  session.flush()

  # creamos otra session y la usamos para hacer consultas 
  #empleando las objetos mapeados
  session = create_session()
  query = session.query(Autor)
  Juan = query.filter_by(nombre="juan").first()
  
  # accedemos a los atributos del objeto Autor, 
  # incluidos los objetos relacionados
  print 'Nombre= ', Juan.nombre
  print 'Titulo de la Primera obra = ',Juan.obras[0].titulo
  print 'Nombre= ', Juan.obras[0].autor.nombre
  