# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'waypointstool.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 647)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(20, 10, 10, -1)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.graphicsView_pic = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_pic.setMinimumSize(QtCore.QSize(580, 420))
        self.graphicsView_pic.setObjectName("graphicsView_pic")
        self.verticalLayout_2.addWidget(self.graphicsView_pic)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setMinimumSize(QtCore.QSize(100, 30))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMinimumSize(QtCore.QSize(30, 30))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lineEdit_zero_x = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_zero_x.setMinimumSize(QtCore.QSize(60, 0))
        self.lineEdit_zero_x.setObjectName("lineEdit_zero_x")
        self.horizontalLayout_4.addWidget(self.lineEdit_zero_x)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setMinimumSize(QtCore.QSize(30, 0))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.lineEdit_zero_y = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_zero_y.setMinimumSize(QtCore.QSize(60, 0))
        self.lineEdit_zero_y.setObjectName("lineEdit_zero_y")
        self.horizontalLayout_4.addWidget(self.lineEdit_zero_y)
        self.pushButton_set_zero = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_set_zero.setMinimumSize(QtCore.QSize(70, 0))
        self.pushButton_set_zero.setObjectName("pushButton_set_zero")
        self.horizontalLayout_4.addWidget(self.pushButton_set_zero)
        self.pushButton_clear_zero = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clear_zero.setMinimumSize(QtCore.QSize(70, 0))
        self.pushButton_clear_zero.setObjectName("pushButton_clear_zero")
        self.horizontalLayout_4.addWidget(self.pushButton_clear_zero)
        self.label_xy = QtWidgets.QLabel(self.centralwidget)
        self.label_xy.setMinimumSize(QtCore.QSize(100, 30))
        self.label_xy.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_xy.setObjectName("label_xy")
        self.horizontalLayout_4.addWidget(self.label_xy)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(10, 10, 20, 0)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.pushButton_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cancel.setMinimumSize(QtCore.QSize(70, 30))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout_3.addWidget(self.pushButton_cancel)
        self.pushButton_clear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clear.setMinimumSize(QtCore.QSize(70, 30))
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.horizontalLayout_3.addWidget(self.pushButton_clear)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(30, 30))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_x = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_x.setMinimumSize(QtCore.QSize(70, 30))
        self.lineEdit_x.setObjectName("lineEdit_x")
        self.horizontalLayout.addWidget(self.lineEdit_x)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMinimumSize(QtCore.QSize(30, 0))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEdit_y = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_y.setMinimumSize(QtCore.QSize(70, 30))
        self.lineEdit_y.setObjectName("lineEdit_y")
        self.horizontalLayout.addWidget(self.lineEdit_y)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.comboBox_direction = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_direction.setMaxVisibleItems(10)
        self.comboBox_direction.setObjectName("comboBox_direction")
        self.comboBox_direction.addItem("")
        self.comboBox_direction.addItem("")
        self.comboBox_direction.addItem("")
        self.comboBox_direction.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_direction)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.comboBox_turn = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_turn.setObjectName("comboBox_turn")
        self.comboBox_turn.addItem("")
        self.comboBox_turn.addItem("")
        self.comboBox_turn.addItem("")
        self.comboBox_turn.addItem("")
        self.comboBox_turn.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_turn)
        self.comboBox_policy = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_policy.setObjectName("comboBox_policy")
        self.comboBox_policy.addItem("")
        self.comboBox_policy.addItem("")
        self.comboBox_policy.addItem("")
        self.comboBox_policy.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_policy)
        self.comboBox_brush = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_brush.setObjectName("comboBox_brush")
        self.comboBox_brush.addItem("")
        self.comboBox_brush.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_brush)
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setMinimumSize(QtCore.QSize(70, 30))
        self.pushButton_add.setObjectName("pushButton_add")
        self.horizontalLayout_2.addWidget(self.pushButton_add)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_7.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setMinimumSize(QtCore.QSize(300, 300))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 31))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_openfile = QtWidgets.QAction(MainWindow)
        self.action_openfile.setObjectName("action_openfile")
        self.action_waypoint_open = QtWidgets.QAction(MainWindow)
        self.action_waypoint_open.setObjectName("action_waypoint_open")
        self.action_waypoint_save = QtWidgets.QAction(MainWindow)
        self.action_waypoint_save.setObjectName("action_waypoint_save")
        self.action_big = QtWidgets.QAction(MainWindow)
        self.action_big.setObjectName("action_big")
        self.action_small = QtWidgets.QAction(MainWindow)
        self.action_small.setObjectName("action_small")
        self.menu.addAction(self.action_openfile)
        self.menu.addAction(self.action_waypoint_open)
        self.menu_2.addAction(self.action_waypoint_save)
        self.menu_2.addAction(self.action_big)
        self.menu_2.addAction(self.action_small)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        self.comboBox_direction.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_6.setText(_translate("MainWindow", "机器人原点："))
        self.label_4.setText(_translate("MainWindow", "X："))
        self.label_5.setText(_translate("MainWindow", "Y："))
        self.pushButton_set_zero.setText(_translate("MainWindow", "设置原点"))
        self.pushButton_clear_zero.setText(_translate("MainWindow", "清空原点"))
        self.label_xy.setText(_translate("MainWindow", "X:0  Y:0"))
        self.comboBox.setItemText(0, _translate("MainWindow", "rectangle"))
        self.comboBox.setItemText(1, _translate("MainWindow", "point"))
        self.comboBox.setItemText(2, _translate("MainWindow", "line"))
        self.pushButton.setText(_translate("MainWindow", "set"))
        self.pushButton_cancel.setText(_translate("MainWindow", "撤销"))
        self.pushButton_clear.setText(_translate("MainWindow", "清除所有点"))
        self.label_2.setText(_translate("MainWindow", "x1"))
        self.lineEdit_x.setText(_translate("MainWindow", "0"))
        self.label_3.setText(_translate("MainWindow", "Y1："))
        self.lineEdit_y.setText(_translate("MainWindow", "0"))
        self.label.setText(_translate("MainWindow", "x2"))
        self.label_7.setText(_translate("MainWindow", "y2"))
        self.comboBox_direction.setItemText(0, _translate("MainWindow", "direction     0°"))
        self.comboBox_direction.setItemText(1, _translate("MainWindow", "direction     +90°"))
        self.comboBox_direction.setItemText(2, _translate("MainWindow", "direction     -90°"))
        self.comboBox_direction.setItemText(3, _translate("MainWindow", "direction     180°"))
        self.comboBox_turn.setItemText(0, _translate("MainWindow", "直          行"))
        self.comboBox_turn.setItemText(1, _translate("MainWindow", "左转    90°"))
        self.comboBox_turn.setItemText(2, _translate("MainWindow", "左转  180°"))
        self.comboBox_turn.setItemText(3, _translate("MainWindow", "右转    90°"))
        self.comboBox_turn.setItemText(4, _translate("MainWindow", "右转  180°"))
        self.comboBox_policy.setItemText(0, _translate("MainWindow", "只能左转"))
        self.comboBox_policy.setItemText(1, _translate("MainWindow", "只能右转"))
        self.comboBox_policy.setItemText(2, _translate("MainWindow", "优先左转"))
        self.comboBox_policy.setItemText(3, _translate("MainWindow", "优先右转"))
        self.comboBox_brush.setItemText(0, _translate("MainWindow", "刷盘抬起"))
        self.comboBox_brush.setItemText(1, _translate("MainWindow", "刷盘放下"))
        self.pushButton_add.setText(_translate("MainWindow", "添加"))
        self.pushButton_2.setText(_translate("MainWindow", "OUTPUT"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "编辑"))
        self.action_openfile.setText(_translate("MainWindow", "打开地图"))
        self.action_waypoint_open.setText(_translate("MainWindow", "打开waypoints"))
        self.action_waypoint_save.setText(_translate("MainWindow", "保存waypoint"))
        self.action_big.setText(_translate("MainWindow", "放大"))
        self.action_small.setText(_translate("MainWindow", "缩小"))
