import os

from PyQt5.QtWidgets import QDialog, QComboBox, QSplitter, QLineEdit, QDialogButtonBox, QPushButton, QFileDialog

from FileInfo import FileInfo
from ModifyDialog import ModifyDialog

SEM_IMAGE_DIRECTORY_PATH = './SEM_Image'
CRAFTS_IMAGE_DIRECTORY_PATH = './Crafts_Image'
FORCE_IMAGE_DIRECTORY_PATH = './Force_Image'
BARK_IMAGE_DIRECTORY_PATH = './Bark_Image'


class ModifyPanel(QDialog, ModifyDialog):

    def __init__(self, metallographics, database, image_info):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('修改图片信息')
        self.file_info = FileInfo()
        self.image_info = image_info
        self.cwd = os.getcwd()
        self.database = database

        """init combo box"""
        names = ['-----请选择图片包含的组织-----'] + [row[0] for row in metallographics]
        self.comboBox = self.findChild(QComboBox)
        self.comboBox.addItems(names)

        self.buttonBox = self.findChild(QDialogButtonBox)
        self.buttonBox.accepted.connect(self.modify)

        self.findChild(QPushButton, 'SEMImage').clicked.connect(self.select_sem_image)
        self.findChild(QPushButton, 'craftImage').clicked.connect(self.select_crafts_image)
        self.findChild(QPushButton, 'forceImage').clicked.connect(self.select_force_image)
        self.findChild(QPushButton, 'barkImage').clicked.connect(self.select_bark_image)

        for splitter in self.findChildren(QSplitter):
            if splitter.handle(1):
                splitter.handle(1).setDisabled(True)

        self.setup(image_info)

    def setup(self, image_info):
        self.findChild(QLineEdit, 'name').setText(image_info[0])
        self.comboBox.setCurrentIndex(image_info[1])
        self.findChild(QLineEdit, 'temp').setText(str(image_info[2]))
        self.findChild(QLineEdit, 'time').setText(str(image_info[3]))
        self.findChild(QLineEdit, 'craft').setText(image_info[4])
        self.findChild(QLineEdit, 'amp_factor').setText(str(image_info[5]))
        self.findChild(QLineEdit, 'no').setText(image_info[6])
        self.findChild(QLineEdit, 'content').setText(image_info[7])

        self.file_info.image_path = image_info[8]
        image_path = image_info[8].split('/')[-1]
        self.findChild(QLineEdit, 'info_SEMImage').setText(image_path)

        self.file_info.craft_image_path = image_info[9]
        craft_image_path = image_info[9].split('/')[-1] if image_info[9] else ''
        self.findChild(QLineEdit, 'info_craftImage').setText(craft_image_path)

        self.file_info.craft_image_path = image_info[10]
        force_image_path = image_info[10].split('/')[-1] if image_info[10] else ''
        self.findChild(QLineEdit, 'info_forceImage').setText(force_image_path)

        self.file_info.bark_image_path = image_info[11]
        bark_image_path = image_info[11].split('/')[-1] if image_info[11] else ''
        self.findChild(QLineEdit, 'info_barkImage').setText(bark_image_path)

        for line_edit in self.findChildren(QLineEdit):
            line_edit.setCursorPosition(0)

    def modify(self):
        name = self.findChild(QLineEdit, 'name').text()
        temp = self.findChild(QLineEdit, 'temp').text()
        time = self.findChild(QLineEdit, 'time').text()
        amp_factor = self.findChild(QLineEdit, 'amp_factor').text()
        craft = self.findChild(QLineEdit, 'craft').text()
        no = self.findChild(QLineEdit, 'no').text()
        content = self.findChild(QLineEdit, 'content').text()
        mid = self.comboBox.currentIndex()

        self.database.modify(name, temp, time, amp_factor, craft, no, content, mid, self.file_info, self.image_info)

    def select_sem_image(self):
        file_name = QFileDialog.getOpenFileName(self, "选取文件", self.cwd, "Image files(*.jpg *.png *tif)")[0]
        self.findChild(QLineEdit, 'info_SEMImage').setText(file_name.split('/')[-1])
        self.file_info.image_path = file_name

    def select_crafts_image(self):
        file_name = QFileDialog.getOpenFileName(self, "选取文件", self.cwd, "Image files(*.jpg *.png *tif)")[0]
        self.findChild(QLineEdit, 'info_craftImage').setText(file_name.split('/')[-1])
        self.file_info.craft_image_path = file_name

    def select_force_image(self):
        file_name = QFileDialog.getOpenFileName(self, "选取文件", self.cwd, "Image files(*.jpg *.png *tif)")[0]
        self.findChild(QLineEdit, 'info_forceImage').setText(file_name.split('/')[-1])
        self.file_info.force_image_path = file_name

    def select_bark_image(self):
        file_name = QFileDialog.getOpenFileName(self, "选取文件", self.cwd, "Image files(*.jpg *.png *tif)")[0]
        self.findChild(QLineEdit, 'info_barkImage').setText(file_name.split('/')[-1])
        self.file_info.bark_image_path = file_name
