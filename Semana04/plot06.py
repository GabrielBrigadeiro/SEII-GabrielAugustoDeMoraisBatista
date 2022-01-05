import numpy as np
import matplotlib.pyplot as plt

x1 = np.arange(-1000,1000,1)

plt.plot(x1, -x1**3+4)
plt.show()