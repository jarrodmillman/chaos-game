import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import rv_discrete as rv

class ChaosGame():

    def __init__(self,A,b,next_transform):

        self.A = A
        self.b = b
        self.next_transform = next_transform
        self.initial_point = np.array([0.0, 0.0]) 

    def set_xylim(self,xs,ys):
        xlim = [min(xs),max(xs)]
        xscale = (xlim[1]-xlim[0])*0.1
        xlim[0] -= xscale
        xlim[1] += xscale
        ylim = [min(ys),max(ys)]
        yscale = (ylim[1]-ylim[0])*0.1
        ylim[0] -= yscale
        ylim[1] += yscale
        return xlim, ylim

    def simplify_axes(self,ax,xs,ys):
        ax.set_yticklabels([])
        ax.set_xticklabels([])
        ax.set_yticks([])
        ax.set_xticks([])
        xylim = self.set_xylim(xs,ys)
        ax.set_xlim(xylim[0])
        ax.set_ylim(xylim[1])

    def next_point(self,last_point):
        transform = self.next_transform.rvs()
        return np.dot(self.A[transform],last_point) + self.b[transform]
    
    def run(self):
    
        fig = plt.figure()
        ax = fig.add_subplot(111)
        
        # Don't plot the first few iterations.
        current = self.initial_point
        for x in range(15):
          current = self.next_point(current)
    
        xs, ys = [], []
        line_fractal, = ax.plot(xs, ys, 'ko', markersize=1)
    
        for x in range(50000):
          current = self.next_point(current)
          xs.append(current[0])
          ys.append(current[1])
          line_fractal.set_data(xs, ys)
        
        self.simplify_axes(ax,xs,ys)
        plt.show()

def mk_sierpinski():

    A = np.array([[[ 0.50, 0.00],[ 0.00, 0.50]],
                  [[ 0.50, 0.00],[ 0.00, 0.50]],
                  [[ 0.50, 0.00],[ 0.00, 0.50]]])
    
    b = np.array([[ 0.00, 0.00],
                  [ 0.50, 0.00],
                  [ 0.25, 0.25]])
    
    next_transform = rv(name='Sierpinski',values=((0,1,2),(0.33,0.33,0.33)))

    return ChaosGame(A,b,next_transform)

def mk_fern():

    A = np.array([[[ 0.00, 0.00],[ 0.00, 0.16]],
                  [[ 0.85, 0.04],[-0.04, 0.85]],
                  [[ 0.20,-0.26],[ 0.23, 0.22]],
                  [[-0.15, 0.28],[ 0.26, 0.24]]])
    
    b = np.array([[ 0.00, 0.00],
                  [ 0.00, 1.60],
                  [ 0.00, 1.60],
                  [ 0.00, 0.44]])
    
    next_transform = rv(name='Fern',values=((0,1,2,3),(0.01,0.85,0.07,0.07)))

    return ChaosGame(A,b,next_transform)

def mk_koch():

    A = np.array([[[ 0.33, 0.00],[ 0.00, 0.33]],
                  [[ 0.33, 0.00],[ 0.00, 0.33]],
                  [[ 0.16,-0.28],[ 0.28, 0.16]],
                  [[-0.16, 0.28],[ 0.28, 0.16]]])
    
    b = np.array([[ 0.00, 0.00],
                  [ 0.66, 0.00],
                  [ 0.33, 0.00],
                  [ 0.66, 0.00]])
    
    next_transform = rv(name='Fern',values=((0,1,2,3),(0.25,0.25,0.25,0.25)))

    return ChaosGame(A,b,next_transform)

def mk_koch1():

    A = np.array([[[ 0.33, 0.00],[ 0.00, 0.33]],
                  [[ 0.33, 0.00],[ 0.00, 0.33]],
                  [[ 0.16, 0.28],[-0.28, 0.16]],
                  [[-0.16, 0.28],[ 0.28, 0.16]]])
    
    b = np.array([[ 0.00, 0.00],
                  [ 0.66, 0.00],
                  [ 0.33, 0.00],
                  [ 0.66, 0.00]])
    
    next_transform = rv(name='Koch',values=((0,1,2,3),(0.25,0.25,0.25,0.25)))

    return ChaosGame(A,b,next_transform)

