import random
import numpy as np
import matplotlib.pyplot as plt

corner = np.array([[0, 0], [1, 0], [0.5, 0.5]])
current = np.array([0.15, 0.35])

def next_point(last_point):
    target_point = random.choice(corner)
    return (last_point + target_point) / 2

fig=plt.figure()
ax=fig.add_subplot(111)

for x in range(50):
  current = next_point(current)
  ax.plot(current[0],current[1],'ko')
  plt.draw()

plt.show()
