import random


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


RACE_LIMIT_IN_KMS: int = 10000
CAR_COUNT: int = 10
CARS: list[Car] = [
    Car(f"ABC-{i + 1}", random.randint(100, 200)) for i in range(CAR_COUNT)
]


def race(cars: list[Car]) -> list[Car]:
    race_finished: bool = False
    while not race_finished:
        for car in cars:
            car.accelerate(random.randint(-15, 15))
            car.drive(1)
            if car.travelled_distance >= RACE_LIMIT_IN_KMS:
                race_finished = True
                break
    return cars


def race_results(cars: list[Car]) -> str:
    cars.sort(key=lambda car: car.travelled_distance, reverse=True)
    return "\n".join(
        f"{(idx + 1):3}. {car.license_plate:<6} {car.travelled_distance:6} kms"
        for idx, car in enumerate(cars)
    )


finished_cars = race(CARS)
print(race_results(finished_cars))
