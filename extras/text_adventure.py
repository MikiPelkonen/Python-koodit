# Work in progress...
"""
!!! Dont overextend the scope anymore...!!!

TODOS:
- Quest completion logic
- Item/Quest item logic
- Game progression/Quest progression phase logic
- Game end logic
- Proper credits
"""

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
    # cancel SGR codes if we don't write to a terminal
    if not __import__("sys").stdout.isatty():
        for _ in dir():
            if isinstance(_, str) and _[0] != "_":
                locals()[_] = ""
    else:
        # set Windows console in VT mode
        if __import__("platform").system() == "Windows":
            kernel32 = __import__("ctypes").windll.kernel32
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
            del kernel32


# Classes.
class Coordinate:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"X: {self.x} Y: {self.y}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Coordinate):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))


class Player:
    def __init__(self, game_size: int, name: str, start_position: Coordinate) -> None:
        self.game_size = game_size
        self.name = name
        self.position = start_position
        self.quest_log = QuestLog()
        self.inventory = Inventory()
        self.target = None

    def run(self, command: IPlayerCommand):
        command.run(self)

    def set_target_npc(self, character: Character):
        self.target = character

    def clear_target_npc(self):
        self.target = None

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


class Item:
    def __init__(self, name: str, desc: str) -> None:
        self.name = name
        self.description = desc


class Inventory:
    def __init__(self) -> None:
        self.items = list[Item]()

    def item_count(self) -> int:
        return len(self.items)

    def add_item(self, item: Item):
        if item not in self.items:
            self.items.append(item)

    def delete_item(self, item: Item):
        self.items.remove(item)

    def has_item(self, name: str) -> bool:
        for item in self.items:
            if item.name == name:
                return True
        return False

    def __repr__(self) -> str:
        item_list = ""
        for item in self.items:
            item_list += f"{item.name} - {item.description}\n"
        return item_list


class Quest:
    def __init__(
        self, name: str, desccription: str, target: Character, item: str
    ) -> None:
        self.name = name
        self.target = target
        self.description = desccription
        self.item = item
        self.completed = False

    def __repr__(self) -> str:
        return f"{self.name}\n{self.description}\ncompleted: [{'x' if self.completed else ' '}]\n"

    def try_complete(self, character: Character, player: Player):
        if self.target == character:
            if player.inventory.has_item(self.item):
                self.completed = True
                print(color_text(Colors.OKGREEN, f"Quest: {self.name} completed!"))


class QuestLog:
    def __init__(self) -> None:
        self.quests = []

    def quest_count(self) -> int:
        return len(self.quests)

    def get_quests(self) -> list[Quest]:
        return self.quests

    def add_quest(self, quest: Quest):
        if quest not in self.quests:
            self.quests.append(quest)
            print(color_text(Colors.WARNING, f"Quest: {quest.name} accepted!"))

    def complete_quest(self, quest: Quest, target: Character, player: Player):
        quest.try_complete(target, player)


# Player commands.
class IPlayerCommand(ABC):
    @abstractmethod
    def run(self, player: Player):
        raise NotImplementedError


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


class InteractCommand(IPlayerCommand):
    def run(self, player: Player):
        if player.target is not None:
            player.target.dialogue(player)
        else:
            clear_console()
            print("There is no-one to talk to...")
            press_enter()


class HelpCommand(IPlayerCommand):
    def run(self, player: Player):
        clear_console()
        print(f"Player: {player.name}")
        print(color_text(Colors.OKGREEN, "[COMMANDS]"))
        print(color_text(Colors.HEADER, "Move: "))
        print("north, south, west, east")
        print("")
        print(color_text(Colors.HEADER, "Interact: "))
        print("talk")
        print("")
        print(color_text(Colors.HEADER, "User interface: "))
        print("quests, inventory")
        print("")
        print(color_text(Colors.WARNING, "Exit game: "))
        print("exit")
        print("")
        press_enter()


