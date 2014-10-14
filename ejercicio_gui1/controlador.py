# -*- coding: utf-8 -*-
from sqlalchemy import *
from sqlalchemy import exc  #por defecto no los incluye en el espacio de nombres
import subprocess 
from model_libros import*


class Database:
    
    engine=None
    
    def conectar_bd(self):
        user='root'; pwd='afi2012';host='localhost';database='libreria'
        cadena_conexion='mysql://'+user+':'+pwd+'@'+host+'/'+database
        
        try:
            engine=create_engine(cadena_conexion, encoding='utf8')    #creamos las tablas con encoding utf8
            #engine=create_engine(cad,encoding='latin1')  #creamos las tablas con encoding latin-1
            engine.connect()  #establece una conexion
            engine.echo = False #True: Muestra las sentencias SQL que genera
            print 'Conexion realizada con exito'
            print 'Base de datos: ', engine.name
            self.engine=engine
            self.populate_database(engine)
        except exc.OperationalError,e:
            print "ERROR: ", e.args[0]
    
    # creamos las tablas (si no estan creadas)
    # e insertamos los libros desde ficheros (si no estaban ya insertados
    def populate_database(self,engine):

        #Cargamos el gestor de Metadatos
        metadata = MetaData(engine)
        print "Conecion DB"
        Base.metadata.create_all(engine) # creamos las tablas
        

        self.rellena_tablas() # rellenamos las tablas si no están resllenas

    #insertar libros en la BD
    def insertar_libro(self,dic_datos_libro=None):
	d=dic_datos_libro
	#creamos una sesion
        Session = sessionmaker(bind=self.engine)
        session = Session()
	autor_record=self.buscar_autor(nombre=d['autor'])
            
        if not autor_record: # si no lo encuentro lo añadimos a la BBDD
            autor=Autor()
            autor.nombre=d['autor']
            session.add(autor)
            session.commit()
            autor_record=autor
                
            libro=Libros(titulo=d['titulo'].decode('utf8'),id_autor=autor_record.id_autor,editorial=d['editorial'],\
            fecha=d['fecha'],precio=d['precio'],portada=d['portada'])
            
        session.add(libro)
        session.commit()
        session.close()
    
    #creamos tablas de autores desde fichero
    def rellena_tablas(self):  
        #creamos una sesion
        Session = sessionmaker(bind=self.engine)
        session = Session()  
            
        #autor1=Autor(nombre='Michael Ruphus')
        #autor2=Autor(nombre='Michael Ruphus bis')
        #autor3=Autor(nombre='Tolkien')
        #session.add_all([autor1,autor2,autor3])

        #grabar_savepoints(session) #transaccion con savepoints


        # creamos tablas de libros
        L=lee_fich()
        L_libros=[]
        print 'Diccionario leido de fichero',L

        for d in L:
            print d
            autor_record=self.buscar_autor(nombre=d['autor'])
            
            if not autor_record: # si no lo encuentro lo añadimos a la BBDD
                autor=Autor()
                autor.nombre=d['autor']
                session.add(autor)
                session.commit()
                autor_record=autor
                
            L_libros.append(Libros(titulo=d['titulo'].decode('utf8'),id_autor=autor_record.id_autor,editorial=d['editorial'],\
            fecha=d['fecha'],precio=d['precio'],portada=d['portada']))
            
        session.add_all(L_libros)
        grabar_savepoints(session)
        session.close()
        
        
    # Ejemplo de cómo ejecutar sentecias SQL RAW en SQL Alchemy
    def busca_libro_sql(self,titulo,autor):
        return self.engine.execute("SELECT * FROM libros WHERE titulo LIKE '%%"+titulo+"%%' ")
        

    def busca_libro(self,titulo,autor):
        #p = self.engine.execute("SELECT * FROM libros WHERE titulo LIKE '%%"+titulo+"%%' ")
        #q=self.buscar_autor(nombre=autor)
        Session = sessionmaker(bind=self.engine)
        session = Session()     
        record = session.query(Autor,Libros).filter(Autor.nombre.like("%"+autor+"%")).\
        filter(Libros.id_autor == Autor.id_autor). filter(Libros.titulo.like("%"+titulo+"%")).all() 
        session.close()
	for (autor, libro) in record:
		print 'Titulo: ', libro.titulo, '-->', 'Autor: ', autor.nombre
        return record
        
    def borrar_autor(self,nombre=None):
        #creamos una sesion
        Session = sessionmaker(bind=self.engine)
        session = Session() 
        autor=session.query(Autor).filter_by(nombre=nombre).first()
        if not autor:
            session.close()
            return -1
        else:
            session.delete(autor)
            session.commit() 
            session.close()
            return 0      
            
    def buscar_autor(self,nombre=None):
        #creamos una sesion
        Session = sessionmaker(bind=self.engine)
        session = Session() 
        autor=session.query(Autor).filter_by(nombre=nombre).first()
        if not autor:
            session.close()
            return None
        else:
            session.close()
            return autor
 
            
# lee autores de fichero y los carga en BBDD
def lee_fich():
  name = ['titulo','autor','editorial','fecha','precio','portada']
  f=file('libros.txt')

  L_libros=[]
  for line in f: 
    L=line.split(',')
    L=[x.strip('\'') for x in L]
    d=dict(zip(name, L  ))
    L_libros.append(d)

  return L_libros
  
# Hacer un commit multiple con puntos de recuperacion
def grabar_savepoints(session):
    # con save points: puntos de recuperacion
    for record in session:
        try:
            with session.begin_nested():
                session.merge(record)
        except exc.IntegrityError,e:
            print "Skipped record %s" % record
            print e[0]
            session.rollback()
        session.commit()
        
    
