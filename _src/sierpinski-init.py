import random
import numpy as np
import matplotlib.pyplot as plt

corner = np.array([[0.0, 0.0], [1.0, 0.0], [0.5, 0.5]])
current = np.array([0.15, 0.35])

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.set_yticklabels([])
ax1.set_xticklabels([])
ax1.set_yticks([])
ax1.set_xticks([])
ax1.set_xlim(corner[:,0].min()-0.1,corner[:,0].max()+0.1)
ax1.set_ylim(corner[:,1].min()-0.1,corner[:,1].max()+0.1)


fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.set_yticklabels([])
ax2.set_xticklabels([])
ax2.set_yticks([])
ax2.set_xticks([])
ax2.set_xlim(corner[:,0].min()-0.1,corner[:,0].max()+0.1)
ax2.set_ylim(corner[:,1].min()-0.1,corner[:,1].max()+0.1)

# Plot the corners of the bounding triangle
for x,y in corner:
  ax1.plot(x,y,'bo')
  ax2.plot(x,y,'bo')

# Plot the starting point
ax1.plot(current[0],current[1],'ro')
ax2.plot(current[0],current[1],'ro')

target=random.choice(corner)
current = (current+target)/2
ax1.plot(current[0],current[1],'ro',markersize=4)
ax2.plot(current[0],current[1],'ro',markersize=4)
plt.draw()

for x in range(19):
  target=random.choice(corner)
  current = (current+target)/2
  ax2.plot(current[0],current[1],'ko',markersize=2)
  plt.draw()

plt.show()
