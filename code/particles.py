import time
import numpy as np
import matplotlib.pyplot as plt
from pprint import pformat

class Particle:
    def __init__(self, x, y):
        self.pos = np.array([x, y])
        self.steps = 0
        
    def move(self):
        self.pos += np.random.normal(scale=0.02, size=2)
        
    def __str__(self):
        return "(" + "%6.3f" % self.pos[0] + ", %6.3f" % self.pos[1] + ")"
        
    def __repr__(self):
        return self.__str__()


class Particles:
    def __init__(self, n, plotstep=2):
        self.particles = sum(([Particle(0., 0.)] for i in range(n)), [])
        self.plotstep = plotstep
    
    def move(self):
        for p in self.particles:
            p.move()
            
    def plot(self):
        plt.cla()
        plt.axis([-1, 1, -1, 1])
        x = [p.pos[0] for p in self.particles]
        y = [p.pos[1] for p in self.particles]
        plt.plot(x, y, 'g.')
        plt.draw()
        plt.pause(0.01)
    
    def moves(self, n):
        plt.figure()
        self.plot()
        for i in range(n):
            self.move()
            if i % self.plotstep == 0:
                self.plot()
                
    def __str__(self):
        return pformat([p for p in self.particles])
    

if __name__ == '__main__':
    import sys
    n = int(sys.argv[1])
    ps = Particles(n)
    ps.moves(200)
