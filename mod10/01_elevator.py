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

    def floor_up(self):
        next_floor = self.current_floor + 1
        clamped_floor = clamp(next_floor, self.bottom_floor, self.top_floor)
        self.current_floor = clamped_floor

    def floor_down(self):
        next_floor = self.current_floor - 1
        clamped_floor = clamp(next_floor, self.bottom_floor, self.top_floor)
        self.current_floor = clamped_floor


h = Elevator(1, 10)
