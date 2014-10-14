import sys
# -*- coding: utf-8 -*-

#---------------------------------------------------------------------#

def bisiesto (anho):
	if (anho % 4 == 0 and (anho % 100 != 0 or anho % 400 == 0)):
		print '\n ** Año bisiesto ** \n', anho
		return True
	return False

#---------------------------------------------------------------------#

diasmes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

anho = input ('\n\nAño de nacimiento: ')
if (anho <= 0):
	print ' ** El anho es incorrecto ** '

mes = input ('Mes de nacimiento: ')
if (mes <= 0 or mes > 12):
	print ' ** El mes es incorrecto ** '

dia = input ('Dia de nacimiento: ')
if (dia < 0 or dia > diasmes[mes-1]):
	print ' ** El dia es incorrecto ** '

anho_nac = anho
mes_nac = mes
dia_nac = dia

#---------------------------------------------------------------------#

anho = input ('\n\nAño actual: ')
if (anho <= 0):
	print ' ** El anho es incorrecto ** '

mes = input ('Mes actual: ')
if (mes <= 0 or mes > 12):
	print ' ** El mes es incorrecto ** '

dia = input ('Dia actual: ')
if (dia < 0 or dia > diasmes[mes-1]):
	print ' ** El dia es incorrecto ** '

#---------------------------------------------------------------------#
# Dias transcurridos en el año actual.
if (bisiesto(anho)):
	diasmes[1] = 29;

total = 0
for i in range (mes-1):
	total += diasmes [i]
total += dia                              

#---------------------------------------------------------------------#
# Dias transcurridos en el año de nacimiento.
diasmes[1] = 28
if (bisiesto (anho_nac)):
	diasmes[1] = 29

for i in range (mes_nac+1, 12):
	total += diasmes [i]
total += diasmes[mes_nac] - dia                

#---------------------------------------------------------------------#

for anho in range (anho_nac+1, anho):
	if bisiesto (anho):
		total += 366
	else:
		total += 365

print '\n La edad es: ', total, ' dias \n'