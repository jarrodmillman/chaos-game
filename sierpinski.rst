Sierpinski's Gasket: the chaos game animated with matplotlib
============================================================

The standard way to describe the construction of the Sierpinski Gasket using
the chaos game techinque is as follows:

#. Choose 3 points in the plane (forming a triangle).
#. Choose another "starting" pointing (current position).
#. Randomly choose one of the corners of the triangle.
#. Move halfway from your current position to the selected corner.
#. Plot the new current position.
#. Repeat from step 3.

To make illustrate the above procedure, let's look at the first few iterations
of the algorithm:

.. plot:: _src/sierpinski-init.py

In both plots, I've colored the vertices of the triangle blue and the initial
point red.  In the first figure, I've also shown the first iteration of the
algorithm with a red dot, which should be half way between the initial point
and one of the corners of the triangle.  In the second figure, I've shown the
first 20 iterations of the algorithm.  After the first iteration of the
algorithm, I used smaller black points. 

Here is what it looks like with 50,000 iterations:

.. plot:: _src/sierpinski.py

A simple Python program
-----------------------

The basic program looks something like this:

.. plot:: _src/sierpinski-simple.py
   :include-source:

There are a few interesting tricks, though, to getting a nice animation of this
with matplotlib.

Speeding it up
--------------

...

Animating it
------------

::

    #!/usr/bin/env python
    """
    Animated construction of the Sierpinski gasket using the chaos game.
    """
    
    import random
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
    
    
    corner = np.array([[0.0, 0.0], [1.0, 0.0], [0.5, 0.5]])
    xs, ys = [], []
    
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
    
    def update_line(i):
        next = next_point(update_line.current)
    
        xs.append(next[0])
        ys.append(next[1])
        update_line.serp.set_data(xs, ys)
    
        update_line.current = next
    
    def main():
        current = [0.15, 0.35]
    
        fig = plt.figure()
        ax = fig.add_subplot(111)
        simplify_axes(ax)
    
        # Don't plot the first few iterations.
        for x in range(15):
          current = next_point(current)
        ax.plot(current[0], current[1], 'ko', markersize=1)
    
        update_line.current = current
        update_line.serp, = ax.plot(xs, ys, 'go', markersize=1)
    
        ani = animation.FuncAnimation(fig, update_line, 1000, interval=10, repeat=False)
        plt.show()
    
    if __name__ == "__main__":
        main()

