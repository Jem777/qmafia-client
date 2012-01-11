# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/game.ui'
#
# Created: Wed Jan 11 19:15:33 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_game(object):
    def setupUi(self, game):
        game.setObjectName(_fromUtf8("game"))
        game.resize(835, 623)
        game.setWindowTitle(QtGui.QApplication.translate("game", "Quantenmafia, qmafia-client", None, QtGui.QApplication.UnicodeUTF8))
        self.centralwidget = QtGui.QWidget(game)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 741, 461))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lHeadline = QtGui.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lHeadline.sizePolicy().hasHeightForWidth())
        self.lHeadline.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.lHeadline.setFont(font)
        self.lHeadline.setText(QtGui.QApplication.translate("game", "Quantenmafia", None, QtGui.QApplication.UnicodeUTF8))
        self.lHeadline.setObjectName(_fromUtf8("lHeadline"))
        self.horizontalLayout.addWidget(self.lHeadline)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.lPhaseHint = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lPhaseHint.setFont(font)
        self.lPhaseHint.setText(QtGui.QApplication.translate("game", "Es ist", None, QtGui.QApplication.UnicodeUTF8))
        self.lPhaseHint.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lPhaseHint.setObjectName(_fromUtf8("lPhaseHint"))
        self.horizontalLayout_2.addWidget(self.lPhaseHint)
        self.lPhase = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.lPhase.setFont(font)
        self.lPhase.setText(QtGui.QApplication.translate("game", "Mafia-Phase", None, QtGui.QApplication.UnicodeUTF8))
        self.lPhase.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lPhase.setObjectName(_fromUtf8("lPhase"))
        self.horizontalLayout_2.addWidget(self.lPhase)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.lYouHint = QtGui.QLabel(self.verticalLayoutWidget)
        self.lYouHint.setText(QtGui.QApplication.translate("game", "Du bist", None, QtGui.QApplication.UnicodeUTF8))
        self.lYouHint.setObjectName(_fromUtf8("lYouHint"))
        self.verticalLayout_2.addWidget(self.lYouHint)
        self.tableView_2 = QtGui.QTableView(self.verticalLayoutWidget)
        self.tableView_2.setObjectName(_fromUtf8("tableView_2"))
        self.verticalLayout_2.addWidget(self.tableView_2)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setText(QtGui.QApplication.translate("game", "Wahrscheinlichkeiten\n"
"in anderer Reihenfolge", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_3.addWidget(self.label)
        self.tableView = QtGui.QTableView(self.verticalLayoutWidget)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.verticalLayout_3.addWidget(self.tableView)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        game.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(game)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 835, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        game.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(game)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        game.setStatusBar(self.statusbar)

        self.retranslateUi(game)
        QtCore.QMetaObject.connectSlotsByName(game)

    def retranslateUi(self, game):
        pass

