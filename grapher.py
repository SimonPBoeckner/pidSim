import matplotlib.pyplot as plt
import numpy as np

from typing import List

class Grapher():
    def __init__(self) -> None:
        self.x_points: List = []
        self.y_points: List = []

        self.fig = plt.figure() 
        self.ax = self.fig.add_subplot()

        t = np.arange(0.0, 2.0, 0.01)
        s = np.sin(2 * np.pi * t)
        self.ax.plot(t, s)
        self.ax.set(xlabel='time (s)', ylabel='voltage (mV)', title='About as simple as it gets, folks')

        plt.grid()
        plt.show(block=False)

    def update(self, x: float, y: float) -> None:
        self.x_points.append(x)
        self.y_points.append(y)

        self.ax.clear()
        self.ax.plot(self.x_points, self.y_points)