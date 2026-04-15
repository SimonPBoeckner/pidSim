from plotter import Plotter

import config

import time

plotter = Plotter(config.set_point)

dt = 0.0001
offset = time.time()

while True:
    start = time.perf_counter()

    for i in config.controllers:
        i.update(dt, time.time() - offset)
        plotter.update(i)

    end = time.perf_counter()
    dt = end - start
    if time.time() - offset > 30:
        plotter.save_plot()
        break