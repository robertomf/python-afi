# --*-- encoding=utf-8 --*--
from sqlalchemy.ext.declarative import declarative_base
from controlador import *
from sqlalchemy.orm import mapper, relationship,create_session,sessionmaker
from sqlalchemy import exc

Base = declarative_base()
  
class Autor(Base):
    __tablename__ = 'autor'
    # seleccionamos el tipo de tablas (tambien podeis escoger InnoDB por defecto en my.cnf)
    __table_args__ = {'mysql_engine':'InnoDB'} 
    #__table_args__ = {'mysql_engine':'MyISAM'}
    id_autor = Column(Integer, primary_key=True,autoincrement=True)
    nombre=Column(String(100),unique = True)
    b_date=Column(Integer)
    d_date=Column(Integer)
    nacionalidad=Column(String(100)) 
    # relaciones ONE TO MANY with Libros
    libros = relationship("Libros", backref="autor")
    # para permitir cargar los datos
    def __init__(self,nombre=None, b_dat=None,d_date=None,nacionalidad=None):
      self.nombre = nombre
      
    
class Libros(Base):
    __tablename__ = 'libros'
    __table_args__ = {'mysql_engine':'InnoDB'}  # seleccionamos el tipo de tablas
    #__table_args__ = {'mysql_engine':'MyISAM'}
    id_libro = Column(Integer, primary_key=True,autoincrement=True)
    titulo=Column(String(100),unique = True)
    #autor=Column(String(100))
    editorial=Column(String(100))
    fecha=Column(Integer)
    precio=Column(Float)
    portada=Column(String(100)) # ruta a la portada del libro
    # relaciones con Autor
    id_autor=Column(Integer,ForeignKey('autor.id_autor'))
    
    def __init__(self,titulo=None, id_autor=None,editorial=None,fecha=None,precio=None,portada=None):
      self.titulo = titulo
      self.id_autor = id_autor
      self.editorial = editorial
      self.precio = precio
      self.fecha=fecha
      self.portada=portada
    def mostrar_libro(self):
      print self.titulo
    def get_libros(self,engine):
      session = sessionmaker(bind=engine)
      session=session()
      return session.query(Libros).all()
    def update_price(self,price):
      self.precio=price




    

