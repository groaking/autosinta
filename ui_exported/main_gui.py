# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/ssynthesia/ghostcity/git/codename-autosinta/src/autosinta/ui/main_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(511, 518)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title_app = QtWidgets.QLabel(self.centralwidget)
        self.title_app.setGeometry(QtCore.QRect(20, 10, 471, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.title_app.setFont(font)
        self.title_app.setObjectName("title_app")
        self.frame_av = QtWidgets.QFrame(self.centralwidget)
        self.frame_av.setGeometry(QtCore.QRect(20, 50, 471, 61))
        self.frame_av.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_av.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_av.setObjectName("frame_av")
        self.title_av = QtWidgets.QLabel(self.frame_av)
        self.title_av.setGeometry(QtCore.QRect(10, 0, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.title_av.setFont(font)
        self.title_av.setObjectName("title_av")
        self.title_avpass = QtWidgets.QLabel(self.frame_av)
        self.title_avpass.setGeometry(QtCore.QRect(240, 30, 61, 17))
        self.title_avpass.setObjectName("title_avpass")
        self.title_avuser = QtWidgets.QLabel(self.frame_av)
        self.title_avuser.setGeometry(QtCore.QRect(10, 30, 61, 17))
        self.title_avuser.setObjectName("title_avuser")
        self.input_avuser = QtWidgets.QLineEdit(self.frame_av)
        self.input_avuser.setGeometry(QtCore.QRect(80, 30, 151, 25))
        self.input_avuser.setObjectName("input_avuser")
        self.input_avpass = QtWidgets.QLineEdit(self.frame_av)
        self.input_avpass.setGeometry(QtCore.QRect(300, 30, 151, 25))
        self.input_avpass.setInputMask("")
        self.input_avpass.setText("")
        self.input_avpass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_avpass.setObjectName("input_avpass")
        self.frame_sync = QtWidgets.QFrame(self.centralwidget)
        self.frame_sync.setGeometry(QtCore.QRect(20, 120, 471, 61))
        self.frame_sync.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_sync.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_sync.setObjectName("frame_sync")
        self.title_syncopt = QtWidgets.QLabel(self.frame_sync)
        self.title_syncopt.setGeometry(QtCore.QRect(10, 0, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.title_syncopt.setFont(font)
        self.title_syncopt.setObjectName("title_syncopt")
        self.select_scopus = QtWidgets.QCheckBox(self.frame_sync)
        self.select_scopus.setGeometry(QtCore.QRect(10, 30, 82, 23))
        self.select_scopus.setChecked(True)
        self.select_scopus.setObjectName("select_scopus")
        self.select_wos = QtWidgets.QCheckBox(self.frame_sync)
        self.select_wos.setGeometry(QtCore.QRect(90, 30, 111, 23))
        self.select_wos.setChecked(False)
        self.select_wos.setObjectName("select_wos")
        self.select_garuda = QtWidgets.QCheckBox(self.frame_sync)
        self.select_garuda.setGeometry(QtCore.QRect(210, 30, 71, 23))
        self.select_garuda.setChecked(False)
        self.select_garuda.setObjectName("select_garuda")
        self.select_gs = QtWidgets.QCheckBox(self.frame_sync)
        self.select_gs.setGeometry(QtCore.QRect(290, 30, 111, 23))
        self.select_gs.setChecked(False)
        self.select_gs.setObjectName("select_gs")
        self.btn_login = QtWidgets.QPushButton(self.centralwidget)
        self.btn_login.setGeometry(QtCore.QRect(170, 190, 121, 25))
        self.btn_login.setObjectName("btn_login")
        self.btn_exportauthor = QtWidgets.QPushButton(self.centralwidget)
        self.btn_exportauthor.setGeometry(QtCore.QRect(300, 190, 111, 25))
        self.btn_exportauthor.setObjectName("btn_exportauthor")
        self.btn_sync = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sync.setGeometry(QtCore.QRect(420, 190, 71, 25))
        self.btn_sync.setObjectName("btn_sync")
        self.frame_log = QtWidgets.QFrame(self.centralwidget)
        self.frame_log.setGeometry(QtCore.QRect(20, 230, 471, 251))
        self.frame_log.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_log.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_log.setObjectName("frame_log")
        self.progress_sync = QtWidgets.QProgressBar(self.frame_log)
        self.progress_sync.setGeometry(QtCore.QRect(10, 30, 451, 23))
        self.progress_sync.setProperty("value", 0)
        self.progress_sync.setObjectName("progress_sync")
        self.title_syncprog = QtWidgets.QLabel(self.frame_log)
        self.title_syncprog.setGeometry(QtCore.QRect(10, 0, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.title_syncprog.setFont(font)
        self.title_syncprog.setObjectName("title_syncprog")
        self.area_message = QtWidgets.QPlainTextEdit(self.frame_log)
        self.area_message.setGeometry(QtCore.QRect(10, 90, 451, 151))
        self.area_message.setReadOnly(True)
        self.area_message.setObjectName("area_message")
        self.title_message = QtWidgets.QLabel(self.frame_log)
        self.title_message.setGeometry(QtCore.QRect(10, 60, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.title_message.setFont(font)
        self.title_message.setObjectName("title_message")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 511, 22))
        self.menubar.setObjectName("menubar")
        self.menu_help = QtWidgets.QMenu(self.menubar)
        self.menu_help.setObjectName("menu_help")
        self.menu_about = QtWidgets.QMenu(self.menubar)
        self.menu_about.setObjectName("menu_about")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        MainWindow.setMenuBar(self.menubar)
        self.action_howto = QtWidgets.QAction(MainWindow)
        self.action_howto.setObjectName("action_howto")
        self.action_about = QtWidgets.QAction(MainWindow)
        self.action_about.setObjectName("action_about")
        self.action_license = QtWidgets.QAction(MainWindow)
        self.action_license.setObjectName("action_license")
        self.action_quit = QtWidgets.QAction(MainWindow)
        self.action_quit.setObjectName("action_quit")
        self.action_troubleshooting = QtWidgets.QAction(MainWindow)
        self.action_troubleshooting.setObjectName("action_troubleshooting")
        self.action_changelog = QtWidgets.QAction(MainWindow)
        self.action_changelog.setObjectName("action_changelog")
        self.menu_help.addAction(self.action_howto)
        self.menu_help.addAction(self.action_troubleshooting)
        self.menu_about.addAction(self.action_about)
        self.menu_about.addAction(self.action_changelog)
        self.menu_about.addAction(self.action_license)
        self.menu_file.addAction(self.action_quit)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())
        self.menubar.addAction(self.menu_about.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AutoSINTA Publication Syncer"))
        self.title_app.setText(_translate("MainWindow", "AutoSINTA Publication Syncer"))
        self.title_av.setText(_translate("MainWindow", "Author Verificator Credential"))
        self.title_avpass.setText(_translate("MainWindow", "Password"))
        self.title_avuser.setText(_translate("MainWindow", "Username"))
        self.title_syncopt.setText(_translate("MainWindow", "Synchronization Options"))
        self.select_scopus.setText(_translate("MainWindow", "Scopus"))
        self.select_wos.setText(_translate("MainWindow", "Web of Science"))
        self.select_garuda.setText(_translate("MainWindow", "Garuda"))
        self.select_gs.setText(_translate("MainWindow", "Google Scholar"))
        self.btn_login.setText(_translate("MainWindow", "Verificator Login"))
        self.btn_exportauthor.setText(_translate("MainWindow", "Load Author List"))
        self.btn_sync.setText(_translate("MainWindow", "Sync"))
        self.title_syncprog.setText(_translate("MainWindow", "Synchronization Progress"))
        self.title_message.setText(_translate("MainWindow", "Message"))
        self.menu_help.setTitle(_translate("MainWindow", "Help"))
        self.menu_about.setTitle(_translate("MainWindow", "About"))
        self.menu_file.setTitle(_translate("MainWindow", "File"))
        self.action_howto.setText(_translate("MainWindow", "How to use the app ..."))
        self.action_about.setText(_translate("MainWindow", "About AutoSINTA"))
        self.action_license.setText(_translate("MainWindow", "License"))
        self.action_quit.setText(_translate("MainWindow", "Quit"))
        self.action_troubleshooting.setText(_translate("MainWindow", "Troubleshooting ..."))
        self.action_changelog.setText(_translate("MainWindow", "Changelog"))
