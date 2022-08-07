import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('simdata.txt',delimiter=',')

vleft = np.diff(data[:,6])/np.diff(data[:,0])


plt.figure()
plt.plot(data[1:,0],vleft)
plt.show()