def mk_bronchi():

    A = np.array([[[ 0.05, 0.00],[ 0.00, 0.50]],
                  [[ 0.05, 0.00],[ 0.00,-0.50]],
                  [[ 0.00,-0.80],[ 0.60, 0.00]],
                  [[ 0.00, 0.80],[-0.65, 0.00]]])
    
    b = np.array([[ 0.00, 0.00],
                  [ 0.00, 0.80],
                  [ 0.00, 0.80],
                  [ 0.00, 0.80]])
    
    next_transform = rv(name='Bronchi',values=((0,1,2,3),(0.15,0.15,0.35,0.35)))

    return ChaosGame(A,b,next_transform)

def mk_helecho():

    A = np.array([[[ 0.00000, 0.0000],[ 0.00   , 0.17000]],
                  [[ 0.84962, 0.0255],[-0.0255 , 0.84962]],
                  [[-0.15540, 0.2350],[ 0.19583, 0.18648]],
                  [[ 0.1554 ,-0.235 ],[ 0.19583, 0.18648]]])
    
    b = np.array([[ 0.00, 0.00],
                  [ 0.00, 3.00],
                  [ 0.00, 1.20],
                  [ 0.00, 3.00]])
    
    next_transform = rv(name='Helecho',
             values=((0,1,2,3),(0.0572,0.5724,0.1852,0.1852)))

    return ChaosGame(A,b,next_transform)

def mk_hoja():

    A = np.array([[[ 0.64987,-0.013 ],[ 0.013  , 0.64987]],
                  [[ 0.64948,-0.026 ],[ 0.026  , 0.64948]],
                  [[ 0.3182 ,-0.3182],[ 0.3182 , 0.3182 ]],
                  [[-0.3182 , 0.3182],[ 0.3182 , 0.3182 ]]])
    
    b = np.array([[ 0.175, 0.00 ],
                  [ 0.165, 0.325],
                  [ 0.2  , 0.00 ],
                  [ 0.8  , 0.00 ]])
    
    next_transform = rv(name='Helecho',
             values=((0,1,2,3),(0.3333,0.3333,0.1667,0.1667)))

    return ChaosGame(A,b,next_transform)

def mk_arbol():

    A = np.array([[[ 0.05 , 0.00 ],[ 0.00 , 0.6  ]],
                  [[ 0.05 , 0.00 ],[ 0.00 ,-0.5  ]],
                  [[ 0.46 ,-0.32 ],[ 0.39 , 0.38 ]],
                  [[ 0.47 ,-0.15 ],[ 0.17 , 0.42 ]],
                  [[ 0.43 , 0.28 ],[-0.25 , 0.45 ]],
                  [[ 0.42 , 0.26 ],[-0.35 , 0.31 ]]])
    
    b = np.array([[ 0.00 , 0.00 ],
                  [ 0.00 , 1.00 ],
                  [ 0.00 , 0.60 ],
                  [ 0.00 , 1.10 ],
                  [ 0.00 , 1.00 ],
                  [ 0.00 , 0.70 ]])
    
    next_transform = rv(name='Arbol',
             values=((0,1,2,3,4,5),(0.1,0.1,0.2,0.2,0.2,0.2)))

    return ChaosGame(A,b,next_transform)

def mk_caracoles():

    A = np.array([[[ 0.5  ,-0.2 ],[ 0.2 , 0.6 ]],
                  [[ 0.75 , 0.5 ],[-0.6 , 0.4 ]]])
    
    b = np.array([[-1.0 ,-2.0 ],
                  [-1.0 , 2.0 ]])
    
    next_transform = rv(name='Caracoles',
             values=((0,1),(0.42,0.58)))

    return ChaosGame(A,b,next_transform)

