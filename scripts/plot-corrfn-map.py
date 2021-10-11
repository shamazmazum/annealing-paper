#!/usr/local/bin/python

from sys import argv
import numpy as np
import matplotlib.pyplot as plt

mapname  = argv[1]
plotname = argv[2]
side     = int(argv[3])

diff = np.fromfile (mapname, dtype = np.float64)
diff = diff.reshape((side, side))
diff = np.abs(diff)

plt.figure(dpi=300)
plt.imshow(diff)
plt.savefig(plotname)
#plt.show()
