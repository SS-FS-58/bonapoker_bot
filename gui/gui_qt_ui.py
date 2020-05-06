# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_QT_ui.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Pokerbot(object):
    def setupUi(self, Pokerbot):
        Pokerbot.setObjectName("Pokerbot")
        Pokerbot.setEnabled(True)
        Pokerbot.resize(617, 713)



        Pokerbot.setMaximumSize(QtCore.QSize(617, 713))
        font = QtGui.QFont()
        font.setPointSize(12)
        Pokerbot.setFont(font)
        Pokerbot.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(Pokerbot)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.vLayout = QtWidgets.QVBoxLayout()
        self.vLayout.setObjectName("vLayout")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.vLayout.addWidget(self.widget_3)
        self.gridLayout.addLayout(self.vLayout, 8, 0, 1, 3)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 0, 2, 1, 2)
        self.vLayout4 = QtWidgets.QVBoxLayout()
        self.vLayout4.setObjectName("vLayout4")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.vLayout4.addWidget(self.widget_2)
        self.gridLayout.addLayout(self.vLayout4, 9, 3, 1, 3)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.button_resume = QtWidgets.QPushButton(self.centralwidget)
        self.button_resume.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_resume.setFont(font)
        self.button_resume.setObjectName("button_resume")
        self.verticalLayout_7.addWidget(self.button_resume)
        self.button_pause = QtWidgets.QPushButton(self.centralwidget)
        self.button_pause.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_pause.setFont(font)
        self.button_pause.setObjectName("button_pause")
        self.verticalLayout_7.addWidget(self.button_pause)
        self.button_log_analyser = QtWidgets.QPushButton(self.centralwidget)
        self.button_log_analyser.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_log_analyser.setFont(font)
        self.button_log_analyser.setObjectName("button_log_analyser")
        self.verticalLayout_7.addWidget(self.button_log_analyser)
        self.button_strategy_editor = QtWidgets.QPushButton(self.centralwidget)
        self.button_strategy_editor.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_strategy_editor.setFont(font)
        self.button_strategy_editor.setObjectName("button_strategy_editor")
        self.verticalLayout_7.addWidget(self.button_strategy_editor)
        self.button_genetic_algorithm = QtWidgets.QPushButton(self.centralwidget)
        self.button_genetic_algorithm.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_genetic_algorithm.setFont(font)
        self.button_genetic_algorithm.setObjectName("button_genetic_algorithm")
        self.verticalLayout_7.addWidget(self.button_genetic_algorithm)
        self.gridLayout.addLayout(self.verticalLayout_7, 5, 0, 1, 3)
        self.vLayout2 = QtWidgets.QVBoxLayout()
        self.vLayout2.setObjectName("vLayout2")
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setObjectName("widget_4")
        self.vLayout2.addWidget(self.widget_4)
        self.gridLayout.addLayout(self.vLayout2, 8, 3, 1, 3)
        self.pushButton_setup = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_setup.setFont(font)
        self.pushButton_setup.setObjectName("pushButton_setup")
        self.gridLayout.addWidget(self.pushButton_setup, 0, 0, 1, 1)
        self.pushButton_help = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_help.setFont(font)
        self.pushButton_help.setObjectName("pushButton_help")
        self.gridLayout.addWidget(self.pushButton_help, 0, 5, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.last_decision = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.last_decision.setFont(font)
        self.last_decision.setAutoFillBackground(False)
        self.last_decision.setFrameShape(QtWidgets.QFrame.Panel)
        self.last_decision.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.last_decision.setScaledContents(False)
        self.last_decision.setAlignment(QtCore.Qt.AlignCenter)
        self.last_decision.setIndent(-1)
        self.last_decision.setObjectName("last_decision")
        self.gridLayout_2.addWidget(self.last_decision, 2, 0, 1, 1)
        self.progress_bar = QtWidgets.QProgressBar(self.centralwidget)
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setObjectName("progress_bar")
        self.gridLayout_2.addWidget(self.progress_bar, 5, 0, 1, 1)
        self.comboBox_current_strategy = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_current_strategy.setFont(font)
        self.comboBox_current_strategy.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboBox_current_strategy.setObjectName("comboBox_current_strategy")
        self.gridLayout_2.addWidget(self.comboBox_current_strategy, 6, 0, 1, 1)
        self.status = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.status.setFont(font)
        self.status.setToolTip("")
        self.status.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.status.setAlignment(QtCore.Qt.AlignCenter)
        self.status.setObjectName("status")
        self.gridLayout_2.addWidget(self.status, 4, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 5, 3, 1, 3)
        self.vLayout3 = QtWidgets.QVBoxLayout()
        self.vLayout3.setObjectName("vLayout3")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.vLayout3.addWidget(self.widget)
        self.gridLayout.addLayout(self.vLayout3, 9, 0, 1, 3)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.winnings = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.winnings.setFont(font)
        self.winnings.setText("")
        self.winnings.setObjectName("winnings")
        self.verticalLayout_6.addWidget(self.winnings)
        self.assumed_players = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.assumed_players.setFont(font)
        self.assumed_players.setText("")
        self.assumed_players.setObjectName("assumed_players")
        self.verticalLayout_6.addWidget(self.assumed_players)
        self.mincallequity = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mincallequity.setFont(font)
        self.mincallequity.setText("")
        self.mincallequity.setObjectName("mincallequity")
        self.verticalLayout_6.addWidget(self.mincallequity)
        self.minbetequity = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.minbetequity.setFont(font)
        self.minbetequity.setText("")
        self.minbetequity.setObjectName("minbetequity")
        self.verticalLayout_6.addWidget(self.minbetequity)
        self.required_mincall = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.required_mincall.setFont(font)
        self.required_mincall.setText("")
        self.required_mincall.setObjectName("required_mincall")
        self.verticalLayout_6.addWidget(self.required_mincall)
        self.required_minbet = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.required_minbet.setFont(font)
        self.required_minbet.setText("")
        self.required_minbet.setObjectName("required_minbet")
        self.verticalLayout_6.addWidget(self.required_minbet)
        self.round_pot = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.round_pot.setFont(font)
        self.round_pot.setText("")
        self.round_pot.setObjectName("round_pot")
        self.verticalLayout_6.addWidget(self.round_pot)
        self.pot_multiple = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pot_multiple.setFont(font)
        self.pot_multiple.setText("")
        self.pot_multiple.setObjectName("pot_multiple")
        self.verticalLayout_6.addWidget(self.pot_multiple)
        self.calllimit = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.calllimit.setFont(font)
        self.calllimit.setText("")
        self.calllimit.setObjectName("calllimit")
        self.verticalLayout_6.addWidget(self.calllimit)
        self.betlimit = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.betlimit.setFont(font)
        self.betlimit.setText("")
        self.betlimit.setObjectName("betlimit")
        self.verticalLayout_6.addWidget(self.betlimit)
        self.outs = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.outs.setFont(font)
        self.outs.setText("")
        self.outs.setObjectName("outs")
        self.verticalLayout_6.addWidget(self.outs)
        self.gridLayout.addLayout(self.verticalLayout_6, 3, 5, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_5.addWidget(self.label_10)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.verticalLayout_5.addWidget(self.label1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_5.addWidget(self.label_8)
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_5.addWidget(self.label_21)
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_5.addWidget(self.label_23)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_5.addWidget(self.label_12)
        self.gridLayout.addLayout(self.verticalLayout_5, 3, 3, 1, 2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.equity = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.equity.setFont(font)
        self.equity.setText("")
        self.equity.setObjectName("equity")
        self.verticalLayout_3.addWidget(self.equity)
        self.range_equity = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.range_equity.setFont(font)
        self.range_equity.setText("")
        self.range_equity.setObjectName("range_equity")
        self.verticalLayout_3.addWidget(self.range_equity)
        self.relative_equity = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.relative_equity.setFont(font)
        self.relative_equity.setText("")
        self.relative_equity.setObjectName("relative_equity")
        self.verticalLayout_3.addWidget(self.relative_equity)
        self.sheetname = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sheetname.setFont(font)
        self.sheetname.setText("")
        self.sheetname.setObjectName("sheetname")
        self.verticalLayout_3.addWidget(self.sheetname)
        self.opponent_range = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.opponent_range.setFont(font)
        self.opponent_range.setText("")
        self.opponent_range.setObjectName("opponent_range")
        self.verticalLayout_3.addWidget(self.opponent_range)
        self.mycards = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mycards.setFont(font)
        self.mycards.setText("")
        self.mycards.setObjectName("mycards")
        self.verticalLayout_3.addWidget(self.mycards)
        self.tablecards = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tablecards.setFont(font)
        self.tablecards.setText("")
        self.tablecards.setObjectName("tablecards")
        self.verticalLayout_3.addWidget(self.tablecards)
        self.collusion_cards = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.collusion_cards.setFont(font)
        self.collusion_cards.setText("")
        self.collusion_cards.setObjectName("collusion_cards")
        self.verticalLayout_3.addWidget(self.collusion_cards)
        self.runs = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.runs.setFont(font)
        self.runs.setText("")
        self.runs.setObjectName("runs")
        self.verticalLayout_3.addWidget(self.runs)
        self.initiative = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.initiative.setFont(font)
        self.initiative.setText("")
        self.initiative.setObjectName("initiative")
        self.verticalLayout_3.addWidget(self.initiative)
        self.gamenumber = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gamenumber.setFont(font)
        self.gamenumber.setText("")
        self.gamenumber.setObjectName("gamenumber")
        self.verticalLayout_3.addWidget(self.gamenumber)
        self.gridLayout.addLayout(self.verticalLayout_3, 3, 2, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_4.addWidget(self.label_19)
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_4.addWidget(self.label_20)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_4.addWidget(self.label_9)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_4.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_4.addWidget(self.label_14)
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_4.addWidget(self.label_16)
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_4.addWidget(self.label_17)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_4.addWidget(self.label_15)
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_4.addWidget(self.label_18)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.gridLayout.addLayout(self.verticalLayout_4, 3, 0, 1, 2)
        Pokerbot.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Pokerbot)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName("statusbar")
        Pokerbot.setStatusBar(self.statusbar)

        self.retranslateUi(Pokerbot)
        QtCore.QMetaObject.connectSlotsByName(Pokerbot)

    def retranslateUi(self, Pokerbot):
        _translate = QtCore.QCoreApplication.translate
        Pokerbot.setWindowTitle(_translate("Pokerbot", "BonaPokerBot"))
        self.label_11.setText(_translate("Pokerbot", "Bona Poker CN Bot"))
        self.button_resume.setText(_translate("Pokerbot", "Start"))
        self.button_pause.setText(_translate("Pokerbot", "Stop"))
        self.button_log_analyser.setToolTip(_translate("Pokerbot", "Analyse past hands that the bot has played so you can improve the strategies"))
        self.button_log_analyser.setText(_translate("Pokerbot", "Strategy Analyser"))
        self.button_strategy_editor.setToolTip(_translate("Pokerbot", "Here you can edit strategies and adjust the bot to your needs"))
        self.button_strategy_editor.setText(_translate("Pokerbot", "Strategy Editor"))
        self.button_genetic_algorithm.setToolTip(_translate("Pokerbot", "<html><head/><body><p>An automatic algorithm that suggests what you need to change. It shows you at each stage whether you need to be more or less aggressive in calling, betting, bluffing etc.</p></body></html>"))
        self.button_genetic_algorithm.setText(_translate("Pokerbot", "Genetic Algorithm"))
        self.pushButton_setup.setToolTip(_translate("Pokerbot", "<html><head/><body><p>Setup which virtual machine the bot should access. You need to install Virtualbox to use this function (available for free). The pokerstars software will then run in the virtualbox and the pokerbot needs to run outside of the virtualbox.</p></body></html>"))
        self.pushButton_setup.setText(_translate("Pokerbot", "Setup"))
        self.pushButton_help.setText(_translate("Pokerbot", "Help"))
        self.last_decision.setToolTip(_translate("Pokerbot", "Last made decision by the bot"))
        self.last_decision.setText(_translate("Pokerbot", "Last Decision"))
        self.progress_bar.setToolTip(_translate("Pokerbot", "Shows progress when the buttons appear"))
        self.comboBox_current_strategy.setToolTip(_translate("Pokerbot", "Choose the strategy that the bot should use to play"))
        self.status.setText(_translate("Pokerbot", "I\'m ready!"))
        self.label_10.setText(_translate("Pokerbot", "BB wins per 100 hands"))
        self.label_6.setText(_translate("Pokerbot", "Assumed players"))
        self.label1.setText(_translate("Pokerbot", "Minimum call equity after adj"))
        self.label_5.setText(_translate("Pokerbot", "Minimum bet equity after adj"))
        self.label_7.setText(_translate("Pokerbot", "Required call (or pot multiple)"))
        self.label_8.setText(_translate("Pokerbot", "Required bet (or pot multiple)"))
        self.label_21.setText(_translate("Pokerbot", "Pot of this round"))
        self.label_23.setText(_translate("Pokerbot", "Player pot / round pot multiple"))
        self.label_3.setText(_translate("Pokerbot", "Final maximum call threshold"))
        self.label_4.setText(_translate("Pokerbot", "Final maximum bet threshold"))
        self.label_12.setText(_translate("Pokerbot", "Outs"))
        self.label_2.setText(_translate("Pokerbot", "Bot absolute equity"))
        self.label_19.setText(_translate("Pokerbot", "Bot range equity"))
        self.label_20.setText(_translate("Pokerbot", "Bot relative equity"))
        self.label_9.setText(_translate("Pokerbot", "Bot preflop sheet"))
        self.label_13.setText(_translate("Pokerbot", "Opponent range"))
        self.label_14.setText(_translate("Pokerbot", "Bot cards"))
        self.label_16.setText(_translate("Pokerbot", "Table cards"))
        self.label_17.setText(_translate("Pokerbot", "Collusion cards"))
        self.label_15.setText(_translate("Pokerbot", "Montecarlo runs"))
        self.label_18.setText(_translate("Pokerbot", "Other player has initiative"))
        self.label.setText(_translate("Pokerbot", "Hand number"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Pokerbot = QtWidgets.QMainWindow()
    ui = Ui_Pokerbot()
    ui.setupUi(Pokerbot)
    Pokerbot.show()
    sys.exit(app.exec_())

