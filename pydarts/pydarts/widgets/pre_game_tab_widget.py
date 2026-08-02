from typing import Optional

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QTabWidget, QWidget

from pydarts.core import models
from pydarts.widgets.ui.pre_game_tab_widget import Ui_pre_game_tab_widget


class PreGameTabWidget(QTabWidget, Ui_pre_game_tab_widget):
    finished = Signal(models.BaseGame, arguments=["game"])

    def __init__(
        self,
        parent: QWidget,
        mode_type: Optional[type[models.BaseGame]] = None,
        player_names: Optional[list[str]] = None
    ) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self._load_event_handling()
        self.mode_type = models.Game301 if mode_type is None else mode_type
        self.player_names = [] if player_names is None else player_names
        self._draw()
        return None

    def _load_event_handling_players_widget(self) -> None:
        self.input_line_edit.returnPressed.connect(self.add_push_button.released.emit)
        self.add_push_button.released.connect(self._add_player)
        self.overview_list_widget.currentItemChanged.connect(self._draw_player_edit_widget)
        self.remove_push_button.released.connect(self._remove_player)
        self.move_up_push_button.released.connect(self._move_player_up)
        self.move_down_push_button.released.connect(self._move_player_down)
        self.players_previous_page_push_button.released.connect(lambda: self.setCurrentIndex(self.currentIndex()-1))
        self.start_game_push_button.released.connect(self._start_game)
        return None

    def _load_event_handling_game_mode_wideget(self) -> None:
        self.selection_combo_box.textActivated.connect(self._select_mode_type)
        self.game_mode_next_page_push_button.released.connect(lambda: self.setCurrentIndex(self.currentIndex()+1))
        return None

    def _load_event_handling(self) -> None:
        self._load_event_handling_game_mode_wideget()
        self._load_event_handling_players_widget()
        return None

    def _draw_player_edit_widget(self) -> None:
        if self.overview_list_widget.currentItem() is None:
            self.remove_push_button.setDisabled(True)
            self.move_up_push_button.setDisabled(True)
            self.move_down_push_button.setDisabled(True)
            return None
        self.remove_push_button.setEnabled(True)
        if self.overview_list_widget.currentRow() != 0:
            self.move_up_push_button.setEnabled(True)
        if self.overview_list_widget.currentRow() != len(self.player_names) - 1:
            self.move_down_push_button.setEnabled(True)
        return None

    def _draw_start_game_widget(self) -> None:
        if not self.player_names:
            self.start_game_push_button.setDisabled(True)
            return None
        self.start_game_push_button.setEnabled(True)
        return None

    def _draw_players_widget(self) -> None:
        if len(self.player_names) == 8:
            self.input_line_edit.setReadOnly(True)
            self.add_push_button.setDisabled(True)
        else:
            self.input_line_edit.setReadOnly(False)
            self.add_push_button.setDisabled(False)
        self.overview_list_widget.clear()
        self.overview_list_widget.addItems(self.player_names)
        self._draw_player_edit_widget()
        self._draw_start_game_widget()
        return None

    def _draw_game_mode_widget(self) -> None:
        self.selection_combo_box.clear()
        self.selection_combo_box.addItems([mode_type.get_name() for mode_type in models.get_mode_types()])
        self.selection_combo_box.setCurrentText(self.mode_type.get_name())
        self.description_label.setText(self.mode_type.get_description())
        return None

    def _draw(self) -> None:
        self._draw_game_mode_widget()
        self._draw_players_widget()
        return None

    def _select_mode_type(self) -> None:
        self.mode_type = models.get_mode_type_by_name(self.selection_combo_box.currentText())
        self._draw_game_mode_widget()
        return None

    def _is_valid_name_for_new_player(self, name: str) -> bool:
        if not name:
            return False
        for player_name in self.player_names:
            if name == player_name:
                return False
        return True

    def _add_player(self) -> None:
        new_player_name = self.input_line_edit.text().strip()
        if self._is_valid_name_for_new_player(new_player_name):
            self.player_names.append(new_player_name)
        self.input_line_edit.setText("")
        self._draw_players_widget()
        return None

    def _remove_player(self) -> None:
        if (selection := self.overview_list_widget.currentItem()) is None:
            return None
        player_name = selection.text()
        index = self.player_names.index(player_name)
        self.player_names.remove(player_name)
        if index > (last_index := len(self.player_names) - 1):
            index = last_index
        self._draw_players_widget()
        self.overview_list_widget.setCurrentRow(index)
        return None

    def _move_player_up(self) -> None:
        if (selection := self.overview_list_widget.currentItem()) is None:
            return None
        player_name = selection.text()
        index = self.player_names.index(player_name)
        if index == 0:
            return None
        self.player_names.pop(index)
        new_index = index - 1
        self.player_names.insert(new_index, player_name)
        self._draw_players_widget()
        self.overview_list_widget.setCurrentRow(new_index)
        return None

    def _move_player_down(self) -> None:
        if (selection := self.overview_list_widget.currentItem()) is None:
            return None
        player_name = selection.text()
        index = self.player_names.index(player_name)
        if index == len(self.player_names) + 1:
            return None
        self.player_names.pop(index)
        new_index = index + 1
        self.player_names.insert(new_index, player_name)
        self._draw_players_widget()
        self.overview_list_widget.setCurrentRow(new_index)
        return None

    def _start_game(self) -> None:
        if not self.player_names:
            return None
        game = self.mode_type.from_player_names(self.player_names)
        self.finished.emit(game)
        return None