def mk_molinos():

    A = np.array([[[ 0.02     , 0.0      ],[ 0.0      , 0.5       ]],
                  [[ 0.02     , 0.0      ],[ 0.0      ,-0.5       ]],
                  [[ 0.5303307,-0.5303307],[ 0.5303307, 0.5303307 ]],
                  [[ 0.0      , 0.5      ],[-0.5      , 0.0       ]]])
    
    b = np.array([[ 0.0 , 0.0 ],
                  [ 0.0 , 0.5 ],
                  [ 0.0 , 1.0 ],
                  [ 0.0 , 1.2 ]])
    
    next_transform = rv(name='Molinos',
             values=((0,1,2,3),(0.145,0.145,0.426,0.284)))

    return ChaosGame(A,b,next_transform)

def mk_vicsek():

    A = np.array([[[ 0.333333, 0.0 ],[ 0.0 , 0.333333 ]],
                  [[ 0.333333, 0.0 ],[ 0.0 , 0.333333 ]],
                  [[ 0.333333, 0.0 ],[ 0.0 , 0.333333 ]],
                  [[ 0.333333, 0.0 ],[ 0.0 , 0.333333 ]],
                  [[ 0.333333, 0.0 ],[ 0.0 , 0.333333 ]]])
    
    b = np.array([[ 0.0 , 0.0 ],
                  [ 2.0 , 0.0 ],
                  [ 1.0 , 1.0 ],
                  [ 0.0 , 2.0 ],
                  [ 2.0 , 2.0 ]])
    
    next_transform = rv(name='Vicsek',
             values=((0,1,2,3,4),(0.2,0.2,0.2,0.2,0.2)))

    return ChaosGame(A,b,next_transform)

def mk_cristales():

    A = np.array([[[ 0.5 , 0.0 ],[ 0.0 ,-0.5 ]],
                  [[ 0.5 , 0.0 ],[ 0.0 ,-0.5 ]],
                  [[ 0.5 , 0.0 ],[ 0.0 ,-0.5 ]]])
    
    b = np.array([[ 0.0  , 0.0 ],
                  [ 0.5  , 0.0 ],
                  [ 0.25 , 0.5 ]])
    
    next_transform = rv(name='Cristales',
             values=((0,1,2),(0.333,0.333,0.334)))

    return ChaosGame(A,b,next_transform)

if __name__ in ("__main__","__plot__"):
    while True:
        print "Enter '1' to plot the Sierpinski Gasket."
        print "Enter '2' to plot the Barnsley Fern."
        print "Enter '3' to plot the von Koch Curve."
        print "Enter '4' to plot the Bronchi Curve."
        print "Enter '5' to plot the Helecho Fern."
        print "Enter '6' to plot the Hoja Leaf."
        print "Enter '7' to plot the Arbol."
        print "Enter '8' to plot the Caracoles."
        print "Enter '9' to plot the Molinos."
        print "Enter '10' to plot the Vicsek."
        print "Enter '11' to plot the Cristales."
        print "Enter '12' to plot the Koch variation."
        answer = raw_input('Enter selection: ')
        if answer == '1':
            sierpinski = mk_sierpinski()
            sierpinski.run()
            break
        elif answer == '2':
            fern = mk_fern()
            fern.run()
            break
        elif answer == '3':
            koch = mk_koch()
            koch.run()
            break
        elif answer == '4':
            bronchi = mk_bronchi()
            bronchi.run()
            break
        elif answer == '5':
            helecho = mk_helecho()
            helecho.run()
            break
        elif answer == '6':
            hoja = mk_hoja()
            hoja.run()
            break
        elif answer == '7':
            frac = mk_arbol()
            frac.run()
            break
        elif answer == '8':
            frac = mk_caracoles()
            frac.run()
            break
        elif answer == '9':
            frac = mk_molinos()
            frac.run()
            break
        elif answer == '10':
            frac = mk_vicsek()
            frac.run()
            break
        elif answer == '11':
            frac = mk_cristales()
            frac.run()
            break
        elif answer == '12':
            frac = mk_koch1()
            frac.run()
            break
        else:
            print "Please select '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', or '11'."
