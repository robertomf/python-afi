#!/usr/bin/env python
# -*- coding: utf-8 -*-

from string import *
import os
# Modlo para generar contraseña encriptada en SHA512
import crypt


filename='users.txt'

etc_dir='/etc/'
home='/home/'
# Encriptamos la contraseña
default_passwd=crypt.crypt("passwd123", "$6$somesalt$")

f=open(filename, "r")

directories=[]

group_id=2000  # empiezo a contar el grupo en 2000
for a in f.readlines():
    user_name=a.strip()
    #print dir
    if user_name != '':
	directories.append(user_name)
	if not os.path.exists(home+user_name):
	    group_id=group_id+1 #incremento id de usuario
	    
	    print 'Añadiendo usuarios al sistema'
	    
	    # creamos el grupo
	    open(etc_dir+'group',"a+b").write(user_name+':x:'+str(group_id)+':\n') 
	    # asignamos el usuario al  grupo
	    open(etc_dir+'passwd',"a+b").write(user_name+':x:'+str(group_id)+':'+str(group_id)+':'+user_name+',,,:'+home+user_name+':/bin/bash\n') 
	    # asignamos a todos el passwd por defecto
	    open(etc_dir+'shadow',"a+b").write(user_name+':'+default_passwd+':15268:0:99999:7:::\n')

	    print 'Creando directorio home: '+home+user_name
	    os.mkdir(home+user_name)
	print 'Cambiado el permiso de: '+home+user_name
	os.chmod(home+user_name,0750)   # permisos del directorio
	print 'Cambiado el propietario de: '+home+user_name
	os.system('chown -R '+ user_name+':'+user_name+' '+home+user_name) # propietario del directorio
    
print 'Lista de usuarios creados:'
print directories
f.close()
    