class ToggleQuestlog(IPlayerCommand):
    def run(self, player: Player):
        clear_console()
        if player.quest_log.quest_count() <= 0:
            print("Your quest log is empty...")
        else:
            for idx, q in enumerate(player.quest_log.get_quests()):
                print(f"{idx + 1}. {q}")
        press_enter()


class ToggleInventory(IPlayerCommand):
    def run(self, player: Player):
        clear_console()
        if player.inventory.item_count() <= 0:
            print("Your inventory is empty...")
        else:
            print(player.inventory)
        press_enter()


# Character classes.
class Character(ABC):
    def __init__(self, name: str, start_position: Coordinate) -> None:
        self.name: str = name
        self.position: Coordinate = start_position
        self.quest: Quest

    @abstractmethod
    def dialogue(self, player: Player):
        pass


class Wizard(Character):
    def __init__(self, name: str, start_position: Coordinate, target) -> None:
        super().__init__(name, start_position)
        tutorial_quest = Quest(
            "The Codex Obscura",
            "Navigate to library and ask for the codex.",
            target,
            "codexobscura",
        )
        self.quest = tutorial_quest

    def dialogue(self, player: Player):
        clear_console()
        print(
            color_text(Colors.OKBLUE, f"[{self.name}]:"),
            f"\nHush now, apprentice {player.name}...\nA tome of great importance lies hidden in the library—\n~ The Codex Obscura. ~\nThe Librarian guards it jealously, but you must persuade them to let you borrow it.\nBring me this book, and I shall reveal secrets of power that even the stones dare not whisper.",
        )
        player.quest_log.add_quest(self.quest)
        press_enter()


class Librarian(Character):
    def __init__(self, name: str, start_position: Coordinate, target) -> None:
        super().__init__(name, start_position)
        coffee_quest = Quest(
            "Cup of joe", "Navigate to kitchen and ask for a coffee.", target, "coffee"
        )
        self.quest = coffee_quest
        self.quest_item = Item("The Codex Obscura", "The codex of blaablaa...")

    def dialogue(self, player: Player):
        clear_console()
        print(
            color_text(Colors.OKBLUE, f"[{self.name}]:"),
            f"\nShhh {player.name}… the books are sleeping.\nYou may not take anything without permission.\nAh, you seek 'The Codex Obscura', do you?\nThe Wizard at the entrance desires it, but I cannot simply hand it over.\nProve your worth, and perhaps I shall consider your request.",
        )
        player.quest_log.add_quest(self.quest)
        press_enter()


class Chef(Character):
    def __init__(self, name: str, start_position: Coordinate) -> None:
        super().__init__(name, start_position)
        self.quest_item = Item("Coffee", "Black as midnight on a moonless night.")

    def dialogue(self, player: Player):
        clear_console()
        print(
            color_text(Colors.OKBLUE, f"[{self.name}]:"),
            f"\nThe chef looks up from his cutting board with a warm smile, {player.name.upper()}, wiping his hands on his apron.\nAh, you want a coffee, eh? No problem, friend. Strong and hot, just the way I like it myself. Give me a moment...",
        )
        player.inventory.add_item(self.quest_item)
        press_enter()


# World entities.
class World:
    def __init__(self, rooms) -> None:
        self.rooms = rooms
        chef = Chef("Gordan Remsay", Coordinate(0, 0))
        librarian = Librarian("Archivist Morwenna", Coordinate(0, 0), chef)
        self.characters = {
            "Wizard": Wizard(
                "Merlin Longbeard",
                Coordinate(0, 0),
                librarian,
            ),
            "Librarian": librarian,
            "Chef": chef,
        }
        for row in self.rooms:
            for room in row:
                if room.room_type == RoomType.LIBRARY:
                    self.characters["Librarian"].position = room.coords
                if room.room_type == RoomType.ENTRANCE:
                    self.characters["Wizard"].position = room.coords
                if room.room_type == RoomType.KITCHEN:
                    self.characters["Chef"].position = room.coords

    def get_characters_by_room_position(self, coords: Coordinate) -> list[Character]:
        character_list: list[Character] = []
        for character in self.characters.values():
            if character.position == coords:
                character_list.append(character)
        return character_list

    def get_room_by_position(self, coords: Coordinate) -> Room:
        return self.rooms[coords.x][coords.y]


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
        self.room_type: RoomType = room_type
        self.coords: Coordinate = coords

    def __repr__(self) -> str:
        return f"{self.room_type.name.capitalize()}({self.coords})"


