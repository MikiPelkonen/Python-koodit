def clamp(value, min_value, max_value):
    """Clamp a value between `min_value` and `max_value`."""
    return max(min_value, min(value, max_value))


class Car:
    def __init__(self, license_plate: str, maximum_speed: int) -> None:
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_delta: int) -> None:
        new_speed = self.current_speed + speed_delta
        clamped_speed = clamp(new_speed, 0, self.maximum_speed)
        self.current_speed = clamped_speed

    def drive(self, hours: float):
        drive_distance = self.current_speed * hours
        self.travelled_distance += drive_distance


class ElectricCar(Car):
    def __init__(
        self, license_plate: str, maximum_speed: int, battery_capacity: float
    ) -> None:
        super().__init__(license_plate, maximum_speed)
        self.battery_capacity = battery_capacity


class GasolineCar(Car):
    def __init__(
        self, license_plate: str, maximum_speed: int, tank_volume: float
    ) -> None:
        super().__init__(license_plate, maximum_speed)
        self.tank_volume = tank_volume
