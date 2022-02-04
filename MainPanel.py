from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QPixmap, QRegExpValidator
from PyQt5.QtWidgets import QMainWindow, QListWidgetItem, QListWidget, QPushButton, QLabel, QSplitter, QLineEdit, \
    QWidget, QDesktopWidget, QMessageBox
from MainWindow import Main_Window


class MainPanel(QMainWindow, Main_Window):

    def __init__(self, database):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("SEMImageManager")
        self.center()
        self.database = database

        # self.modify_panel = ModifyPanel(metallographics)
        self.findChild(QPushButton, 'searchImage').clicked.connect(self.search)
        self.findChild(QPushButton, 'deleteImage').clicked.connect(self.delete)
        self.findChild(QPushButton, 'resetImage').clicked.connect(self.reset)

        validator = QRegExpValidator(QRegExp("^\d+(\.\d+)?$"))
        validator_amp = QRegExpValidator(QRegExp("^-?\d+$"))
        self.findChild(QLineEdit, 'temp').setValidator(validator)
        self.findChild(QLineEdit, 'time').setValidator(validator)
        self.findChild(QLineEdit, 'amp_factor').setValidator(validator_amp)

        self.list_widget = self.findChild(QListWidget)
        self.init_list_widget(self.list_widget)

        for splitter in self.findChildren(QSplitter):
            if splitter.handle(1):
                splitter.handle(1).setDisabled(True)

        self.statusbar.showMessage("请选择右上角的图片查看信息或者进行删除和修改操作！")

    # make the window center
    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        horizon = (screen.width() - size.width()) / 2
        vertical = (screen.height() - size.height()) / 2
        self.move(int(horizon), int(vertical))

    # Init the ListWidget
    def init_list_widget(self, list_widget):
        list_widget.clear()
        rows = self.database.get_all_rows()
        for row in rows:
            name = row[0]
            list_widget.addItem(QListWidgetItem(name))
        list_widget.sortItems()
        list_widget.setCurrentRow(0)
        self.show_info()
        list_widget.itemClicked.connect(self.show_info)

    # Get selected image's information
    def fetch_info(self):
        item_name = self.list_widget.currentItem().text()
        image_info = self.database.search_info(item_name)
        return image_info

    # Show image's info when clicked an item
    def show_info(self):
        result = self.fetch_info()
        image_path = result[8]
        self.findChild(QLabel, 'SEM_image').setPixmap(QPixmap(image_path))

        craft_image_path = result[9]
        if craft_image_path:
            self.findChild(QLabel, 'craft_image').setPixmap(QPixmap(craft_image_path))
        else:
            self.findChild(QLabel, 'craft_image').setPixmap(
                QPixmap('./SEM_Image/none.jpg'))

        force_image_path = result[10]
        if force_image_path:
            self.findChild(QLabel, 'force_image').setPixmap(QPixmap(force_image_path))
        else:
            self.findChild(QLabel, 'force_image').setPixmap(
                QPixmap('./SEM_Image/none.jpg'))

        bark_image_path = result[11]
        if bark_image_path:
            self.findChild(QLabel, 'bark_image').setPixmap(QPixmap(bark_image_path))
        else:
            self.findChild(QLabel, 'bark_image').setPixmap(
                QPixmap('./SEM_Image/none.jpg'))

        self.findChild(QLabel, 'SEM_image').setScaledContents(True)
        self.findChild(QLabel, 'craft_image').setScaledContents(True)
        self.findChild(QLabel, 'force_image').setScaledContents(True)
        self.findChild(QLabel, 'bark_image').setScaledContents(True)

        metal = self.database.search_metal(result[1])
        self.findChild(QLineEdit, 'metal_info').setText(metal)
        temp = str(result[2])
        self.findChild(QLineEdit, 'temp_info').setText(temp)
        time = str(result[3])
        self.findChild(QLineEdit, 'time_info').setText(time)
        craft = result[4]
        self.findChild(QLineEdit, 'craft_info').setText(craft)
        amp_factor = str(result[5])
        self.findChild(QLineEdit, 'amp_info').setText(amp_factor)
        no = result[6]
        self.findChild(QLineEdit, 'no_info').setText(no)
        content = result[7]
        self.findChild(QLineEdit, 'content_info').setText(content)
        self.findChild(QLineEdit, 'content_info').setCursorPosition(0)
        update_time = str(result[-1])
        self.findChild(QLineEdit, 'update_info').setText(update_time)

    # Search the image's name and show on the ListWidget
    def search(self):
        temp = self.findChild(QLineEdit, "temp").text()
        time = self.findChild(QLineEdit, "time").text()
        crafts = self.findChild(QLineEdit, "crafts").text()
        amp_factor = self.findChild(QLineEdit, "amp_factor").text()
        if not (temp or time or crafts or amp_factor):
            msg_box = QMessageBox(QMessageBox.Warning, "警告", "请输入至少一条筛选条件！")
            msg_box.exec_()
            return
        self.findChild(QListWidget).clear()
        result = self.database.search_image(temp, time, crafts, amp_factor)
        for row in result:
            QListWidgetItem(row[0], self.findChild(QListWidget))

    # reset main panel when clicked reset
    def reset(self):
        self.init_list_widget(self.list_widget)
        self.show_info()

        inputs = self.findChild(QWidget, 'search_input').findChildren(QLineEdit)
        for inputted in inputs:
            inputted.clear()

    # delete an image
    def delete(self):
        selected = self.fetch_info()
        self.database.delete(selected)
        self.reset()
