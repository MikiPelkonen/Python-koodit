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
        result = f"{self.license_plate:6} {self.current_speed:<5} {self.maximum_speed:<3} {self.travelled_distance:<8}"
        return result

    def accelerate(self, speed_delta: int) -> None:
        new_speed = self.current_speed + speed_delta
        clamped_speed = clamp(new_speed, 0, self.maximum_speed)
        self.current_speed = clamped_speed

    def drive(self, hours: float):
        drive_distance = self.current_speed * hours
        self.travelled_distance += drive_distance


class Race:
    def __init__(self, name: str, distance: int, cars: list[Car]) -> None:
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self) -> None:
        for car in self.cars:
            car.accelerate(random.randint(-15, 15))
            car.drive(1)

    def print_status(self) -> None:
        header_str = f"ID. {'Driver':<6} {'Speed':<5} {'Max':<3} {'Distance':8}"
        print(header_str)
        print("-" * len(header_str))
        for idx, car in enumerate(self.cars):
            print(f"{idx + 1:2}. {car}")
        print()

    def race_finished(self) -> bool:
        for car in self.cars:
            if car.travelled_distance >= RACE_LIMIT_IN_KMS:
                return True
        return False


def race_results(cars: list[Car]) -> str:
    cars.sort(key=lambda car: car.travelled_distance, reverse=True)
    return "\n".join(
        f"{(idx + 1):3}. {car.license_plate:<6} {car.travelled_distance:<6} kms"
        for idx, car in enumerate(cars)
    )


RACE_NAME: str = "Grand Demolition Derby"
RACE_LIMIT_IN_KMS: int = 8000
CAR_COUNT: int = 10
CARS: list[Car] = [
    Car(f"ABC-{i + 1}", random.randint(100, 200)) for i in range(CAR_COUNT)
]

race = Race(RACE_NAME, RACE_LIMIT_IN_KMS, CARS)
while not race.race_finished():
    race.hour_passes()
    race.print_status()
print("---- RACE RESULTS ----")
print(race_results(CARS))
