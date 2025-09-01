from enum import Enum


# Enums.
class GameSize(Enum):
    SMALL = 4
    MEDIUM = 6
    LARGE = 8


class RoomType(Enum):
    EMPTY = 0
    ENTRANCE = 1
    LIBRARY = 2
    KITCHEN = 3


# Classes.
class Coordinate:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"X: {self.x} Y: {self.y}"

    @property
    def get_x(self) -> int:
        return self.x

    @property
    def get_y(self) -> int:
        return self.y


class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.level = 1


class World:
    def __init__(self, rooms) -> None:
        self.rooms = rooms

    def get_room_type(self, coords: Coordinate) -> RoomType:
        return self.rooms[coords.get_x][coords.get_y].room_type


class WorldBuilder:
    def __init__(self, size: GameSize) -> None:
        self.game_size = size

    def build_world(self) -> World:
        length = self.game_size.value
        rooms = [
            [Room(RoomType.EMPTY, Coordinate(row, col)) for col in range(length)]
            for row in range(length)
        ]
        # Place entrance
        rooms[0][0] = Room(RoomType.ENTRANCE, Coordinate(0, 0))
        # Place kitchen
        rooms[length // 2][length - 1] = Room(
            RoomType.KITCHEN, Coordinate(length // 2, length - 1)
        )
        return World(rooms)


class Room:
    def __init__(self, room_type: RoomType, coords: Coordinate) -> None:
        self.room_type = room_type
        self.coords = coords

    @property
    def get_room_type(self) -> RoomType:
        return self.room_type

    @property
    def get_coords(self) -> Coordinate:
        return self.coords

    def __repr__(self) -> str:
        return f"{self.room_type}({self.coords})"


# Main program.
world_builder = WorldBuilder(GameSize.SMALL)
world = world_builder.build_world()
for x in world.rooms:
    print(x)

print(world.get_room_type(Coordinate(0, 0)))
