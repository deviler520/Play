import matplotlib.pyplot as plt
import numpy as np
import math

theta = [i*np.pi/50 for i in range(201)]
r = [(1-math.sin(i)) for i in theta]
ax = plt.subplot(111, projection='polar')
ax.plot(theta, r, linewidth=2, color='red')
plt.title("ρ=1-sinθ", color='blue', fontdict={"fontsize": 20})
plt.show()
