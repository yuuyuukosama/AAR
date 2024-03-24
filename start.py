import threading
import time
import webbrowser

import pyautogui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QInputDialog

from GameWinSet import gameWin
from tagIdentification import tagIdentify
from ui import Ui_AutoRecruit

click = [0] * 8


class Main_AutoRecruit(QtWidgets.QWidget, Ui_AutoRecruit):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.action()
        self.flag = 0
        self.FrameClass = "None"
        self.FrameTitle = "None"

    def action(self):
        self.b1.clicked.connect(self.on)
        self.b2.clicked.connect(self.off)
        self.b3.clicked.connect(self.contact)
        self.b4.clicked.connect(self.rewriteClass_botton)
        self.b5.clicked.connect(self.rewriteTitle_botton)

    # 多线程
    def on(self):
        t = threading.Thread(target=self.a, name='t')
        t.start()

    def a(self):
        self.flag = 1
        print("开始")
        gameWinflag = gameWin(self.FrameClass, self.FrameTitle)
        if gameWinflag == 0:
            self.GameState.setText("游戏未识别")
            self.GameState.setStyleSheet("background-color:yellow")
            return
        self.GameState.setStyleSheet("background-color:green")
        self.GameState.setText("游戏已识别")
        while True:
            if self.flag == 1:
                self.ProState.setStyleSheet("background-color:green")
                self.ProState.setText("程序已开始")
                for i in range(7):
                    click[i] = 0
                # 点击:开始招募干员
                pyautogui.click(300, 300, button='left')
                time.sleep(2)
                tagIdentify(click)
                print(click)
                if click[0] == -1:
                    exit(0)
                if click[0] == 1:
                    # 点击:设置9小时
                    pyautogui.click(400, 300, button='left')
                    if click[1] == 1:
                        pyautogui.click(396, 376, button='left')
                    if click[2] == 1:
                        pyautogui.click(541, 376, button='left')
                    if click[3] == 1:
                        pyautogui.click(695, 376, button='left')
                    if click[4] == 1:
                        pyautogui.click(396, 439, button='left')
                    if click[5] == 1:
                        pyautogui.click(541, 439, button='left')
                    if click[6] == 1:
                        pyautogui.click(695, 439, button='left')
                    # 点击:√
                    pyautogui.click(865, 553, button='left')
                    time.sleep(2)
                    # 点击:立即招募
                    pyautogui.click(418, 370, button='left')
                    time.sleep(2)
                    # 点击:√
                    pyautogui.click(850, 500, button='left')
                    time.sleep(2)
                    # 点击:聘用候选人
                    pyautogui.click(418, 370, button='left')
                    time.sleep(2)
                    # 点击:skip
                    pyautogui.click(1077, 78, button='left')
                    time.sleep(3)
                    # 点击:屏幕
                    pyautogui.click(418, 370, button='left')
                    continue
                if click[0] == 0:
                    # 点击:√
                    pyautogui.click(865, 553, button='left')
                    time.sleep(2)
                    # 点击:停止招募
                    pyautogui.click(151, 371, button='left')
                    time.sleep(2)
                    # 点击:停止招募
                    pyautogui.click(300, 472, button='left')
                    time.sleep(2)
                time.sleep(3)
            else:
                break
        self.ProState.setStyleSheet("background-color:red")
        self.ProState.setText("程序已停止")
        print("暂停成功!")

    def off(self):
        self.flag = 0
        print("暂停")

    def contact(self):
        webbrowser.open("https://space.bilibili.com/150504469")

    def rewriteClass_botton(self):
        text, ok = QInputDialog.getText(self, '修改Class', '请输入Class:')
        if ok:
            self.FrameClass = text
            self.ClassName.setText(text)

    def rewriteTitle_botton(self):
        text, ok = QInputDialog.getText(self, '修改Title', '请输入Title:')
        if ok:
            self.FrameTitle = text
            self.TitleName.setText(text)
