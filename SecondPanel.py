import sys

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QPushButton, QDesktopWidget, QLabel, QTableWidget, QTableWidgetItem, QFrame, \
    QAbstractItemView

from Database import Database
from SecondWindow import SecondWindow


class SecondPanel(QMainWindow, SecondWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("图像识别和相似度比较")
        self.center()
        self.database = Database()
        self.tableWidget = self.findChild(QTableWidget)

        # self.findChild(QPushButton, 'select').clicked.connect(self.select_sem_image)
        # self.findChild(QPushButton, 'analyze').clicked.connect(self.analyze)
        self.findChild(QLabel, 'SEM_image').setPixmap(QPixmap("./SEM_Image/1-a439-b-01.tif"))
        self.findChild(QLabel, 'SEM_image').setScaledContents(True)
        self.init_table_widget(self.tableWidget)

        self.findChild(QLabel, 'SEM_image_2').setPixmap(QPixmap("./SEM_Image/1-a401-b-665--24h-08.tif"))
        self.findChild(QLabel, 'SEM_image_2').setScaledContents(True)

    # def select_sem_image(self):
    #     pass
    #
    # def analyze(self):
    #     pass
    def init_table_widget(self, table):
        table.horizontalHeader().setFixedHeight(30)  ##设置表头高度
        table.horizontalHeader().setStretchLastSection(True)  ##设置最后一列拉伸至最大
        table.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置 不可选择单个单元格，只可选择一行。
        table.setColumnCount(2)  ##设置表格一共有2列
        table.setHorizontalHeaderLabels(['图片名', '相似度'])  # 设置表头文字

        row = table.rowCount()
        table.setRowCount(row + 10)
        table.setItem(0, 0, QTableWidgetItem('1-a439-b-01.tif'))
        table.setItem(0, 1, QTableWidgetItem('100.00%'))

        table.setItem(1, 0, QTableWidgetItem('1-a401-b-665--24h-08.tif'))
        table.setItem(1, 1, QTableWidgetItem('93.25%'))

        table.setItem(2, 0, QTableWidgetItem('8-a415-b-02.tif'))
        table.setItem(2, 1, QTableWidgetItem('89.29%'))

        table.setItem(3, 0, QTableWidgetItem('1-a439-b-10.tif'))
        table.setItem(3, 1, QTableWidgetItem('88.75%'))

        table.setItem(4, 0, QTableWidgetItem('9-a417-b-03.tif'))
        table.setItem(4, 1, QTableWidgetItem('88.45%'))

        table.setItem(5, 0, QTableWidgetItem('1-a439-b-07.tif'))
        table.setItem(5, 1, QTableWidgetItem('87.75%'))

        table.setItem(6, 0, QTableWidgetItem('1-a439-b-04.tif'))
        table.setItem(6, 1, QTableWidgetItem('87.29%'))

        table.setItem(7, 0, QTableWidgetItem('1-a439-b-13.tif'))
        table.setItem(7, 1, QTableWidgetItem('85.32%'))

        table.setItem(8, 0, QTableWidgetItem('1-a401-b-665--24h-05.tif'))
        table.setItem(8, 1, QTableWidgetItem('84.87%'))

        table.setItem(9, 0, QTableWidgetItem('1-a401-b-665--24h-02.tif'))
        table.setItem(9, 1, QTableWidgetItem('84.03%'))


    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        horizon = (screen.width() - size.width()) / 2
        vertical = (screen.height() - size.height()) / 2
        self.move(int(horizon), int(vertical))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    second_panel = SecondPanel()
    second_panel.show()
    sys.exit(app.exec_())
