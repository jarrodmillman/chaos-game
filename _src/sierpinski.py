import random
import numpy as np
import matplotlib.pyplot as plt

corner = np.array([[0.0, 0.0], [1.0, 0.0], [0.5, 0.5]])

def simplify_axes(ax):
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    ax.set_yticks([])
    ax.set_xticks([])
    ax.set_xlim(corner[:,0].min()-0.1,corner[:,0].max()+0.1)
    ax.set_ylim(corner[:,1].min()-0.1,corner[:,1].max()+0.1)

def next_point(last_point):
    target_point = random.choice(corner)
    return (last_point + target_point) / 2

def main():
    current = np.array([0.0, 0.0])

    fig = plt.figure()
    ax = fig.add_subplot(111)
    simplify_axes(ax)
    
    # Don't plot the first few iterations.
    for x in range(15):
      current = next_point(current)

    ax.plot(current[0], current[1], 'ko', markersize=1)
    xs, ys = [], []
    line_sierp, = ax.plot(xs, ys, 'ko', markersize=1)

    for x in range(50000):
      current = next_point(current)
      xs.append(current[0])
      ys.append(current[1])
      line_sierp.set_data(xs, ys)
    
    plt.show()

if __name__ in ("__main__","__plot__"):
    main()
