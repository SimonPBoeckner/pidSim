from dataTypes import ControllerConstants, SetPoint
from controller import Controller

set_point = SetPoint(100)

controllers = [
    Controller(ControllerConstants(0.1, 0.008, 0.0000001), set_point, "line_1"),
    Controller(ControllerConstants(0.01, 0.09, 0), set_point, "line_2"),
    Controller(ControllerConstants(0.05, 0.04, 0), set_point, "line_3")
]