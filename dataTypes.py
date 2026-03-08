from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class ControllerConstants:
    kP: float
    kI: float
    kD: float

@dataclass(frozen=True)
class SetPoint:
    set_point: float

@dataclass
class Line:
    name: str
    x_points: List[float]
    y_points: List[float]