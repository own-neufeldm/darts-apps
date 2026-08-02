from typing import Self


class IllegalThrowError(Exception):
    pass


class ValueLimitExceededError(IllegalThrowError):
    pass


class BaseGame():
    def __init__(self, players: list["Player"]) -> None:
        self.players = players
        self.is_over = False
        return None

    @classmethod
    def from_player_names(cls, player_names: list[str]) -> Self:
        players = [Player(player_name, cls.get_starting_score()) for player_name in player_names]
        return cls(players)

    @classmethod
    def from_game(cls, game: Self) -> Self:
        return cls.from_player_names([player.name for player in game.players])

    @classmethod
    def get_name(cls) -> str:
        raise NotImplementedError()

    @classmethod
    def get_description(cls) -> str:
        raise NotImplementedError()

    @classmethod
    def get_starting_score(cls) -> int:
        raise NotImplementedError()

    def get_active_player(self) -> "Player":
        for player in self.players:
            if player.active:
                return player
        raise ValueError("No player is active.")

    def activate_next_player(self) -> None:
        try:
            active_player = self.get_active_player()
        except ValueError:
            self.players[0].activate()
            return None
        index = self.players.index(active_player)
        if index == len(self.players) - 1:
            index = 0
        else:
            index += 1
        active_player.deactivate()
        self.players[index].activate()
        return None

    def register_throw(self, throw: "Throw") -> None:
        player = self.get_active_player()
        turn = player.history[-1]
        turn.append(throw)
        if player.score - int(throw) < 0:
            for _ in range(len(turn), 3):
                turn.append(Throw("0"))
            raise ValueLimitExceededError
        player.score -= int(throw)
        if player.score == 0:
            for _ in range(len(turn), 3):
                turn.append(Throw("0"))
            self.is_over = True
            return None
        return None


class Game301(BaseGame):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        return None

    @classmethod
    def get_name(cls) -> str:
        return "301"

    @classmethod
    def get_description(cls) -> str:
        return " ".join([
            "Reach zero from starting score 301 by subtracting the score achieved with each throw. Players take turns",
            "throwing three darts per round, aiming to hit the numbered sections on the dartboard. The scoring is",
            "based on the numerical value of the hit sections, with doubles and triples offering double and triple the",
            "respective value. The game ends when a player reaches exactly zero."
        ])

    @classmethod
    def get_starting_score(cls) -> int:
        return 301


class Game501(BaseGame):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        return None

    @classmethod
    def get_name(cls) -> str:
        return "501"

    @classmethod
    def get_description(cls) -> str:
        return " ".join([
            "Reach zero from starting score 501 by subtracting the score achieved with each throw. Players take turns",
            "throwing three darts per round, aiming to hit the numbered sections on the dartboard. The scoring is",
            "based on the numerical value of the hit sections, with doubles and triples offering double and triple the",
            "respective value. The game ends when a player reaches exactly zero."
        ])

    @classmethod
    def get_starting_score(cls) -> int:
        return 501


class Player():
    def __init__(self, name: str, score: int) -> None:
        self.name = name
        self.score = score
        self.history: list[list["Throw"]] = []
        self.active = False
        return None

    @property
    def is_turn_over(self) -> bool:
        return len(self.history[-1]) == 3

    def activate(self) -> None:
        self.active = True
        self.history.append([])
        return None

    def deactivate(self) -> None:
        self.active = False
        return None


class Throw():
    def __init__(self, value: str) -> None:
        self.value = value
        return None

    def __int__(self) -> int:
        if (rest := self.value.removeprefix("D")) != self.value:
            return 2 * int(rest)
        if (rest := self.value.removeprefix("T")) != self.value:
            return 3 * int(rest)
        return int(self.value)


def get_mode_types() -> list[type[BaseGame]]:
    return [Game301, Game501]


def get_mode_type_by_name(name: str) -> type[BaseGame]:
    for mode_type in get_mode_types():
        if mode_type.get_name() == name:
            return mode_type
    raise ValueError(f"No mode type named {name!r}.")
