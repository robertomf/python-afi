''' listing 6: pi_mp.py
 
Multiprocessing based code to estimate the value of PI
using monte carlo sampling 
Ref: http://math.fullerton.edu/mathews/n2003/montecarlopimod.html
Uses workers: 
http://docs.python.org/library/multiprocessing.html#module-multiprocessing.pool
'''
 
import random
import multiprocessing
from multiprocessing import Pool
import time
 
#caculate the number of points in the unit circle
#out of n points
def monte_carlo_pi_part(n):
    
    count = 0
    for i in range(n):
        x=random.random()
        y=random.random()
        
        # if it is within the unit circle
        if x*x + y*y <= 1:
            count=count+1
        
    #return
    return count
 
 
if __name__=='__main__':
    
    np = multiprocessing.cpu_count()
    print 'Usted tien {0:1d} CPUs'.format(np)
 
    # Numero de puntos a emplear para el calculo de pi
    n = 10000000
    
    # iterable con una lista de puntos que se generan en cada hilo
    # cada proceso emplea n/np puntos para el calculo de pi
 
    part_count=[n/np for i in range(np)]
 
    #Crear los hilos
    # http://docs.python.org/library/multiprocessing.html#module-multiprocessing.pool
    pool = Pool(processes=np)   
 
    t0=time.time()
    # parallel map
    count=pool.map(monte_carlo_pi_part, part_count)
    print 'Tiempo de CPU empleado: ', time.time()-t0
 
    print "Valor estimado de Pi:: ", sum(count)/(n*1.0)*4 
