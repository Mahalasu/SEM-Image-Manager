import os

from PyQt5.QtWidgets import QDialog, QComboBox, QSplitter, QLineEdit, QDialogButtonBox, QPushButton, QFileDialog

from FileInfo import FileInfo
from InsertDialog import InsertDialog


class InsertPanel(QDialog, InsertDialog):

    def __init__(self, metallographics, database):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('插入图片')
        self.file_info = FileInfo()
        self.cwd = os.getcwd()
        self.database = database

        names = ['-----请选择图片包含的组织-----'] + [row[0] for row in metallographics]
        self.comboBox = self.findChild(QComboBox)
        self.comboBox.addItems(names)

        self.buttonBox = self.findChild(QDialogButtonBox)
        self.buttonBox.accepted.connect(self.insert)
        self.buttonBox.button(QDialogButtonBox.Reset).clicked.connect(self.reset)

        self.findChild(QPushButton, 'SEMImage').clicked.connect(self.select_sem_image)
        self.findChild(QPushButton, 'craftImage').clicked.connect(self.select_crafts_image)
        self.findChild(QPushButton, 'forceImage').clicked.connect(self.select_force_image)
        self.findChild(QPushButton, 'barkImage').clicked.connect(self.select_bark_image)

        for splitter in self.findChildren(QSplitter):
            if splitter.handle(1):
                splitter.handle(1).setDisabled(True)

    def reset(self):
        line_edits = self.findChildren(QLineEdit)
        for each in line_edits:
            each.clear()
        self.file_info.reset()
        self.comboBox.setCurrentIndex(0)

    def insert(self):
        name = self.findChild(QLineEdit, 'name_insert').text()
        temp = self.findChild(QLineEdit, 'temp_insert').text()
        time = self.findChild(QLineEdit, 'time_insert').text()
        amp_factor = self.findChild(QLineEdit, 'amp_factor_insert').text()
        craft = self.findChild(QLineEdit, 'craft_insert').text()
        no = self.findChild(QLineEdit, 'no_insert').text()
        content = self.findChild(QLineEdit, 'content_insert').text()
        mid = self.comboBox.currentIndex()

        self.database.insert(name, temp, time, amp_factor, craft, no, content, mid, self.file_info)

    def select_sem_image(self):
        file_name = QFileDialog.getOpenFileName(self, "选取文件", self.cwd, "Image files(*.jpg *.png *tif)")[0]
        self.findChild(QLineEdit, 'info_SEMImage_insert').setText(file_name.split('/')[-1])
        self.findChild(QLineEdit, 'info_SEMImage_insert').setCursorPosition(0)
        self.file_info.image_path = file_name

    def select_crafts_image(self):
        file_name = QFileDialog.getOpenFileName(self, "选取文件", self.cwd, "Image files(*.jpg *.png *tif)")[0]
        self.findChild(QLineEdit, 'info_craftImage_insert').setText(file_name.split('/')[-1])
        self.findChild(QLineEdit, 'info_craftImage_insert').setCursorPosition(0)
        self.file_info.craft_image_path = file_name

    def select_force_image(self):
        file_name = QFileDialog.getOpenFileName(self, "选取文件", self.cwd, "Image files(*.jpg *.png *tif)")[0]
        self.findChild(QLineEdit, 'info_forceImage_insert').setText(file_name.split('/')[-1])
        self.findChild(QLineEdit, 'info_forceImage_insert').setCursorPosition(0)
        self.file_info.force_image_path = file_name

    def select_bark_image(self):
        file_name = QFileDialog.getOpenFileName(self, "选取文件", self.cwd, "Image files(*.jpg *.png *tif)")[0]
        self.findChild(QLineEdit, 'info_barkImage_insert').setText(file_name.split('/')[-1])
        self.findChild(QLineEdit, 'info_barkImage_insert').setCursorPosition(0)
        self.file_info.bark_image_path = file_name
