from PySide6.QtCore import Signal
from PySide6.QtWidgets import QAbstractButton, QPushButton, QWidget

from pydarts.core import models
from pydarts.widgets.ui.game_widget import Ui_game_widget


class GameWidget(QWidget, Ui_game_widget):
    finished = Signal(models.BaseGame, arguments=["game"])

    def __init__(self, parent: QWidget, game: models.BaseGame) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self._load_event_handling()
        self.game = game
        self._activate_next_player()
        return None

    def _load_event_handling(self) -> None:
        self.input_single_radio_button.released.connect(self._draw_darts_widget)
        self.input_double_radio_button.released.connect(self._draw_darts_widget)
        self.input_triple_radio_button.released.connect(self._draw_darts_widget)
        self.input_miss_push_button.released.connect(lambda: self._register_throw(self.input_miss_push_button))
        self.input_1_push_button.released.connect(lambda: self._register_throw(self.input_1_push_button))
        self.input_2_push_button.released.connect(lambda: self._register_throw(self.input_2_push_button))
        self.input_3_push_button.released.connect(lambda: self._register_throw(self.input_3_push_button))
        self.input_4_push_button.released.connect(lambda: self._register_throw(self.input_4_push_button))
        self.input_5_push_button.released.connect(lambda: self._register_throw(self.input_5_push_button))
        self.input_6_push_button.released.connect(lambda: self._register_throw(self.input_6_push_button))
        self.input_7_push_button.released.connect(lambda: self._register_throw(self.input_7_push_button))
        self.input_8_push_button.released.connect(lambda: self._register_throw(self.input_8_push_button))
        self.input_9_push_button.released.connect(lambda: self._register_throw(self.input_9_push_button))
        self.input_10_push_button.released.connect(lambda: self._register_throw(self.input_10_push_button))
        self.input_11_push_button.released.connect(lambda: self._register_throw(self.input_11_push_button))
        self.input_12_push_button.released.connect(lambda: self._register_throw(self.input_12_push_button))
        self.input_13_push_button.released.connect(lambda: self._register_throw(self.input_13_push_button))
        self.input_14_push_button.released.connect(lambda: self._register_throw(self.input_14_push_button))
        self.input_15_push_button.released.connect(lambda: self._register_throw(self.input_15_push_button))
        self.input_16_push_button.released.connect(lambda: self._register_throw(self.input_16_push_button))
        self.input_17_push_button.released.connect(lambda: self._register_throw(self.input_17_push_button))
        self.input_18_push_button.released.connect(lambda: self._register_throw(self.input_18_push_button))
        self.input_19_push_button.released.connect(lambda: self._register_throw(self.input_19_push_button))
        self.input_20_push_button.released.connect(lambda: self._register_throw(self.input_20_push_button))
        self.input_25_push_button.released.connect(lambda: self._register_throw(self.input_25_push_button))
        self.next_turn_push_button.released.connect(self._continue_to_next_turn)
        self.finish_game_push_button.released.connect(self._end_game)
        return None

    def _draw_darts_widget(self) -> None:
        self.input_25_push_button.setDisabled(self.input_triple_radio_button.isChecked())
        return None

    def _draw(self) -> None:
        self._draw_darts_widget()
        current_player = self.game.get_active_player()
        self.turn_order_value_label.setText("\n".join(
            f"{index+1}. {player.name} ({player.score})"
            for index, player in enumerate(self.game.players)
        ))
        index = self.game.players.index(current_player)
        self.current_player_value_label.setText(f"{current_player.name} ({current_player.score})")
        for index, line_edit in enumerate([self.throw_1_line_edit, self.throw_2_line_edit, self.throw_3_line_edit]):
            try:
                throw = current_player.history[-1][index]
            except IndexError:
                line_edit.setText("")
            else:
                line_edit.setText(throw.value)
        for child in self.darts_widget.findChildren(QAbstractButton):
            child.setEnabled(not current_player.is_turn_over and not self.game.is_over)
        self.next_turn_push_button.setEnabled(current_player.is_turn_over and not self.game.is_over)
        if self.game.is_over:
            self.finish_game_push_button.setFocus()
        else:
            self.next_turn_push_button.setFocus()
        return None

    def _activate_next_player(self) -> None:
        self.game.activate_next_player()
        self._draw()
        return None

    def _register_throw(self, widget: QPushButton) -> None:
        if widget is self.input_miss_push_button:
            value = "0"
        elif self.input_single_radio_button.isChecked():
            value = widget.text()
        elif self.input_double_radio_button.isChecked():
            value = f"D{widget.text()}"
            self.input_single_radio_button.setChecked(True)
        elif self.input_triple_radio_button.isChecked():
            value = f"T{widget.text()}"
            self.input_single_radio_button.setChecked(True)
        throw = models.Throw(value)
        try:
            self.game.register_throw(throw)
        except models.ValueLimitExceededError:
            self.hint_label.setText("Too much! Try again next round.\n\nPress 'Next' to activate next player.")
            self._draw()
            return None
        if self.game.is_over:
            self.hint_label.setText("You won, congratulations!\n\nPress 'Finish' to end game.")
        elif self.game.get_active_player().is_turn_over:
            self.hint_label.setText("Press 'Next' to activate next player.")
        self._draw()
        return None

    def _continue_to_next_turn(self) -> None:
        self.hint_label.setText("")
        current_player = self.game.get_active_player()
        current_turn = current_player.history[-1]
        for _ in range(len(current_turn), 3):
            current_turn.append(models.Throw("0"))
        self._activate_next_player()
        return None

    def _end_game(self) -> None:
        self.finished.emit(self.game)
        return None
