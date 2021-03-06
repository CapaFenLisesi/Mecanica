#!/usr/bin/env python
from pylab import *
from matplotlib import rc
import sys
rc('text', usetex=True)

A=np.zeros((6,2))
A[0]=np.array([0,0])
A[1]=np.array([22.3,26.1])
A[2]=np.array([40.1,38.1])
A[3]=np.array([55.5,39.2])
A[4]=np.array([69.1,31.0])
A[5]=np.array([80.8,14.8])
#plt.plot(A[:,0],A[:,1],'k-',lw=2)
x=A[:,0]
y=A[:,1]
p=np.poly1d(np.polyfit(x,y,3))
xx=np.linspace(x[0],x[-1])
plt.plot(x,y,'ro')
plt.plot(xx,p(xx),'k-')
plt.xlabel(r'$x$ [m]',size=20)
plt.ylabel(r'$y$ [m]',size=20)
       
#plt.ylim(0,120)
#plt.xlim(0,2.2)
plt.grid()
plt.savefig('flyingballpy.pdf')
#plt.show()

sys.exit()

plt.vlines(1,ylim()[0],70,color='b', linestyles='dashed')
plt.ylim(0,120)
plt.xlim(0.,2.2)
plt.text(1.05,35,r'$v_1=\bar{v}_1=\frac{70\ \hbox{Km}}{1\ \hbox{h}}=70\ \hbox{Km/h}$',fontsize=20)
plt.text(0.8,72,'(1,30)',size=20)
#plt.savefig('vinstaprom2.pdf')


plt.vlines(2,70,100,color='g', linestyles='dashed')
plt.hlines(70,1,2,color='g', linestyles='dashed')
plt.text(1.9,102,'(2,100)',size=20)
plt.ylim(0,120)
plt.xlim(0.,2.2)
#plt.savefig('vinstaprom3.pdf')

plt.show()
#
