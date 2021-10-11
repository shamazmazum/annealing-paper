#!/usr/local/bin/python

from sys import argv
import numpy as np
import matplotlib.pyplot as plt

source = argv[1]
dest   = argv[2]

data = np.load(source)

plt.figure(dpi = 230)
plt.plot(data)
plt.yscale('log')
plt.xlabel('Number of iterations')
plt.ylabel('Value of the target function')
plt.savefig(dest)
