#!/usr/local/bin/python

import numpy as np
import matplotlib.pyplot as plt

uniform   = np.load('../cost-comparison/cost-uniform.npy')
interface = np.load('../cost-comparison/cost-interface.npy')
dpn_15    = np.load('../cost-comparison/cost-dpn-1.5.npy')
dpn_20    = np.load('../cost-comparison/cost-dpn-2.npy')
dpn_27    = np.load('../cost-comparison/cost-dpn-2.7.npy')

plt.figure(figsize = (8,6), dpi = 300)
plt.plot(uniform / 3)
plt.plot(interface / 3)
plt.plot(dpn_15 / 3)
plt.plot(dpn_20 / 3)
plt.plot(dpn_27 / 3)
plt.yscale('log')
plt.xlabel('Number of iterations')
plt.ylabel('Value of the target function')
plt.legend(['Uniform', 'Interface',
            r'DPN, $\alpha = 1.5$', r'DPN, $\alpha = 2$', r'DPN, $\alpha = 2.7$'])
#plt.show()
plt.savefig('../target-plots/sampler-comparison.png')
