# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'post_game_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_post_game_widget(object):
    def setupUi(self, post_game_widget):
        if not post_game_widget.objectName():
            post_game_widget.setObjectName(u"post_game_widget")
        post_game_widget.resize(300, 350)
        post_game_widget.setMinimumSize(QSize(300, 350))
        post_game_widget.setMaximumSize(QSize(300, 350))
        self.verticalLayout = QVBoxLayout(post_game_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.leaderboard_widget = QWidget(post_game_widget)
        self.leaderboard_widget.setObjectName(u"leaderboard_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.leaderboard_widget.sizePolicy().hasHeightForWidth())
        self.leaderboard_widget.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(self.leaderboard_widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.leaderboard_label = QLabel(self.leaderboard_widget)
        self.leaderboard_label.setObjectName(u"leaderboard_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leaderboard_label.sizePolicy().hasHeightForWidth())
        self.leaderboard_label.setSizePolicy(sizePolicy1)
        self.leaderboard_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_2.addWidget(self.leaderboard_label)


        self.verticalLayout.addWidget(self.leaderboard_widget)

        self.end_game_widget = QWidget(post_game_widget)
        self.end_game_widget.setObjectName(u"end_game_widget")
        self.horizontalLayout = QHBoxLayout(self.end_game_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.play_again_push_button = QPushButton(self.end_game_widget)
        self.play_again_push_button.setObjectName(u"play_again_push_button")

        self.horizontalLayout.addWidget(self.play_again_push_button)

        self.exit_game_push_button = QPushButton(self.end_game_widget)
        self.exit_game_push_button.setObjectName(u"exit_game_push_button")

        self.horizontalLayout.addWidget(self.exit_game_push_button)


        self.verticalLayout.addWidget(self.end_game_widget)


        self.retranslateUi(post_game_widget)

        QMetaObject.connectSlotsByName(post_game_widget)
    # setupUi

    def retranslateUi(self, post_game_widget):
        post_game_widget.setWindowTitle(QCoreApplication.translate("post_game_widget", u"Results", None))
        self.leaderboard_label.setText("")
        self.play_again_push_button.setText(QCoreApplication.translate("post_game_widget", u"Play again", None))
        self.exit_game_push_button.setText(QCoreApplication.translate("post_game_widget", u"Exit", None))
    # retranslateUi

