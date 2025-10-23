def clamp(value, min_value, max_value):
    """Clamp a value between `min_value` and `max_value`."""
    return max(min_value, min(value, max_value))


class Car:
    def __init__(self, license_plate: str, maximum_speed: int) -> None:
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def __repr__(self) -> str:
        result_list = [
            f"License plate: {self.license_plate}",
            f"Maximum speed: {self.maximum_speed} km/h",
            f"Current speed: {self.current_speed} km/h",
            f"Travelled distance: {self.travelled_distance} km",
        ]
        return "\n".join(result_list)

    def accelerate(self, speed_delta: int) -> None:
        new_speed = self.current_speed + speed_delta
        clamped_speed = clamp(new_speed, 0, self.maximum_speed)
        self.current_speed = clamped_speed

    def drive(self, hours: float):
        drive_distance = self.current_speed * hours
        self.travelled_distance += drive_distance


LICENSE_PLATE: str = "ABC-123"
MAXIMUM_SPEED: int = 142

car = Car(LICENSE_PLATE, MAXIMUM_SPEED)
print(car)
car.current_speed = 60
car.drive(1.5)
print(f"Distance after driving 1.5 hours at 60 km/h: {car.travelled_distance} km")
