from dataTypes import ControllerConstants, SetPoint, Line

class Controller():
    def __init__(self, pid_constants: ControllerConstants, set_point: SetPoint, name: str) -> None:
        self.kP: float = pid_constants.kP
        self.kI: float = pid_constants.kI
        self.kD: float = pid_constants.kD

        self.set_point: float = set_point.set_point
        self.current_state: float = 0

        self.last_error: float = 0
        self.integral_sum: float = 0

        self.path = Line(name, [0], [0])

    def update(self, dt: float, time: float) -> None:
        error: float = self.set_point - self.current_state
        self.integral_sum += error * dt
        derivative: float = (error - self.last_error) / dt
        self.last_error: float = error
        self.current_state += (self.kP * error) + (self.kI * self.integral_sum) + (self.kD * derivative)

        self.path.x_points.append(time)
        self.path.y_points.append(self.current_state)

    def get_line(self) -> Line:
        return self.path