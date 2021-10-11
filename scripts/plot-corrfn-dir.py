#!/usr/local/bin/python

from os import path
from sys import argv
import numpy as np
import matplotlib.pyplot as plt

directory = argv[1]
plotname  = argv[2]

s2diff  = np.loadtxt(path.join(directory, 's2diff.dat'))
l2vdiff = np.loadtxt(path.join(directory, 'l2vdiff.dat'))
l2sdiff = np.loadtxt(path.join(directory, 'l2sdiff.dat'))
ssdiff  = np.loadtxt(path.join(directory, 'ssdiff.dat'))
svdiff  = np.loadtxt(path.join(directory, 'svdiff.dat'))
c2diff  = np.loadtxt(path.join(directory, 'c2diff.dat'))

plt.figure(dpi=300, figsize = (7.73, 5.8))
plt.xlabel('Correlation length, $r$')
plt.ylabel('$F_{orig}(r) - F_{recon}(r)$')
ax1  = plt.gca()
ax2 = ax1.twinx()
plt.ylabel('$C_{2_{orig}}(r) - C_{2_{recon}}(r)$')

ax1.ticklabel_format(scilimits = (0, 0))
ax2.ticklabel_format(scilimits = (0, 0))

ax1.plot(s2diff)
ax1.plot(l2vdiff)
ax1.plot(l2sdiff)
ax1.plot(ssdiff)
ax1.plot(svdiff)
ax2.plot(c2diff, 'r--')
ax1.legend(['$S_2$', '$L_2^{(0)}$', '$L_2^{(1)}$', '$F_{ss}$', '$F_{sv}$', '$C_2$'])
ax2.legend(['$C_2$'], loc = 9)
plt.savefig(plotname)
#plt.show()
