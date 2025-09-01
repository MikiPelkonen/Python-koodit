from __future__ import annotations
from enum import Enum
from abc import ABC, abstractmethod
from datetime import datetime


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


class Player:
    def __init__(self, game_size: int, name: str, start_position: Coordinate) -> None:
        self.game_size = game_size
        self.name = name
        self.position = start_position

    def run(self, command: IPlayerCommand):
        command.run(self)

    def is_legal_move(self, coords: Coordinate) -> bool:
        legal: bool = (
            coords.x >= 0
            and coords.x <= self.game_size - 1
            and coords.y >= 0
            and coords.y <= self.game_size - 1
        )
        return legal

    def illegal_move(self):
        print("Illegal move! Try another direction!")


class IPlayerCommand(ABC):
    @abstractmethod
    def run(self, player: Player):
        return


class NorthCommand(IPlayerCommand):
    def run(self, player: Player):
        new_position = Coordinate(player.position.x, player.position.y - 1)
        if player.is_legal_move(new_position):
            player.position = new_position
        else:
            player.illegal_move()


class SouthCommand(IPlayerCommand):
    def run(self, player: Player):
        new_position = Coordinate(player.position.x, player.position.y + 1)
        if player.is_legal_move(new_position):
            player.position = new_position
        else:
            player.illegal_move()


class WestCommand(IPlayerCommand):
    def run(self, player: Player):
        new_position = Coordinate(player.position.x - 1, player.position.y)
        if player.is_legal_move(new_position):
            player.position = new_position
        else:
            player.illegal_move()


class EastCommand(IPlayerCommand):
    def run(self, player: Player):
        new_position = Coordinate(player.position.x + 1, player.position.y)
        if player.is_legal_move(new_position):
            player.position = new_position
        else:
            player.illegal_move()


class World:
    def __init__(self, rooms) -> None:
        self.rooms = rooms

    def get_room_type(self, coords: Coordinate) -> RoomType:
        return self.rooms[coords.x][coords.y].room_type


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

    def __repr__(self) -> str:
        return f"{self.room_type}({self.coords})"

    @property
    def get_room_type(self) -> RoomType:
        return self.room_type

    @property
    def get_coords(self) -> Coordinate:
        return self.coords


class Game:
    def __init__(self, world: World, player: Player) -> None:
        self.world = world
        self.player = player

    def run(self):
        clear_console()
        print("You stand at the castle gates.")
        print(
            "Cold wind sweeps across the courtyard, carrying the scent of dust and forgotten history.  "
        )
        press_enter()


def get_game_size() -> GameSize:
    while True:
        user_input = (
            input("Choose the size of the world (small, medium, large): ")
            .lower()
            .strip()
        )
        if user_input == "small":
            return GameSize.SMALL
        if user_input == "medium":
            return GameSize.MEDIUM
        if user_input == "large":
            return GameSize.LARGE

        print(f"Invalid option: {user_input}. Please try again.")


def game_life_time(start_time: datetime):
    end_time: datetime = datetime.now()
    time_span = end_time - start_time
    minutes = (time_span.seconds / 60).__floor__()
    seconds = time_span.seconds - (minutes * 60)
    print(f"The game was running for {minutes} minutes and {seconds} seconds.")


def clear_console():
    print("\033[H\033[J", end="")


def press_enter():
    input("Press enter to continue...")


# Main program.
start_time: datetime = datetime.now()
world_builder: WorldBuilder = WorldBuilder(get_game_size())
game: Game = Game(
    world_builder.build_world(),
    Player(world_builder.game_size.value, "mudsrulez", Coordinate(0, 0)),
)
game.run()
game_life_time(start_time)
