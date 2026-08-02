# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'game_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_game_widget(object):
    def setupUi(self, game_widget):
        if not game_widget.objectName():
            game_widget.setObjectName(u"game_widget")
        game_widget.resize(700, 500)
        game_widget.setMinimumSize(QSize(700, 500))
        game_widget.setMaximumSize(QSize(700, 500))
        self.verticalLayout = QVBoxLayout(game_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.input_widget = QWidget(game_widget)
        self.input_widget.setObjectName(u"input_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.input_widget.sizePolicy().hasHeightForWidth())
        self.input_widget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.input_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.darts_widget = QWidget(self.input_widget)
        self.darts_widget.setObjectName(u"darts_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(6)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.darts_widget.sizePolicy().hasHeightForWidth())
        self.darts_widget.setSizePolicy(sizePolicy1)
        self.verticalLayout_4 = QVBoxLayout(self.darts_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.input_1_widget = QWidget(self.darts_widget)
        self.input_1_widget.setObjectName(u"input_1_widget")
        self.horizontalLayout_3 = QHBoxLayout(self.input_1_widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.input_single_radio_button = QRadioButton(self.input_1_widget)
        self.input_single_radio_button.setObjectName(u"input_single_radio_button")
        self.input_single_radio_button.setChecked(True)
        self.input_single_radio_button.setAutoExclusive(True)

        self.horizontalLayout_3.addWidget(self.input_single_radio_button)

        self.input_double_radio_button = QRadioButton(self.input_1_widget)
        self.input_double_radio_button.setObjectName(u"input_double_radio_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.input_double_radio_button.sizePolicy().hasHeightForWidth())
        self.input_double_radio_button.setSizePolicy(sizePolicy2)
        self.input_double_radio_button.setAutoExclusive(True)

        self.horizontalLayout_3.addWidget(self.input_double_radio_button)

        self.input_triple_radio_button = QRadioButton(self.input_1_widget)
        self.input_triple_radio_button.setObjectName(u"input_triple_radio_button")
        sizePolicy2.setHeightForWidth(self.input_triple_radio_button.sizePolicy().hasHeightForWidth())
        self.input_triple_radio_button.setSizePolicy(sizePolicy2)
        self.input_triple_radio_button.setAutoExclusive(True)

        self.horizontalLayout_3.addWidget(self.input_triple_radio_button)

        self.input_miss_push_button = QPushButton(self.input_1_widget)
        self.input_miss_push_button.setObjectName(u"input_miss_push_button")
        sizePolicy2.setHeightForWidth(self.input_miss_push_button.sizePolicy().hasHeightForWidth())
        self.input_miss_push_button.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.input_miss_push_button)


        self.verticalLayout_4.addWidget(self.input_1_widget)

        self.input_2_widget = QWidget(self.darts_widget)
        self.input_2_widget.setObjectName(u"input_2_widget")
        self.horizontalLayout_8 = QHBoxLayout(self.input_2_widget)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.input_1_push_button = QPushButton(self.input_2_widget)
        self.input_1_push_button.setObjectName(u"input_1_push_button")
        sizePolicy2.setHeightForWidth(self.input_1_push_button.sizePolicy().hasHeightForWidth())
        self.input_1_push_button.setSizePolicy(sizePolicy2)

        self.horizontalLayout_8.addWidget(self.input_1_push_button)

        self.input_2_push_button = QPushButton(self.input_2_widget)
        self.input_2_push_button.setObjectName(u"input_2_push_button")
        sizePolicy2.setHeightForWidth(self.input_2_push_button.sizePolicy().hasHeightForWidth())
        self.input_2_push_button.setSizePolicy(sizePolicy2)

        self.horizontalLayout_8.addWidget(self.input_2_push_button)

        self.input_3_push_button = QPushButton(self.input_2_widget)
        self.input_3_push_button.setObjectName(u"input_3_push_button")
        sizePolicy2.setHeightForWidth(self.input_3_push_button.sizePolicy().hasHeightForWidth())
        self.input_3_push_button.setSizePolicy(sizePolicy2)

        self.horizontalLayout_8.addWidget(self.input_3_push_button)


        self.verticalLayout_4.addWidget(self.input_2_widget)

        self.input_3_widget = QWidget(self.darts_widget)
        self.input_3_widget.setObjectName(u"input_3_widget")
        self.horizontalLayout_9 = QHBoxLayout(self.input_3_widget)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.input_4_push_button = QPushButton(self.input_3_widget)
        self.input_4_push_button.setObjectName(u"input_4_push_button")
        sizePolicy2.setHeightForWidth(self.input_4_push_button.sizePolicy().hasHeightForWidth())
        self.input_4_push_button.setSizePolicy(sizePolicy2)

        self.horizontalLayout_9.addWidget(self.input_4_push_button)

        self.input_5_push_button = QPushButton(self.input_3_widget)
        self.input_5_push_button.setObjectName(u"input_5_push_button")
        sizePolicy2.setHeightForWidth(self.input_5_push_button.sizePolicy().hasHeightForWidth())
        self.input_5_push_button.setSizePolicy(sizePolicy2)

        self.horizontalLayout_9.addWidget(self.input_5_push_button)

        self.input_6_push_button = QPushButton(self.input_3_widget)
        self.input_6_push_button.setObjectName(u"input_6_push_button")
        sizePolicy2.setHeightForWidth(self.input_6_push_button.sizePolicy().hasHeightForWidth())
        self.input_6_push_button.setSizePolicy(sizePolicy2)

        self.horizontalLayout_9.addWidget(self.input_6_push_button)


        self.verticalLayout_4.addWidget(self.input_3_widget)

        self.input_4_widget = QWidget(self.darts_widget)
        self.input_4_widget.setObjectName(u"input_4_widget")
        self.horizontalLayout_10 = QHBoxLayout(self.input_4_widget)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.input_7_push_button = QPushButton(self.input_4_widget)
        self.input_7_push_button.setObjectName(u"input_7_push_button")
        sizePolicy2.setHeightForWidth(self.input_7_push_button.sizePolicy().hasHeightForWidth())
        self.input_7_push_button.setSizePolicy(sizePolicy2)

        self.horizontalLayout_10.addWidget(self.input_7_push_button)

        self.input_8_push_button = QPushButton(self.input_4_widget)
        self.input_8_push_button.setObjectName(u"input_8_push_button")
        sizePolicy2.setHeightForWidth(self.input_8_push_button.sizePolicy().hasHeightForWidth())
        self.input_8_push_button.setSizePolicy(sizePolicy2)

        self.horizontalLayout_10.addWidget(self.input_8_push_button)

        self.input_9_push_button = QPushButton(self.input_4_widget)
        self.input_9_push_button.setObjectName(u"input_9_push_button")
        sizePolicy2.setHeightForWidth(self.input_9_push_button.sizePolicy().hasHeightForWidth())
        self.input_9_push_button.setSizePolicy(sizePolicy2)

        self.horizontalLayout_10.addWidget(self.input_9_push_button)


        self.verticalLayout_4.addWidget(self.input_4_widget)

        self.input_5_widget = QWidget(self.darts_widget)
        self.input_5_widget.setObjectName(u"input_5_widget")
        self.horizontalLayout_11 = QHBoxLayout(self.input_5_widget)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.input_10_push_button = QPushButton(self.input_5_widget)
        self.input_10_push_button.setObjectName(u"input_10_push_button")
        sizePolicy2.setHeightForWidth(self.input_10_push_button.sizePolicy().hasHeightForWidth())
        self.input_10_push_button.setSizePolicy(sizePolicy2)

        self.horizontalLayout_11.addWidget(self.input_10_push_button)

        self.input_11_push_button = QPushButton(self.input_5_widget)
        self.input_11_push_button.setObjectName(u"input_11_push_button")
        sizePolicy2.setHeightForWidth(self.input_11_push_button.sizePolicy().hasHeightForWidth())
        self.input_11_push_button.setSizePolicy(sizePolicy2)

        self.horizontalLayout_11.addWidget(self.input_11_push_button)

        self.input_12_push_button = QPushButton(self.input_5_widget)
        self.input_12_push_button.setObjectName(u"input_12_push_button")
        sizePolicy2.setHeightForWidth(self.input_12_push_button.sizePolicy().hasHeightForWidth())
        self.input_12_push_button.setSizePolicy(sizePolicy2)

        self.horizontalLayout_11.addWidget(self.input_12_push_button)


        self.verticalLayout_4.addWidget(self.input_5_widget)

        self.input_6_widget = QWidget(self.darts_widget)
        self.input_6_widget.setObjectName(u"input_6_widget")
        self.horizontalLayout_12 = QHBoxLayout(self.input_6_widget)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.input_13_push_button = QPushButton(self.input_6_widget)
        self.input_13_push_button.setObjectName(u"input_13_push_button")
        sizePolicy2.setHeightForWidth(self.input_13_push_button.sizePolicy().hasHeightForWidth())
        self.input_13_push_button.setSizePolicy(sizePolicy2)

        self.horizontalLayout_12.addWidget(self.input_13_push_button)

        self.input_14_push_button = QPushButton(self.input_6_widget)
        self.input_14_push_button.setObjectName(u"input_14_push_button")
        sizePolicy2.setHeightForWidth(self.input_14_push_button.sizePolicy().hasHeightForWidth())
        self.input_14_push_button.setSizePolicy(sizePolicy2)

        self.horizontalLayout_12.addWidget(self.input_14_push_button)

        self.input_15_push_button = QPushButton(self.input_6_widget)
        self.input_15_push_button.setObjectName(u"input_15_push_button")
        sizePolicy2.setHeightForWidth(self.input_15_push_button.sizePolicy().hasHeightForWidth())
        self.input_15_push_button.setSizePolicy(sizePolicy2)

        self.horizontalLayout_12.addWidget(self.input_15_push_button)


        self.verticalLayout_4.addWidget(self.input_6_widget)

        self.input_7_widget = QWidget(self.darts_widget)
        self.input_7_widget.setObjectName(u"input_7_widget")
        self.horizontalLayout_13 = QHBoxLayout(self.input_7_widget)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.input_16_push_button = QPushButton(self.input_7_widget)
        self.input_16_push_button.setObjectName(u"input_16_push_button")
        sizePolicy2.setHeightForWidth(self.input_16_push_button.sizePolicy().hasHeightForWidth())
        self.input_16_push_button.setSizePolicy(sizePolicy2)

        self.horizontalLayout_13.addWidget(self.input_16_push_button)

        self.input_17_push_button = QPushButton(self.input_7_widget)
        self.input_17_push_button.setObjectName(u"input_17_push_button")
        sizePolicy2.setHeightForWidth(self.input_17_push_button.sizePolicy().hasHeightForWidth())
        self.input_17_push_button.setSizePolicy(sizePolicy2)

        self.horizontalLayout_13.addWidget(self.input_17_push_button)

        self.input_18_push_button = QPushButton(self.input_7_widget)
        self.input_18_push_button.setObjectName(u"input_18_push_button")
        sizePolicy2.setHeightForWidth(self.input_18_push_button.sizePolicy().hasHeightForWidth())
        self.input_18_push_button.setSizePolicy(sizePolicy2)

        self.horizontalLayout_13.addWidget(self.input_18_push_button)


        self.verticalLayout_4.addWidget(self.input_7_widget)

        self.input_8_widget = QWidget(self.darts_widget)
        self.input_8_widget.setObjectName(u"input_8_widget")
        self.horizontalLayout_14 = QHBoxLayout(self.input_8_widget)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.input_19_push_button = QPushButton(self.input_8_widget)
        self.input_19_push_button.setObjectName(u"input_19_push_button")
        sizePolicy2.setHeightForWidth(self.input_19_push_button.sizePolicy().hasHeightForWidth())
        self.input_19_push_button.setSizePolicy(sizePolicy2)

        self.horizontalLayout_14.addWidget(self.input_19_push_button)

        self.input_20_push_button = QPushButton(self.input_8_widget)
        self.input_20_push_button.setObjectName(u"input_20_push_button")
        sizePolicy2.setHeightForWidth(self.input_20_push_button.sizePolicy().hasHeightForWidth())
        self.input_20_push_button.setSizePolicy(sizePolicy2)

        self.horizontalLayout_14.addWidget(self.input_20_push_button)

        self.input_25_push_button = QPushButton(self.input_8_widget)
        self.input_25_push_button.setObjectName(u"input_25_push_button")
        sizePolicy2.setHeightForWidth(self.input_25_push_button.sizePolicy().hasHeightForWidth())
        self.input_25_push_button.setSizePolicy(sizePolicy2)

        self.horizontalLayout_14.addWidget(self.input_25_push_button)


        self.verticalLayout_4.addWidget(self.input_8_widget)


        self.horizontalLayout.addWidget(self.darts_widget)

        self.turn_widget = QWidget(self.input_widget)
        self.turn_widget.setObjectName(u"turn_widget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.turn_widget.sizePolicy().hasHeightForWidth())
        self.turn_widget.setSizePolicy(sizePolicy3)
        self.verticalLayout_3 = QVBoxLayout(self.turn_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.turn_order_widget = QWidget(self.turn_widget)
        self.turn_order_widget.setObjectName(u"turn_order_widget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(1)
        sizePolicy4.setHeightForWidth(self.turn_order_widget.sizePolicy().hasHeightForWidth())
        self.turn_order_widget.setSizePolicy(sizePolicy4)
        self.horizontalLayout_7 = QHBoxLayout(self.turn_order_widget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.turn_order_key_label = QLabel(self.turn_order_widget)
        self.turn_order_key_label.setObjectName(u"turn_order_key_label")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(4)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.turn_order_key_label.sizePolicy().hasHeightForWidth())
        self.turn_order_key_label.setSizePolicy(sizePolicy5)
        self.turn_order_key_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_7.addWidget(self.turn_order_key_label)

        self.turn_order_value_label = QLabel(self.turn_order_widget)
        self.turn_order_value_label.setObjectName(u"turn_order_value_label")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(5)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.turn_order_value_label.sizePolicy().hasHeightForWidth())
        self.turn_order_value_label.setSizePolicy(sizePolicy6)
        self.turn_order_value_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_7.addWidget(self.turn_order_value_label)


        self.verticalLayout_3.addWidget(self.turn_order_widget)

        self.current_player_widget = QWidget(self.turn_widget)
        self.current_player_widget.setObjectName(u"current_player_widget")
        self.current_player_widget.setEnabled(True)
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.current_player_widget.sizePolicy().hasHeightForWidth())
        self.current_player_widget.setSizePolicy(sizePolicy7)
        self.horizontalLayout_2 = QHBoxLayout(self.current_player_widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.current_player_key_label = QLabel(self.current_player_widget)
        self.current_player_key_label.setObjectName(u"current_player_key_label")
        sizePolicy5.setHeightForWidth(self.current_player_key_label.sizePolicy().hasHeightForWidth())
        self.current_player_key_label.setSizePolicy(sizePolicy5)

        self.horizontalLayout_2.addWidget(self.current_player_key_label)

        self.current_player_value_label = QLabel(self.current_player_widget)
        self.current_player_value_label.setObjectName(u"current_player_value_label")
        sizePolicy6.setHeightForWidth(self.current_player_value_label.sizePolicy().hasHeightForWidth())
        self.current_player_value_label.setSizePolicy(sizePolicy6)
        self.current_player_value_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.current_player_value_label)


        self.verticalLayout_3.addWidget(self.current_player_widget)

        self.throws_widget = QWidget(self.turn_widget)
        self.throws_widget.setObjectName(u"throws_widget")
        sizePolicy7.setHeightForWidth(self.throws_widget.sizePolicy().hasHeightForWidth())
        self.throws_widget.setSizePolicy(sizePolicy7)
        self.horizontalLayout_4 = QHBoxLayout(self.throws_widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.throw_1_line_edit = QLineEdit(self.throws_widget)
        self.throw_1_line_edit.setObjectName(u"throw_1_line_edit")
        self.throw_1_line_edit.setEnabled(True)
        self.throw_1_line_edit.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.throw_1_line_edit)

        self.throw_2_line_edit = QLineEdit(self.throws_widget)
        self.throw_2_line_edit.setObjectName(u"throw_2_line_edit")
        self.throw_2_line_edit.setEnabled(True)
        self.throw_2_line_edit.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.throw_2_line_edit)

        self.throw_3_line_edit = QLineEdit(self.throws_widget)
        self.throw_3_line_edit.setObjectName(u"throw_3_line_edit")
        self.throw_3_line_edit.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.throw_3_line_edit)


        self.verticalLayout_3.addWidget(self.throws_widget)

        self.turn_control_widget = QWidget(self.turn_widget)
        self.turn_control_widget.setObjectName(u"turn_control_widget")
        sizePolicy7.setHeightForWidth(self.turn_control_widget.sizePolicy().hasHeightForWidth())
        self.turn_control_widget.setSizePolicy(sizePolicy7)
        self.horizontalLayout_5 = QHBoxLayout(self.turn_control_widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.next_turn_push_button = QPushButton(self.turn_control_widget)
        self.next_turn_push_button.setObjectName(u"next_turn_push_button")

        self.horizontalLayout_5.addWidget(self.next_turn_push_button)


        self.verticalLayout_3.addWidget(self.turn_control_widget)

        self.hint_widget = QWidget(self.turn_widget)
        self.hint_widget.setObjectName(u"hint_widget")
        sizePolicy4.setHeightForWidth(self.hint_widget.sizePolicy().hasHeightForWidth())
        self.hint_widget.setSizePolicy(sizePolicy4)
        self.horizontalLayout_6 = QHBoxLayout(self.hint_widget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.hint_label = QLabel(self.hint_widget)
        self.hint_label.setObjectName(u"hint_label")
        sizePolicy7.setHeightForWidth(self.hint_label.sizePolicy().hasHeightForWidth())
        self.hint_label.setSizePolicy(sizePolicy7)
        font = QFont()
        font.setItalic(True)
        self.hint_label.setFont(font)
        self.hint_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_6.addWidget(self.hint_label)


        self.verticalLayout_3.addWidget(self.hint_widget)


        self.horizontalLayout.addWidget(self.turn_widget)


        self.verticalLayout.addWidget(self.input_widget)

        self.finish_game_widget = QWidget(game_widget)
        self.finish_game_widget.setObjectName(u"finish_game_widget")
        sizePolicy7.setHeightForWidth(self.finish_game_widget.sizePolicy().hasHeightForWidth())
        self.finish_game_widget.setSizePolicy(sizePolicy7)
        self.verticalLayout_2 = QVBoxLayout(self.finish_game_widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.finish_game_push_button = QPushButton(self.finish_game_widget)
        self.finish_game_push_button.setObjectName(u"finish_game_push_button")

        self.verticalLayout_2.addWidget(self.finish_game_push_button)


        self.verticalLayout.addWidget(self.finish_game_widget)


        self.retranslateUi(game_widget)

        QMetaObject.connectSlotsByName(game_widget)
    # setupUi

    def retranslateUi(self, game_widget):
        game_widget.setWindowTitle(QCoreApplication.translate("game_widget", u"Game", None))
        self.input_single_radio_button.setText(QCoreApplication.translate("game_widget", u"Single", None))
        self.input_double_radio_button.setText(QCoreApplication.translate("game_widget", u"Double", None))
        self.input_triple_radio_button.setText(QCoreApplication.translate("game_widget", u"Triple", None))
        self.input_miss_push_button.setText(QCoreApplication.translate("game_widget", u"Miss", None))
        self.input_1_push_button.setText(QCoreApplication.translate("game_widget", u"1", None))
        self.input_2_push_button.setText(QCoreApplication.translate("game_widget", u"2", None))
        self.input_3_push_button.setText(QCoreApplication.translate("game_widget", u"3", None))
        self.input_4_push_button.setText(QCoreApplication.translate("game_widget", u"4", None))
        self.input_5_push_button.setText(QCoreApplication.translate("game_widget", u"5", None))
        self.input_6_push_button.setText(QCoreApplication.translate("game_widget", u"6", None))
        self.input_7_push_button.setText(QCoreApplication.translate("game_widget", u"7", None))
        self.input_8_push_button.setText(QCoreApplication.translate("game_widget", u"8", None))
        self.input_9_push_button.setText(QCoreApplication.translate("game_widget", u"9", None))
        self.input_10_push_button.setText(QCoreApplication.translate("game_widget", u"10", None))
        self.input_11_push_button.setText(QCoreApplication.translate("game_widget", u"11", None))
        self.input_12_push_button.setText(QCoreApplication.translate("game_widget", u"12", None))
        self.input_13_push_button.setText(QCoreApplication.translate("game_widget", u"13", None))
        self.input_14_push_button.setText(QCoreApplication.translate("game_widget", u"14", None))
        self.input_15_push_button.setText(QCoreApplication.translate("game_widget", u"15", None))
        self.input_16_push_button.setText(QCoreApplication.translate("game_widget", u"16", None))
        self.input_17_push_button.setText(QCoreApplication.translate("game_widget", u"17", None))
        self.input_18_push_button.setText(QCoreApplication.translate("game_widget", u"18", None))
        self.input_19_push_button.setText(QCoreApplication.translate("game_widget", u"19", None))
        self.input_20_push_button.setText(QCoreApplication.translate("game_widget", u"20", None))
        self.input_25_push_button.setText(QCoreApplication.translate("game_widget", u"25", None))
        self.turn_order_key_label.setText(QCoreApplication.translate("game_widget", u"Turn order:", None))
        self.turn_order_value_label.setText("")
        self.current_player_key_label.setText(QCoreApplication.translate("game_widget", u"Current player:", None))
        self.current_player_value_label.setText("")
        self.next_turn_push_button.setText(QCoreApplication.translate("game_widget", u"Next", None))
        self.hint_label.setText("")
        self.finish_game_push_button.setText(QCoreApplication.translate("game_widget", u"Finish", None))
    # retranslateUi

