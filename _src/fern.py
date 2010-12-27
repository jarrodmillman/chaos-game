import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import rv_discrete as rv

A = np.array([[[0.0,0.0],[0.00,0.16]],
          [[0.85,0.04],[-0.04,0.85]],
          [[0.2,-0.26],[0.23,0.22]],
          [[-0.15,0.28],[0.26,0.24]]])

b = np.array([[0.00,0.00],
              [0.00,1.60],
              [0.00,1.60],
              [0.00,0.44]])

#next_transform = rv(name='Fern',values=((0,1,2,3),(0.01,0.85,0.0,0.14)))
next_transform = rv(name='Fern',values=((0,1,2,3),(0.01,0.85,0.07,0.07)))

def simplify_axes(ax):
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    ax.set_yticks([])
    ax.set_xticks([])
    ax.set_xlim(-2.3,2.8)
    ax.set_ylim(-0.1,10.1)


def next_point(last_point):
    transform = next_transform.rvs()
    return np.dot(A[transform],last_point) + b[transform]

def main():
    current = np.array([0.0, 0.0])

    fig = plt.figure()
    ax = fig.add_subplot(111)
    simplify_axes(ax)
    
    # Don't plot the first few iterations.
    for x in range(15):
      current = next_point(current)

    ax.plot(current[0], current[1], 'go', markersize=1)
    xs, ys = [], []
    line_fern, = ax.plot(xs, ys, 'go', markersize=1)

    for x in range(60000):
      current = next_point(current)
      xs.append(current[0])
      ys.append(current[1])
      line_fern.set_data(xs, ys)
    
    plt.show()

if __name__ in ("__main__","__plot__"):
    main()
