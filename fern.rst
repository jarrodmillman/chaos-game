Barnsley Fern
=============

Ferns are a good example of a self-similar natural object.  
In his book titled **Fractals Everywhere**, Michael Barnsley
described a IFS construction, which closely resembles a
Black Spleenwort fern (Asplenium adiantum-nigrum).  It can
be constructed using the chaos game just like Sierpinski's
gasket.

The Barnsley Fern can be described by 4 affine transforms.  An
affine transform can be specified via the following formula:

.. math::

    f(x,y) = \begin{bmatrix} \ a & \ b \ \\ c & \ d \end{bmatrix} \begin{bmatrix} \ x \\ y \end{bmatrix} + \begin{bmatrix} \ e \\ f \end{bmatrix} 

Or in vector notation:

.. math::

    \vec{y} = A \vec{x} + \vec{b}

Writing that in Python:

::

    np.dot(A,x) + b

Here are the 4 affine transforms used to construct the Barnsley fern:

.. math::

    f_1(x,y) = \begin{bmatrix} \ 0.00 & \ 0.00 \ \\ 0.00 & \ 0.16 \end{bmatrix} \begin{bmatrix} \ x \\ y \end{bmatrix}

    f_2(x,y) = \begin{bmatrix} \ 0.85 & \ 0.04 \ \\ -0.04 & \ 0.85 \end{bmatrix} \begin{bmatrix} \ x \\ y \end{bmatrix} + \begin{bmatrix} \ 0.00 \\ 1.60 \end{bmatrix}

    f_3(x,y) = \begin{bmatrix} \ 0.20 & \ -0.26 \ \\ 0.23 & \ 0.22 \end{bmatrix} \begin{bmatrix} \ x \\ y \end{bmatrix} + \begin{bmatrix} \ 0.00 \\ 1.60 \end{bmatrix}

    f_4(x,y) = \begin{bmatrix} \ -0.15 & \ 0.28 \ \\ 0.26 & \ 0.24 \end{bmatrix} \begin{bmatrix} \ x \\ y \end{bmatrix} + \begin{bmatrix} \ 0.00 \\ 0.44 \end{bmatrix} 

In Python, we can represent this using NumPy's ``nd-arrays``:

::

    A = np.array([[[0.0,0.0],[0.00,0.16]],
              [[0.85,0.04],[-0.04,0.85]],
              [[0.2,-0.26],[0.23,0.22]],
              [[-0.15,0.28],[0.26,0.24]]])
    
    b = np.array([[0.00,0.00],
                  [0.00,1.60],
                  [0.00,1.60],
                  [0.00,0.44]])


Like the algorithm used to construct Sierpinski's gasket, we will iteratively draw points
selected as follows:

#. Start with the point (0,0)
#. Plot the starting point
#. Randomly select one of the affine transforms
#. Apply the selected affine transform to the previous point to ovtain
   the next point
#. Plot the new point
#. Repeat from step 3

Unlike the Sierpinski gasket, the affine transform selected in step 3 isn't
choosen with equal likelihood.  Instead we select the affine transform according
to the following probability table:

   ================    ===========
   affine transform    probability
   ================    ===========
   :math:`f_1`         0.01
   :math:`f_2`         0.85
   :math:`f_3`         0.07
   :math:`f_4`         0.07
   ================    ===========

The SciPy stats module provide a convenient function, ``scipy.stats.rv_discrete``,
which we can use to represent this distribution:

::

  from scipy.stats import rv_discrete as rv
  next_transform = rv(name='Fern',values=((0,1,2,3),(0.01,0.85,0.07,0.07)))

Now we can use ``next_transform.rvs()`` to choose one of the affine transforms
according the to the probability distribution described in the above table:

::

    def next_point(last_point):
        transform = next_transform.rvs()
        return np.dot(M[transform],last_point) + C[transform]

Iterating the described algorithm sixty thousand times results in this:

.. plot:: _src/fern.py

Finally, we can use the ``matplotlib.animation`` module to animate the
Barnsley fern like this::

    #!/usr/bin/env python
    """
    Animated construction of the Sierpinski gasket using the chaos game.
    """
    
    import random
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
    from scipy.stats import rv_discrete as rv
    
    
    A = np.array([[[0.0,0.0],[0.00,0.16]],
              [[0.85,0.04],[-0.04,0.85]],
              [[0.2,-0.26],[0.23,0.22]],
              [[-0.15,0.28],[0.26,0.24]]])
    
    b = np.array([[0.00,0.00],
                  [0.00,1.60],
                  [0.00,1.60],
                  [0.00,0.44]])
    
    next_transform = rv(name='Fern',values=((0,1,2,3),(0.01,0.85,0.07,0.07)))
    
    xs, ys = [], []
    
    def simplify_axes(ax):
        ax.set_yticklabels([])
        ax.set_xticklabels([])
        ax.set_yticks([])
        ax.set_xticks([])
        ax.set_xlim(-2.3,2.8)
        ax.set_ylim(-0.1,10.1)
    
    .
    int(last_point):
        transform = next_transform.rvs()
        return np.dot(A[transform],last_point) + b[transform]
    
    
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
        ax.plot(current[0], current[1], 'go', markersize=1)
    
        update_line.current = current
        update_line.serp, = ax.plot(xs, ys, 'go', markersize=1)
    
        ani = animation.FuncAnimation(fig, update_line, 1000, interval=10, repeat=False)
        plt.show()
    
    if __name__ == "__main__":
        main()

