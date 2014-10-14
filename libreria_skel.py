# --*-- encoding=utf-8 --*--
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper, relationship,create_session,sessionmaker
from sqlalchemy import exc
from sqlalchemy import create_engine
from sqlalchemy import *

Base = declarative_base() #Todas las clases deben heredar de este objeto

class Autor(Base):
	__tablename__='autor'
	id_autor = Column(Integer, primary_key=True, autoincrement=True)	
	nombre = Column (String(100), unique=True)
	libros = relationship("Libros", backref="autor")
	def __init__(self, nombre=None):	
		self.nombre=nombre

class Libros(Base):
	__tablename__='libros'
	id_libro = Column(Integer, primary_key=True, autoincrement=True)
	titulo = Column(String(100), unique=True)
	editorial = Column(String(80))
	fecha = Column(Integer)
	precio = Column(Float)
	portada = Column (String(100))
	id_autor = Column(Integer, ForeignKey('autor.id_autor'))

	def __init__(self, titulo=None, editorial=None, fecha=None, precio=None, portada=None):
		self.titulo=titulo
		self.editorial=editorial
		self.fecha=fecha
		self.precio=precio
		self.portada=portada

def populate_database(L, session):
	L_libros=[]
	for d in L:
    		L_libros.append(Libros(titulo=d['titulo'],editorial=d['editorial'],fecha=d['fecha'],precio=d['precio']))

	session.add_all(L_libros)
	#session.commit()
	grabar_savepoints(session)
	
	author1 = Autor(nombre='Michael')
	author2 = Autor(nombre='John Doe')
	L_autores = [author1, author2]
	session.add_all(L_autores)
	grabar_savepoints(session)
	

# lee autores de fichero y los carga en BBDD
def lee_fich():
  keys = ['titulo','id_autor','editorial','fecha','precio','portada']
  f=file('libros.txt')
  L_libros=[]
  for line in f: 
    L=line.split(',')
    L=[x.strip('\'') for x in L]
    d=dict(zip(keys, L  ))
    L_libros.append(d)
  print L_libros
  return L_libros
  
# grabar con varios commits
def grabar_nosavepoints(session,records):
  #añadimos, mirando antes si está duplicado el elemento
  for a in records:
    print a
    try:
      session.add(a)
      session.commit()
    except :
      session.rollback()
      print 'Entrada duplicada'
    
def grabar_savepoints(session):
  # con save points: puntos de recuperacion
  for  record in session:
    try:
      with session.begin_nested():
	session.merge(record)
    except exc.IntegrityError,e:
      print "Skipped record %s" % record
      print e[0]
      session.rollback()
    session.commit()

def borrar_autor(sesion,nombre=None):
    autor=session.query(Autor).filter_by(nombre=nombre).first()
    if not autor:
	session.close()
	return -1
    else:
	session.delete(autor)
	session.commit() 
	session.close()
	return 0
	
def db_connect():
  # mysql://joseanto:josino652@localhost/empresa
  user='root'
  pwd='afi2012'
  host='localhost'
  database='Libreria'
  cad='mysql://'+user+':'+pwd+'@'+host+'/'+database
  engine=create_engine(cad, encoding='utf-8')
  return engine

def consulta_sql_raw(engine):
  records=engine.execute("SELECT * FROM libros WHERE titulo LIKE'%%5%%'") 
  for row in records:
    print 'Libros encontrados: ', row.titulo

  
if __name__=='__main__':
  L=lee_fich()
  engine=db_connect()
  #imprimimos datos de conexión
  print engine.name
  print engine.url
  
  #para generar los metadatos y poblar la BBDD
  Base.metadata.create_all(engine)
  
  
#creamos una sesion
  Session = sessionmaker(bind=engine)
  session=Session()
  grabar_savepoints(session)
  populate_database(L,session)

  consulta_sql_raw(engine)

  borrar_autor(session, 'Michael')

