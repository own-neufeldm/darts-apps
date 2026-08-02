# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pre_game_tab_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QTabWidget, QVBoxLayout, QWidget)

class Ui_pre_game_tab_widget(object):
    def setupUi(self, pre_game_tab_widget):
        if not pre_game_tab_widget.objectName():
            pre_game_tab_widget.setObjectName(u"pre_game_tab_widget")
        pre_game_tab_widget.resize(300, 350)
        pre_game_tab_widget.setMinimumSize(QSize(300, 350))
        pre_game_tab_widget.setMaximumSize(QSize(300, 350))
        self.game_mode_widget = QWidget()
        self.game_mode_widget.setObjectName(u"game_mode_widget")
        self.verticalLayout_3 = QVBoxLayout(self.game_mode_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.selection_widget = QWidget(self.game_mode_widget)
        self.selection_widget.setObjectName(u"selection_widget")
        self.horizontalLayout_4 = QHBoxLayout(self.selection_widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.selection_label = QLabel(self.selection_widget)
        self.selection_label.setObjectName(u"selection_label")

        self.horizontalLayout_4.addWidget(self.selection_label)

        self.selection_combo_box = QComboBox(self.selection_widget)
        self.selection_combo_box.setObjectName(u"selection_combo_box")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selection_combo_box.sizePolicy().hasHeightForWidth())
        self.selection_combo_box.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.selection_combo_box)


        self.verticalLayout_3.addWidget(self.selection_widget)

        self.description_widget = QWidget(self.game_mode_widget)
        self.description_widget.setObjectName(u"description_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.description_widget.sizePolicy().hasHeightForWidth())
        self.description_widget.setSizePolicy(sizePolicy1)
        self.verticalLayout_4 = QVBoxLayout(self.description_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.description_label = QLabel(self.description_widget)
        self.description_label.setObjectName(u"description_label")
        self.description_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.description_label.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.description_label)


        self.verticalLayout_3.addWidget(self.description_widget)

        self.game_mode_page_control_widget = QWidget(self.game_mode_widget)
        self.game_mode_page_control_widget.setObjectName(u"game_mode_page_control_widget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.game_mode_page_control_widget.sizePolicy().hasHeightForWidth())
        self.game_mode_page_control_widget.setSizePolicy(sizePolicy2)
        self.horizontalLayout_5 = QHBoxLayout(self.game_mode_page_control_widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.game_mode_next_page_push_button = QPushButton(self.game_mode_page_control_widget)
        self.game_mode_next_page_push_button.setObjectName(u"game_mode_next_page_push_button")

        self.horizontalLayout_5.addWidget(self.game_mode_next_page_push_button)


        self.verticalLayout_3.addWidget(self.game_mode_page_control_widget)

        pre_game_tab_widget.addTab(self.game_mode_widget, "")
        self.players_widget = QWidget()
        self.players_widget.setObjectName(u"players_widget")
        self.verticalLayout = QVBoxLayout(self.players_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.player_input_widget = QWidget(self.players_widget)
        self.player_input_widget.setObjectName(u"player_input_widget")
        self.player_input_widget.setStyleSheet(u"")
        self.horizontalLayout_3 = QHBoxLayout(self.player_input_widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.input_label = QLabel(self.player_input_widget)
        self.input_label.setObjectName(u"input_label")

        self.horizontalLayout_3.addWidget(self.input_label)

        self.input_line_edit = QLineEdit(self.player_input_widget)
        self.input_line_edit.setObjectName(u"input_line_edit")

        self.horizontalLayout_3.addWidget(self.input_line_edit)

        self.add_push_button = QPushButton(self.player_input_widget)
        self.add_push_button.setObjectName(u"add_push_button")

        self.horizontalLayout_3.addWidget(self.add_push_button)


        self.verticalLayout.addWidget(self.player_input_widget)

        self.player_overview_widget = QWidget(self.players_widget)
        self.player_overview_widget.setObjectName(u"player_overview_widget")
        self.verticalLayout_2 = QVBoxLayout(self.player_overview_widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.overview_list_widget = QListWidget(self.player_overview_widget)
        self.overview_list_widget.setObjectName(u"overview_list_widget")

        self.verticalLayout_2.addWidget(self.overview_list_widget)


        self.verticalLayout.addWidget(self.player_overview_widget)

        self.player_edit_widget = QWidget(self.players_widget)
        self.player_edit_widget.setObjectName(u"player_edit_widget")
        self.horizontalLayout = QHBoxLayout(self.player_edit_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.remove_push_button = QPushButton(self.player_edit_widget)
        self.remove_push_button.setObjectName(u"remove_push_button")

        self.horizontalLayout.addWidget(self.remove_push_button)

        self.move_up_push_button = QPushButton(self.player_edit_widget)
        self.move_up_push_button.setObjectName(u"move_up_push_button")

        self.horizontalLayout.addWidget(self.move_up_push_button)

        self.move_down_push_button = QPushButton(self.player_edit_widget)
        self.move_down_push_button.setObjectName(u"move_down_push_button")

        self.horizontalLayout.addWidget(self.move_down_push_button)


        self.verticalLayout.addWidget(self.player_edit_widget)

        self.players_page_controls_widget = QWidget(self.players_widget)
        self.players_page_controls_widget.setObjectName(u"players_page_controls_widget")
        self.horizontalLayout_2 = QHBoxLayout(self.players_page_controls_widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.players_previous_page_push_button = QPushButton(self.players_page_controls_widget)
        self.players_previous_page_push_button.setObjectName(u"players_previous_page_push_button")

        self.horizontalLayout_2.addWidget(self.players_previous_page_push_button)

        self.start_game_push_button = QPushButton(self.players_page_controls_widget)
        self.start_game_push_button.setObjectName(u"start_game_push_button")

        self.horizontalLayout_2.addWidget(self.start_game_push_button)


        self.verticalLayout.addWidget(self.players_page_controls_widget)

        pre_game_tab_widget.addTab(self.players_widget, "")

        self.retranslateUi(pre_game_tab_widget)

        pre_game_tab_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(pre_game_tab_widget)
    # setupUi

    def retranslateUi(self, pre_game_tab_widget):
        pre_game_tab_widget.setWindowTitle(QCoreApplication.translate("pre_game_tab_widget", u"Setup", None))
        self.selection_label.setText(QCoreApplication.translate("pre_game_tab_widget", u"Select game mode:", None))
        self.description_label.setText("")
        self.game_mode_next_page_push_button.setText(QCoreApplication.translate("pre_game_tab_widget", u"Next", None))
        pre_game_tab_widget.setTabText(pre_game_tab_widget.indexOf(self.game_mode_widget), QCoreApplication.translate("pre_game_tab_widget", u"Game mode", None))
        self.input_label.setText(QCoreApplication.translate("pre_game_tab_widget", u"Player name:", None))
        self.add_push_button.setText(QCoreApplication.translate("pre_game_tab_widget", u"Add", None))
        self.remove_push_button.setText(QCoreApplication.translate("pre_game_tab_widget", u"Remove", None))
        self.move_up_push_button.setText(QCoreApplication.translate("pre_game_tab_widget", u"Move up", None))
        self.move_down_push_button.setText(QCoreApplication.translate("pre_game_tab_widget", u"Move down", None))
        self.players_previous_page_push_button.setText(QCoreApplication.translate("pre_game_tab_widget", u"Previous", None))
        self.start_game_push_button.setText(QCoreApplication.translate("pre_game_tab_widget", u"Start", None))
        pre_game_tab_widget.setTabText(pre_game_tab_widget.indexOf(self.players_widget), QCoreApplication.translate("pre_game_tab_widget", u"Players", None))
    # retranslateUi

