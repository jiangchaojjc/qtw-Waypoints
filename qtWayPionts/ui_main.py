import sys
from copy import copy
from shutil import copy

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGraphicsLineItem
from pip._vendor.distlib._backport.shutil import copy

sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import cv2
sys.path.append('/opt/ros/kinetic/lib/python2.7/dist-packages')
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QAbstractItemView

import module
from settting import *
from waypointstool import Ui_MainWindow
import xlrd
import xlwt
from xlutils.copy import copy


class Manager(Ui_MainWindow):

    def __init__(self, parent:QMainWindow=None):


        self.setupUi(parent)
        self.parent=parent
        self.scene = None  # type: QtWidgets.QGraphicsScene()
        self.item = None  # type: QtWidgets.QGraphicsItem()
        self.lineitem = None  # type:  QtWidgets.QGraphicsLineItem()
        self.graphicsView_pic.wheelEvent = self.wheel_callback
        self.action_openfile.setShortcut('Ctrl+O')
        # add signal
        self.action_openfile.triggered.connect(self.open_file_callback)

        self.pushButton_set_zero.clicked.connect(self.on_set_zero)
        self.pushButton_clear_zero.clicked.connect(self.on_clear_zero)
        self.pushButton_add.clicked.connect(self.add_item_table)
        self.pushButton_cancel.clicked.connect(self.cancel_point)
        self.pushButton_clear.clicked.connect(self.clear_points)
        self.pushButton_2.clicked.connect(self.output_data)

        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(100)

        self.tableWidget.verticalHeader().setVisible(False)
        # self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.line_cnt = 0

        self.zoom_level = 1
        self.zero_x = None
        self.zero_y = None
        self.input_x = 0
        self.input_y = 0
        self.add_x = 0
        self.add_y = 0
        self.direction = 0
        self.two_points = []
        self.last_points=[]
        self.rectanglepoints= []
        self.resolution = 0.05
        self.flag =0
        self.flag1 = 0
        self.index=0
        self.__init_config()
        self.linelist = []
        self.linepoints =[]
        self.set_title()

        self.scene = QtWidgets.QGraphicsScene()
        self.graphicsView_pic.setScene(self.scene)
        self.initUI()

        # self.painter = QPainter(parent)
        # self.painter.begin(parent)
        # self.painter.setPen(Qt.red)
        # self.painter.drawRect(0, 0, 10, 10)
        # self.painter.end()
    def initUI(self):
        self.parent.setWindowTitle('drawrect')
        self.parent.show()

    def set_title(self):
        self.line_cnt = 0
        self.tableWidget.setHorizontalHeaderLabels(['序号', 'X坐标', 'Y坐标', 'status', 'action', '策略', '刷盘'])

    def add_item_table(self):
        if self.comboBox.currentText() == 'line':

            self.tableWidget.setItem(self.line_cnt, 0, QtWidgets.QTableWidgetItem(str(self.line_cnt)))
            self.tableWidget.setItem(self.line_cnt, 1, QtWidgets.QTableWidgetItem(self.lineEdit_x.text()))
            self.tableWidget.setItem(self.line_cnt, 2, QtWidgets.QTableWidgetItem(self.lineEdit_y.text()))
            self.tableWidget.setItem(self.line_cnt, 3, QtWidgets.QTableWidgetItem(
                str(action_relations[self.comboBox_direction.currentText()])))
            self.tableWidget.setItem(self.line_cnt, 4, QtWidgets.QTableWidgetItem(
                str(action_relations[self.comboBox_turn.currentText()])))
            self.tableWidget.setItem(self.line_cnt, 5, QtWidgets.QTableWidgetItem(
                str(action_relations[self.comboBox_policy.currentText()])))
            self.tableWidget.setItem(self.line_cnt, 6, QtWidgets.QTableWidgetItem(
                str(action_relations[self.comboBox_brush.currentText()])))
            self.line_cnt += 1
            self.comboBox.setEnabled(False)
            self.flag1 = self.flag1 + 1
            self.linepoints.append((self.lineEdit_x.text(),self.lineEdit_y.text(),str(action_relations[self.comboBox_direction.currentText()]),str(action_relations[self.comboBox_turn.currentText()]),'0','0'))
            if self.flag1 == 2:
                self.comboBox.setEnabled(True)
                self.flag1 = 0
                self.paint(self.linepoints)
                self.linepoints.clear()

        elif self.comboBox.currentText() == 'point':
            self.tableWidget.setItem(self.line_cnt, 0, QtWidgets.QTableWidgetItem(str(self.line_cnt)))
            self.tableWidget.setItem(self.line_cnt, 1, QtWidgets.QTableWidgetItem(self.lineEdit_x.text()))
            self.tableWidget.setItem(self.line_cnt, 2, QtWidgets.QTableWidgetItem(self.lineEdit_y.text()))
            self.tableWidget.setItem(self.line_cnt, 3, QtWidgets.QTableWidgetItem(
                str(action_relations[self.comboBox_direction.currentText()])))
            self.tableWidget.setItem(self.line_cnt, 4, QtWidgets.QTableWidgetItem(
                str(action_relations[self.comboBox_turn.currentText()])))
            self.tableWidget.setItem(self.line_cnt, 5, QtWidgets.QTableWidgetItem(
                str(action_relations[self.comboBox_policy.currentText()])))
            self.tableWidget.setItem(self.line_cnt, 6, QtWidgets.QTableWidgetItem(
                str(action_relations[self.comboBox_brush.currentText()])))
            self.line_cnt += 1


        elif self.comboBox.currentText() == 'rectangle' and self.flag != 1:
            self.add_x = self.lineEdit_x.text()
            self.add_y = self.lineEdit_y.text()
            self.direction = str(action_relations[self.comboBox_direction.currentText()])
            self.action = str(action_relations[self.comboBox_turn.currentText()])
            self.two_points.append((self.add_x, self.add_y, self.direction,self.action))
            self.tableWidget.setItem(self.line_cnt, 0, QtWidgets.QTableWidgetItem(str(self.line_cnt)))
            self.tableWidget.setItem(self.line_cnt, 1, QtWidgets.QTableWidgetItem(self.lineEdit_x.text()))
            self.tableWidget.setItem(self.line_cnt, 2, QtWidgets.QTableWidgetItem(self.lineEdit_y.text()))
            self.tableWidget.setItem(self.line_cnt, 3, QtWidgets.QTableWidgetItem(
                str(action_relations[self.comboBox_direction.currentText()])))
            self.tableWidget.setItem(self.line_cnt, 4, QtWidgets.QTableWidgetItem(
                str(action_relations[self.comboBox_turn.currentText()])))
            self.tableWidget.setItem(self.line_cnt, 5, QtWidgets.QTableWidgetItem(
                str(action_relations[self.comboBox_policy.currentText()])))
            self.tableWidget.setItem(self.line_cnt, 6, QtWidgets.QTableWidgetItem(
                str(action_relations[self.comboBox_brush.currentText()])))
            self.line_cnt += 1
            self.comboBox.setEnabled(False)
            self.flag += 1
            self.rectanglepoints.append((self.add_x, self.add_y, self.direction,self.action,'0','0'))
        else:
            self.add_x = self.lineEdit_x.text()
            self.add_y = self.lineEdit_y.text()
            self.direction = str(action_relations[self.comboBox_direction.currentText()])
            self.action = str(action_relations[self.comboBox_turn.currentText()])
            self.two_points.append((self.add_x, self.add_y, self.direction, self.action))
            rectangle_points = module.points_in_rectangle(self.two_points)
            for n in range(len(rectangle_points)):
                self.tableWidget.setItem(self.line_cnt, 0, QtWidgets.QTableWidgetItem(str(self.line_cnt)))
                self.tableWidget.setItem(self.line_cnt, 1, QtWidgets.QTableWidgetItem(rectangle_points[n][0]))
                self.tableWidget.setItem(self.line_cnt, 2, QtWidgets.QTableWidgetItem(rectangle_points[n][1]))
                self.tableWidget.setItem(self.line_cnt, 3, QtWidgets.QTableWidgetItem(rectangle_points[n][2]))
                self.tableWidget.setItem(self.line_cnt, 4, QtWidgets.QTableWidgetItem(rectangle_points[n][3]))
                self.tableWidget.setItem(self.line_cnt, 5, QtWidgets.QTableWidgetItem(rectangle_points[n][4]))
                self.tableWidget.setItem(self.line_cnt, 6, QtWidgets.QTableWidgetItem(rectangle_points[n][5]))
                self.line_cnt += 1

            self.flag = 0
            # self.line_cnt += 1
            self.two_points.clear()
            self.comboBox.setEnabled(True)
            for item in rectangle_points:
                self.rectanglepoints.append(item)
            self.paint(self.rectanglepoints)
            self.rectanglepoints.clear()

    def __init_config(self):
        self.pushButton_clear_zero.setEnabled(False)

    def on_clear_zero(self):
        self.lineEdit_zero_x.setEnabled(True)
        self.lineEdit_zero_y.setEnabled(True)
        self.zero_x = None
        self.zero_y = None
        self.lineEdit_zero_x.setText('')
        self.lineEdit_zero_y.setText('')
        self.pushButton_clear_zero.setEnabled(False)
        self.pushButton_set_zero.setEnabled(True)

    def on_set_zero(self):
        self.lineEdit_zero_x.setEnabled(False)
        self.lineEdit_zero_y.setEnabled(False)
        self.zero_x = float(self.lineEdit_zero_x.text())
        self.zero_y = float(float(self.lineEdit_zero_y.text()))
        self.pushButton_clear_zero.setEnabled(True)
        self.pushButton_set_zero.setEnabled(False)
        self.last_points.append((float((self.zero_x)*20),float((self.zero_y)*20*(-1))))

    def add_point(self):
        if self.zero_x is not None and self.zero_y is not None:
            self.lineEdit_x.setText(str(round((self.input_x - self.zero_x),2)))
            self.lineEdit_y.setText(str(round((self.input_y - self.zero_y),2)))

    def cancel_point(self):
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        row_select = self.tableWidget.selectedItems()
        if len(row_select) == 0:
            return
        self.row = row_select[0].row()
        #print(self.row)
        self.tableWidget.removeRow(self.row)
        self.updatepoint()
        if self.flag == 1:
            self.two_points.pop()
            self.flag = 0
            self.comboBox.setEnabled(True)
        elif self.flag1 == 1:
            self.comboBox.setEnabled(True)
            self.flag1=0

    def updatepoint(self):
        for n in range(self.line_cnt-self.row):
            self.tableWidget.setItem(int(self.row)+n, 0, QtWidgets.QTableWidgetItem(str(int(self.row)+n)))
        self.tableWidget.removeRow(self.line_cnt)
        self.line_cnt = self.line_cnt - 1

    def clear_points(self):
        self.flag = 0
        self.tableWidget.clear()
        self.set_title()
        self.two_points.clear()
    def set_label_xy_show(self):
        str_show = 'X:' + str(self.input_x) + '  ' + 'Y:' + str(self.input_y)
        self.label_xy.setText(str_show)

    def set_line_zero_show(self):
        if self.lineEdit_zero_x.isEnabled() and self.lineEdit_zero_y.isEnabled():
            self.lineEdit_zero_x.setText(str(self.input_x))
            self.lineEdit_zero_y.setText(str(self.input_y))
    def mouse_press_callback(self, event:QtWidgets.QGraphicsSceneMouseEvent):

        self.input_x = round((event.pos().x() * self.resolution), 2)
        self.input_y = round((event.pos().y() * (-1) * self.resolution), 2)

        self.set_label_xy_show()
        self.set_line_zero_show()
        self.add_point()
        self.last_points.append((int(event.pos().x()), int(event.pos().y())))
        #print(len(self.last_points))
        # if ((len(self.last_points) % 2) == 0) and (len(self.last_points) != 0):
        #     self.paint(self.last_points)


    def wheel_callback(self, event: QtGui.QWheelEvent):
        self.zoom_level += (event.angleDelta().y())/(abs(event.angleDelta().y())) * 0.05
        if self.zoom_level < 0.05:
            self.zoom_level = 0.05

        if self.zoom_level > 10:
            self.zoom_level = 10

        self.update_zoom_level()

    def update_zoom_level(self):
        if self.item is not None:
            self.item.setScale(self.zoom_level)
            for n in range(len(self.linelist)):
                self.linelist[n].setScale(self.zoom_level)
        else:
            print('please input img')

    def open_file_callback(self):
        filename_choose, file_type = QtWidgets.QFileDialog.getOpenFileName(None, '选取文件', './',
                                                                           'All Files (*);;Pic Files (*.png)')

        if filename_choose == "":
            print("\n取消选择")
            return
        self.img = cv2.imread(filename_choose)
        self.img_x = self.img.shape[1] * self.resolution
        self.img_y = self.img.shape[0] * self.resolution
        #print(self.img_x,self.img_y)
        pixmap = QtGui.QPixmap(filename_choose)
        self.item = QtWidgets.QGraphicsPixmapItem(pixmap)
        #self.item.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable)
        self.line = QGraphicsLineItem()
        self.scene.addItem(self.item)

        self.item.mouseDoubleClickEvent = self.mouse_press_callback

        self.zoom_level = 1
        self.tableWidget.clear()
        self.set_title()

    def paint(self, p):
        # self.item1.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable)
        for n in range(int(len(p))-1):
            x0 = int((float(p[n][0])+float(self.zero_x))/self.resolution)
            x1 = int((float(p[n][1])+float(self.zero_y))/self.resolution*(-1))
            y0 = int((float(p[n+1][0])+float(self.zero_x))/self.resolution)
            y1 = int((float(p[n+1][1])+float(self.zero_y))/self.resolution*(-1))
            self.lineitem = QGraphicsLineItem()
            self.lineitem.setPen(Qt.red)
            self.lineitem.setLine(x0, x1, y0, y1)
            self.linelist.append(self.lineitem)
            self.scene.addItem(self.lineitem)

    def output_data(self):
        oldWb = xlrd.open_workbook('/home/utryjc/databag/021904.xls', formatting_info=True)
        borders = xlwt.Borders()
        borders.left = 1
        borders.right = 1
        borders.top = 1
        borders.bottom = 1
        style = xlwt.XFStyle() #chushi hua yangshi
        style.borders = borders
        newWb = copy(oldWb)
        newWs = newWb.get_sheet(0)
        rows = self.tableWidget.rowCount()
        for i in range(rows):
            mainList = []
            for j in range(7):
                try:
                    data = self.tableWidget.item(i, j).text()
                    mainList.append(data)
                except:
                    data = ''
                    mainList.append(data)
                newWs.write(i, j, mainList[j], style)
        newWb.save('/home/utryjc/databag/021904.xls')







if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = QtWidgets.QMainWindow()
    manager = Manager(window)
    window.show()
    app.exec_()
