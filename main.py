from pidController import PIDController
from grapher import Grapher
from time import perf_counter

import matplotlib.pyplot as plt
import numpy as np

controller = PIDController(kP=0.5, setpoint=20)

# grapher = Grapher()

t = np.arange(0.0, 2.0, 0.01)
s = np.sin(2 * np.pi * t)
# fig = plt.figure() 
# ax = fig.add_subplot()
fig, ax = plt.subplots()

ax.plot(t, s)
ax.set(xlabel='time (s)', ylabel='voltage (mV)', title='About as simple as it gets, folks')

plt.grid()
plt.savefig('test.png')
plt.show(block=False)

# current_state = 0
# dt = 0

# while True:
#     start = perf_counter()
#     current_state += controller.update(current_state, dt)
#     end = perf_counter()
#     dt = end - start
#     print(current_state)
#     if current_state == 20:
#         break