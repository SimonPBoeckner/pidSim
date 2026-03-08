from dataTypes import ControllerConstants, SetPoint
from controller import Controller

set_point = SetPoint(100)

controllers = [
    Controller(ControllerConstants(0.1, 0.005, 0), set_point, "line_1"),
    Controller(ControllerConstants(0.01, 0, 0), set_point, "line_2")
]