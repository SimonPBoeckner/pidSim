from dataTypes import SetPoint
from controller import Controller

import matplotlib.pyplot as plt

class Plotter():
    def __init__(self, set_point: SetPoint):
        self.set_point = set_point.set_point
        self.line_cache = {}

        self.fig, self.ax = plt.subplots()
        self.ax.set(
            xlabel='time (seconds)',
            ylabel='system state (unitless)',
            title='PID Response Simulation Graph'
        )
        self.ax.axhline(
            y=self.set_point,
            color='black',
            linestyle='--'
        )
        plt.grid()
        plt.ion()

    def update(self, controller: Controller):
        if len(self.line_cache.keys()) == 0:
            new_item = {controller.path.name: controller.path}
            self.line_cache.update(new_item)

        for i in list(self.line_cache.keys()):
            if controller.path.name == i:
                self.line_cache[i] = controller.path
            else:
                new_item = {controller.path.name: controller.path}
                self.line_cache.update(new_item)

        self.ax.clear()

        self.ax.set(
            xlabel='time (seconds)',
            ylabel='system state (unitless)',
            title='PID Response Simulation Graph'
        )
        self.ax.axhline(
            y=self.set_point,
            color='black',
            linestyle='--'
        )
        plt.grid()
        for j in self.line_cache.values():
            self.ax.plot(j.x_points, j.y_points)
            # plt.annotate(
            #     f'kP: {controller.kP}, kI: {controller.kI}, kD: {controller.kD}', 
            #     (controller.path.x_points[int(len(controller.path.x_points)/2)], 
            #     controller.path.y_points[int(len(controller.path.y_points)/2)]),
            #     textcoords="offset points",
            #     xytext=(0, -15),
            #     ha='center'
            # )
        plt.pause(0.001)

    def start(self) -> None:
        plt.show()

    def save_plot(self) -> None:
        plt.savefig("plot.png")
