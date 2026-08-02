from itertools import groupby

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget

from pydarts.core import models
from pydarts.widgets.ui.post_game_widget import Ui_post_game_widget


class PostGameWidget(QWidget, Ui_post_game_widget):
    finished_exit = Signal()
    finished_play_again = Signal(models.BaseGame, arguments=["game"])

    def __init__(self, parent: QWidget, game: models.BaseGame) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self._load_event_handling()
        self.game = game
        self._draw()
        return None

    def _load_event_handling(self) -> None:
        self.exit_game_push_button.released.connect(self.finished_exit.emit)
        self.play_again_push_button.released.connect(lambda: self.finished_play_again.emit(self.game))
        return None

    def _draw(self) -> None:
        leaderboard = groupby(sorted(self.game.players, key=lambda p: p.score), key=lambda p: p.score)
        self.leaderboard_label.setText("\n".join(
            f"{index+1}. {player.name} ({player.score})"
            for index, group in enumerate(leaderboard)
            for player in group[1]
        ))
        return None
