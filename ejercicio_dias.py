# -*- coding: utf-8 -*-

diasmes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

anho = input('Introduce un año: ')
if (anho <= 0):
	print ' ** El anho es incorrecto **'

mes = input('Introduce un mes: ')
if (mes < 0 or mes > 12):
	print ' ** El mes es incorrecto ** '

dia = input('Introduce un dia: ')
if (dia < 0 or dia > diasmes[mes-1]):
	print ' ** El dia es incorrecto ** '

total = 0
for i in range (mes-1):
	total += diasmes [i]
total += dia

print 'El numero de dias transcurridos es: ', total
