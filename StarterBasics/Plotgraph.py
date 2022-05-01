#Plotting a Graph#
#Example1#
import matplotlib.pyplot as plt
import numpy as np

a=[x for x in xrange(10)]
b=np.square(a)
plt.plot(a,b)
plt.show()

#Example2#
import matplotlib.pyplot as plt

X = range(10)
plt.plot(X, [x*x for x in X])
plt.show()