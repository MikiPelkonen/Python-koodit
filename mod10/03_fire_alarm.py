def clamp(value, min_value, max_value):
    """Clamp a value between `min_value` and `max_value`."""
    return max(min_value, min(value, max_value))


class Elevator:
    def __init__(self, bottom_floor: int, top_floor: int) -> None:
        self.bottom_floor: int = bottom_floor
        self.top_floor: int = top_floor
        self.current_floor: int = bottom_floor

    def go_to_floor(self, target_floor: int) -> None:
        while self.current_floor != target_floor:
            if self.current_floor < target_floor:
                self.floor_up()
            else:
                self.floor_down()
            print(f"Current floor: {self.current_floor}")

    def floor_up(self) -> None:
        next_floor = self.current_floor + 1
        clamped_floor = clamp(next_floor, self.bottom_floor, self.top_floor)
        self.current_floor = clamped_floor

    def floor_down(self) -> None:
        next_floor = self.current_floor - 1
        clamped_floor = clamp(next_floor, self.bottom_floor, self.top_floor)
        self.current_floor = clamped_floor


class Building:
    def __init__(self, bottom_floor: int, top_floor: int, elevator_count: int) -> None:
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators: list[Elevator] = [
            Elevator(bottom_floor, top_floor) for _ in range(elevator_count)
        ]

    def run_elevator(self, elevator_index: int, target_floor: int) -> None:
        self.elevators[elevator_index].go_to_floor(target_floor)

    def fire_alarm(self) -> None:
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom_floor)


building = Building(1, 10, 3)
