from typing import Optional

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QMainWindow, QWidget

from pydarts.core import models
from pydarts.widgets.game_widget import GameWidget
from pydarts.widgets.post_game_widget import PostGameWidget
from pydarts.widgets.pre_game_tab_widget import PreGameTabWidget
from pydarts.widgets.ui.main_window import Ui_main_window


class MainWindow(QMainWindow, Ui_main_window):
    finished_exit = Signal()

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.pre_game_widget: PreGameTabWidget
        self.game_widget: GameWidget
        self.post_game_widget: PostGameWidget
        self._load_pre_game_widget()
        return None

    def _load_widget(self, widget: QWidget) -> None:
        self.stacked_widget.hide()
        if (current_widget := self.stacked_widget.currentWidget()) is not None:
            self.stacked_widget.removeWidget(current_widget)
            current_widget.destroy()
        self.stacked_widget.addWidget(widget)
        self.setMinimumSize(widget.minimumSize())
        self.setMaximumSize(widget.maximumSize())
        self.setGeometry(widget.geometry())
        self.move(self.screen().geometry().center() - self.geometry().center())
        self.setWindowTitle(widget.windowTitle())
        self.stacked_widget.show()
        return None

    def _load_pre_game_widget(self, game: Optional[models.BaseGame] = None) -> None:
        if game is None:
            self.pre_game_widget = PreGameTabWidget(parent=self)
        else:
            mode_type = type(game)
            player_names = [player.name for player in game.players]
            self.pre_game_widget = PreGameTabWidget(self, mode_type, player_names)
        self._load_widget(self.pre_game_widget)
        self.pre_game_widget.finished.connect(lambda game: self._load_game_widget(game))
        self.show()
        return None

    def _load_game_widget(self, game: models.BaseGame) -> None:
        self.game_widget = GameWidget(self, game)
        self._load_widget(self.game_widget)
        self.game_widget.finished.connect(lambda game: self._load_post_game_widget(game))
        return None

    def _load_post_game_widget(self, game: models.BaseGame) -> None:
        self.post_game_widget = PostGameWidget(self, game)
        self._load_widget(self.post_game_widget)
        self.post_game_widget.finished_exit.connect(self.finished_exit.emit)
        self.post_game_widget.finished_play_again.connect(lambda game: self._load_pre_game_widget(game))
        return None