class Game:
    def __init__(self, world: World, player: Player) -> None:
        self.world = world
        self.player = player
        self.game_over = False
        self.start_time = datetime.now()

    def display_room(self, room: Room):
        print(
            color_text(
                Colors.HEADER,
                f"You are in the room: {room.room_type.name.capitalize()} at coordinates: {self.player.position}",
            )
        )
        if room.room_type == RoomType.EMPTY:
            print(
                color_text(
                    Colors.ENDC,
                    "\nThe chamber is bare and cold.\nDust swirls in the stale air,\nand your footsteps echo against stone walls.",
                )
            )
        elif room.room_type == RoomType.ENTRANCE:
            print(
                color_text(
                    Colors.ENDC,
                    "\nA heavy wooden door creaks behind you.\nA faint draft of fresh air slips through the cracks,\ncarrying with it the scent of pine from outside.",
                )
            )
        elif room.room_type == RoomType.LIBRARY:
            print(
                color_text(
                    Colors.ENDC,
                    "\nTowering shelves groan under the weight of ancient tomes.\nThe scent of parchment and candlewax lingers,\nand faint whispers seem to dance between the books.",
                )
            )
        elif room.room_type == RoomType.KITCHEN:
            print(
                color_text(
                    Colors.ENDC,
                    "\nThe long-abandoned kitchen is littered with tarnished pots and cracked plates.\nA lingering smell of herbs and ashes clings to the hearth.",
                )
            )

        for character in self.world.characters.values():
            if room.coords == character.position:
                print(
                    color_text(
                        Colors.WARNING,
                        f"There is a {character.__class__.__name__} in the room.\nType 'talk' to start dialogue with {character.name}.",
                    )
                )
                self.player.target = character

    def run(self):
        clear_console()
        print(color_text(Colors.HEADER, "You stand at the castle gates."))
        print(
            "Cold wind sweeps across the courtyard,\ncarrying the scent of dust and forgotten history.  ",
        )
        press_enter()
        # Game loop
        while not self.game_over:
            clear_console()
            self.player.clear_target_npc()
            room = self.world.get_room_by_position(self.player.position)
            self.display_room(room)

            command_str = player_input_prompt(
                self.player.name, "\nWhat do you want to do? "
            )

            if command_str == "exit":
                break

            command = {
                "north": NorthCommand(),
                "south": SouthCommand(),
                "east": EastCommand(),
                "west": WestCommand(),
                "talk": InteractCommand(),
                "quests": ToggleQuestlog(),
                "inventory": ToggleInventory(),
                "help": HelpCommand(),
            }.get(command_str)

            if command is None:
                self.invalid_command(command_str)
            else:
                self.player.run(command)

    def invalid_command(self, command: str):
        clear_console()
        print(color_text(Colors.FAIL, f"INVALID COMMAND: {command}\n"))
        print("type help for list of commands...")
        press_enter()


# Functions. (Global/Main level helpers)
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
        f"Thank you {color_text(Colors.OKCYAN, player_info)} for playing!\n{color_text(Colors.OKBLUE, '- smol indie dev')}"
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
world_builder: WorldBuilder = WorldBuilder(get_game_size())
player_info = get_player_info()
game: Game = Game(
    world_builder.build_world(),
    Player(world_builder.game_size.value, player_info, Coordinate(0, 0)),
)
game.run()
get_game_life_time(game.start_time, player_info)
