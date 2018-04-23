# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 15:59:58 2018

@author: Tankiso
"""
import numpy
import pylab

#Problem3
a=0
b=numpy.pi/2

def steps(n):
	x = numpy.linspace(a,b,n)
	return x
	
m = [10,30,100,300,1000]
for n in m:
    x=numpy.linspace(a,b,n)
    y=numpy.cos(x)
    method=numpy.sum(y)*(x[-1]-x[0])/n
    er=1-method
    print 'Intergral = ' + repr(method) + ' with no. of points = ' + repr(er)
    
#Problem4
def simpsonsrule(n):  
    dx=b/(n-1)*2
    Xn=numpy.cos(steps(n))
    Xe=Xn[2::2]     #Taking all even points from an array, but skipping 1st and last points
    Xo=Xn[1:-1:2]   #Taking odd points from an array
    total=(Xn[0]/6+numpy.sum(Xo)*2/3+numpy.sum(Xe)*1/3+Xn[-1]/6)*dx
    return total
#The more the number of point the less the error.
#we used infinite number of points


#Problem5
if __name__=='__main__':
		final=simpsonsrule(11)
		err=numpy.abs(final-1)
		print 'Final answer = ' + repr(final)
		print '11 points error = ' + repr(err)
m = [10,30,100,300,1000]
for n in m:
    err=abs(simpsonsrule(n)-1)
    print 'The error for ' + repr(n) + ' points is ' + repr(err)
			
#Problem6
m = [11,31,101,301,1001,3001,10001,3001,100001]
m = numpy.array(m)
simpsonserr=numpy.zeros(m.size)
methoderr=numpy.zeros(m.size)
for t in range(m.size):
    n=m[t]
    dx=b/n
    x=numpy.linspace(a,b,n)
    y=numpy.cos(x)
    method=y.sum()*dx
    simpsonserr[t]=numpy.abs(simpsonsrule(n)-1)
    methoderr[t]=numpy.abs(method-1)
pylab.plot(m,methoderr,'g-o')
pylab.plot(m,simpsonserr,'b-o')
ax=pylab.gca()
ax.set_yscale('log')
ax.set_xscale('log')

    
