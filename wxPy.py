#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Py40 PyQt5 tutorial 

This program creates a statusbar.

author: Jan Bodnar
website: py40.com 
last edited: January 2015
"""

import sys
from PyQt5.QtWidgets import QWidget,QMainWindow, QApplication,QLabel,QLineEdit,QPushButton

from PyQt5.QtWidgets import QVBoxLayout,QHBoxLayout

def  login():
    print('presss')
class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):               
        user=QLabel("User")
        password=QLabel("PassWord")
        
        userEdit=QLineEdit()
        passwordEdit=QLineEdit()
        
        hbox=QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(user)
        hbox.addWidget(userEdit)

        hbox1=QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(password)
        hbox1.addWidget(passwordEdit)
   
        btn1 = QPushButton("login")
        btn1.clicked.connect(login)        

        vbox=QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addLayout(hbox1)
        vbox.addWidget(btn1)
        self.setLayout(vbox)
        self.setWindowTitle('LInkdood')    
        self.setGeometry(300, 300, 250, 100)
        self.show()


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())