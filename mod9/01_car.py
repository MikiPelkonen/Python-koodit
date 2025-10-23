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


LICENSE_PLATE: str = "ABC-123"
MAXIMUM_SPEED: int = 142

car = Car(LICENSE_PLATE, MAXIMUM_SPEED)
print(car)
