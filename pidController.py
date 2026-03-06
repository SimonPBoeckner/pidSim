class PIDController():
    def __init__(self, kP: float = 0, kI: float = 0, kD: float = 0, setpoint: float = None) -> None:
        self.kP = kP
        self.kI = kI
        self.kD = kD
        self.setpoint = setpoint
        self.last_error = 0
        self.integral_sum = 0

    def update(self, measurement: float, dt: float) -> float:
        error = self.setpoint - measurement
        self.integral_sum += error * dt
        derivative = (error - self.last_error) * dt
        self.last_error = error
        return self.kP * error + self.kI * self.integral_sum + self.kD * derivative