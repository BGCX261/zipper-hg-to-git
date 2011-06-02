#!/Library/Frameworks/Python.framework/Versions/Current/bin/python

import numpy as np
import pylab as lab
import polytest

infile = "/Users/simonspicer/Desktop/cat.txt"
intpt  = 0
N      = 300

A      = np.loadtxt(infile)
B      = A[:,0] +1j*A[:,1]
B      = B[:-1]

X      = polytest.polygon(B, intpt, N)
Y      = np.trim_zeros(X)

#lab.plot(lab.real(Y),lab.imag(Y),'r.')
#lab.show()

Z      = polytest.zipper(Y,intpt)


