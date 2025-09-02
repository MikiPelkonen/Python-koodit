# Work in progress...

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
class Colors(Enum):
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


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
        print(color_text(Colors.FAIL, "Illegal move! Try another direction!"))
        press_enter()


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
        # Create world grid and init every room as empty room
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
        # Place library
        rooms[length // 2][length // 2] = Room(
            RoomType.LIBRARY, Coordinate(length // 2, length // 2)
        )
        return World(rooms)


class Room:
    def __init__(self, room_type: RoomType, coords: Coordinate) -> None:
        self.room_type = room_type
        self.coords = coords

    def __repr__(self) -> str:
        return f"{self.room_type.name.capitalize()}({self.coords})"


class Game:
    def __init__(self, world: World, player: Player) -> None:
        self.world = world
        self.player = player
        self.game_over = False

    def display_room(self, room_type: RoomType):
        print(
            color_text(
                Colors.HEADER,
                f"You are in the room: {room_type.name.capitalize()} at coordinates: {self.player.position}",
            )
        )
        if room_type == RoomType.EMPTY:
            print(
                color_text(
                    Colors.ENDC,
                    "\nThe chamber is bare and cold.\nDust swirls in the stale air,\nand your footsteps echo against stone walls.",
                )
            )
        elif room_type == RoomType.ENTRANCE:
            print(
                color_text(
                    Colors.ENDC,
                    "\nA heavy wooden door creaks behind you.\nA faint draft of fresh air slips through the cracks,\ncarrying with it the scent of pine from outside.",
                )
            )
        elif room_type == RoomType.LIBRARY:
            print(
                color_text(
                    Colors.ENDC,
                    "\nTowering shelves groan under the weight of ancient tomes.\nThe scent of parchment and candlewax lingers,\nand faint whispers seem to dance between the books.",
                )
            )
        elif room_type == RoomType.KITCHEN:
            print(
                color_text(
                    Colors.ENDC,
                    "\nThe long-abandoned kitchen is littered with tarnished pots and cracked plates.\nA lingering smell of herbs and ashes clings to the hearth.",
                )
            )

    def run(self):
        clear_console()
        print(color_text(Colors.HEADER, "You stand at the castle gates."))
        print(
            color_text(
                Colors.OKGREEN,
                "Cold wind sweeps across the courtyard,\ncarrying the scent of dust and forgotten history.  ",
            )
        )
        press_enter()
        # Game loop
        while not self.game_over:
            clear_console()
            room_type = self.world.get_room_type(self.player.position)
            self.display_room(room_type)
            command_str = player_input_prompt(
                self.player.name, "\nWhat do you want to do? "
            )
            command = {
                "move north": NorthCommand(),
                "move south": SouthCommand(),
                "move east": EastCommand(),
                "move west": WestCommand(),
            }.get(command_str)

            if command_str == "exit":
                break

            if command is None:
                self.invalid_command(command_str)
            else:
                self.player.run(command)

    def invalid_command(self, command: str):
        clear_console()
        print(color_text(Colors.FAIL, f"INVALID COMMAND: {command}\n"))
        print(color_text(Colors.OKGREEN, "Valid commands:"))
        print(
            color_text(Colors.WARNING, "move north, move south, move west, move east")
        )
        press_enter()


# Functions.
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

        print(
            color_text(Colors.FAIL, f"Invalid option: {user_input}. Please try again.")
        )


def get_game_life_time(start_time: datetime, player_info: str):
    end_time: datetime = datetime.now()
    time_span = end_time - start_time
    minutes = (time_span.seconds / 60).__floor__()
    seconds = time_span.seconds - (minutes * 60)
    clear_console()
    print(f"The game was running for {minutes} minutes and {seconds} seconds.")
    print(
        f"Thank you {player_info} for playing!\n{color_text(Colors.OKBLUE, '- smol indie dev')}"
    )


def get_player_info() -> str:
    result = input("Tell me, traveler, by what name are you known in these lands? ")
    return result.capitalize()


def color_text(color: Colors, input_str: str) -> str:
    return f"{color.value}{input_str}{Colors.ENDC.value}"


def player_input_prompt(player_info: str, prompt_str: str):
    print(prompt_str)
    return input(color_text(Colors.OKCYAN, f"[{player_info}]: "))


def clear_console():
    print("\033[H\033[J", end="")


def press_enter(message: str = "\nPress enter to continue..."):
    input(color_text(Colors.OKCYAN, message))


# Main program.
start_time: datetime = datetime.now()
world_builder: WorldBuilder = WorldBuilder(get_game_size())
player_info = get_player_info()
game: Game = Game(
    world_builder.build_world(),
    Player(world_builder.game_size.value, player_info, Coordinate(0, 0)),
)
game.run()
get_game_life_time(start_time, player_info)
