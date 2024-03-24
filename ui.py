from PyQt5 import QtGui
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QGridLayout


class Ui_AutoRecruit(object):

    def setupUi(self, AutoRecruit):
        self.winSize(AutoRecruit)
        self.winUi(AutoRecruit)

    def winSize(self, AutoRecruit):
        # 窗口大小
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.screenheight = self.screenRect.height()
        self.screenwidth = self.screenRect.width()
        self.height = int(self.screenheight * 0.2)
        self.width = int(self.screenwidth * 0.3)
        AutoRecruit.resize(self.width, self.height)
        # 窗口标题
        AutoRecruit.setWindowTitle('明日方舟自动公招器')

        # Ui

    def winUi(self, AutoRecruit):
        ui = QGridLayout(self)

        # 按钮
        font1 = QtGui.QFont()
        font1.setFamily('Arial')
        font1.setBold(True)
        font1.setPointSize(20)
        font2 = QtGui.QFont()
        font2.setFamily('Arial')
        font2.setPointSize(15)
        StateFont = QtGui.QFont()
        StateFont.setFamily('Arial')
        StateFont.setBold(True)
        StateFont.setPointSize(15)
        self.b1 = QPushButton("开始")
        self.b2 = QPushButton("停止")
        self.b3 = QPushButton("联系作者(跳转作者B站首页)")
        self.b4 = QPushButton("修改Class")
        self.b5 = QPushButton("修改Title")
        self.b1.setFont(font1)
        self.b2.setFont(font1)
        self.b3.setFont(font1)
        self.b4.setFont(font2)
        self.b5.setFont(font2)
        ui.addWidget(self.b1, 0, 0, 1, 0)
        ui.addWidget(self.b2, 2, 0, 1, 0)
        ui.addWidget(self.b3, 4, 0, 1, 0)
        ui.addWidget(self.b4, 7, 0)
        ui.addWidget(self.b5, 6, 0)
        AutoRecruit.setLayout(ui)

        # 文字
        Class = QLabel("Class:")
        self.ClassName = QLabel("None")
        Title = QLabel("Title:")
        self.TitleName = QLabel("None")
        State1 = QLabel("游戏状态:")
        self.GameState = QLabel("游戏未识别")
        State2 = QLabel("程序状态:")
        self.ProState = QLabel("程序停止中")
        qq = QLabel("作者QQ:380599261")
        gameVer = QLabel("适用于明日方舟v2.2.21")
        ProVer = QLabel("程序版本v1.0")
        Class.setFont(QFont('Arial', 14))
        self.ClassName.setFont(QFont('Arial', 12))
        Title.setFont(QFont('Arial', 14))
        self.TitleName.setFont(QFont('Arial', 12))
        State1.setFont(QFont('Arial', 20))
        self.GameState.setFont(StateFont)
        State2.setFont(QFont('Arial', 20))
        self.ProState.setFont(StateFont)
        qq.setFont(QFont('Arial', 12))
        gameVer.setFont(QFont('Arial', 12))
        ProVer.setFont(QFont('Arial', 12))
        ui.addWidget(Class, 7, 1)
        ui.addWidget(self.ClassName, 7, 2, 1, 2)
        ui.addWidget(Title, 6, 1)
        ui.addWidget(self.TitleName, 6, 2, 1, 2)
        ui.addWidget(State1, 8, 0)
        ui.addWidget(self.GameState, 8, 1)
        ui.addWidget(State2, 9, 0)
        ui.addWidget(self.ProState, 9, 1)
        ui.addWidget(qq, 11, 3)
        ui.addWidget(gameVer, 12, 3)
        ui.addWidget(ProVer, 12, 0)
        self.GameState.setStyleSheet("background-color:red")
        self.ProState.setStyleSheet("background-color:red")
        AutoRecruit.setLayout(ui)
