# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Main_Window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 850)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1100, 850))
        MainWindow.setMaximumSize(QtCore.QSize(1100, 850))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1100, 0))
        self.centralwidget.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.images = QtWidgets.QWidget(self.centralwidget)
        self.images.setMinimumSize(QtCore.QSize(710, 780))
        self.images.setMaximumSize(QtCore.QSize(710, 780))
        self.images.setStyleSheet("QWidget #images {\n"
"    border-width: 5px; \n"
"    border-style: solid;\n"
"    border-color: #00afb9;\n"
"    border-radius: 15px;\n"
"}")
        self.images.setObjectName("images")
        self.gridLayout = QtWidgets.QGridLayout(self.images)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter_5 = QtWidgets.QSplitter(self.images)
        self.splitter_5.setMinimumSize(QtCore.QSize(0, 330))
        self.splitter_5.setMaximumSize(QtCore.QSize(320, 337))
        self.splitter_5.setOrientation(QtCore.Qt.Vertical)
        self.splitter_5.setObjectName("splitter_5")
        self.bark_image = QtWidgets.QLabel(self.splitter_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bark_image.sizePolicy().hasHeightForWidth())
        self.bark_image.setSizePolicy(sizePolicy)
        self.bark_image.setMinimumSize(QtCore.QSize(320, 300))
        self.bark_image.setMaximumSize(QtCore.QSize(320, 300))
        self.bark_image.setStyleSheet("url (\':/fig/bak.jpg\')")
        self.bark_image.setFrameShape(QtWidgets.QFrame.Box)
        self.bark_image.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.bark_image.setText("")
        self.bark_image.setScaledContents(False)
        self.bark_image.setObjectName("bark_image")
        self.label_8 = QtWidgets.QLabel(self.splitter_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QtCore.QSize(320, 30))
        self.label_8.setMaximumSize(QtCore.QSize(320, 30))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.splitter_5, 1, 2, 1, 1)
        self.splitter_3 = QtWidgets.QSplitter(self.images)
        self.splitter_3.setMinimumSize(QtCore.QSize(0, 330))
        self.splitter_3.setMaximumSize(QtCore.QSize(320, 337))
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.craft_image = QtWidgets.QLabel(self.splitter_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.craft_image.sizePolicy().hasHeightForWidth())
        self.craft_image.setSizePolicy(sizePolicy)
        self.craft_image.setMinimumSize(QtCore.QSize(320, 300))
        self.craft_image.setMaximumSize(QtCore.QSize(320, 300))
        self.craft_image.setStyleSheet("")
        self.craft_image.setFrameShape(QtWidgets.QFrame.Box)
        self.craft_image.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.craft_image.setText("")
        self.craft_image.setObjectName("craft_image")
        self.label_5 = QtWidgets.QLabel(self.splitter_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(320, 30))
        self.label_5.setMaximumSize(QtCore.QSize(320, 30))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.splitter_3, 0, 2, 1, 1)
        self.splitter_2 = QtWidgets.QSplitter(self.images)
        self.splitter_2.setMinimumSize(QtCore.QSize(320, 330))
        self.splitter_2.setMaximumSize(QtCore.QSize(320, 337))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.SEM_image = QtWidgets.QLabel(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SEM_image.sizePolicy().hasHeightForWidth())
        self.SEM_image.setSizePolicy(sizePolicy)
        self.SEM_image.setMinimumSize(QtCore.QSize(320, 300))
        self.SEM_image.setMaximumSize(QtCore.QSize(320, 300))
        self.SEM_image.setAcceptDrops(False)
        self.SEM_image.setStyleSheet("")
        self.SEM_image.setFrameShape(QtWidgets.QFrame.Box)
        self.SEM_image.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.SEM_image.setText("")
        self.SEM_image.setScaledContents(False)
        self.SEM_image.setObjectName("SEM_image")
        self.label_4 = QtWidgets.QLabel(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(320, 30))
        self.label_4.setMaximumSize(QtCore.QSize(320, 30))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.splitter_2, 0, 0, 1, 1)
        self.splitter_4 = QtWidgets.QSplitter(self.images)
        self.splitter_4.setMinimumSize(QtCore.QSize(320, 330))
        self.splitter_4.setMaximumSize(QtCore.QSize(320, 337))
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setObjectName("splitter_4")
        self.force_image = QtWidgets.QLabel(self.splitter_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.force_image.sizePolicy().hasHeightForWidth())
        self.force_image.setSizePolicy(sizePolicy)
        self.force_image.setMinimumSize(QtCore.QSize(320, 300))
        self.force_image.setMaximumSize(QtCore.QSize(320, 300))
        self.force_image.setFrameShape(QtWidgets.QFrame.Box)
        self.force_image.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.force_image.setText("")
        self.force_image.setObjectName("force_image")
        self.label_6 = QtWidgets.QLabel(self.splitter_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(320, 30))
        self.label_6.setMaximumSize(QtCore.QSize(320, 30))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.splitter_4, 1, 0, 1, 1)
        self.horizontalLayout.addWidget(self.images)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setMinimumSize(QtCore.QSize(300, 780))
        self.widget_2.setMaximumSize(QtCore.QSize(300, 780))
        self.widget_2.setStyleSheet("QWidget #widget_2 {\n"
"    border-width: 5px; \n"
"    border-style: solid;\n"
"    border-color: #00afb9;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: 1px solid white;\n"
"    border-radius: 10px;\n"
"    background-color: #f5f3f4;\n"
"    color: #161a1d;\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMinimumSize(QtCore.QSize(275, 100))
        self.listWidget.setMaximumSize(QtCore.QSize(275, 100))
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.info = QtWidgets.QWidget(self.widget_2)
        self.info.setMinimumSize(QtCore.QSize(275, 330))
        self.info.setMaximumSize(QtCore.QSize(275, 330))
        self.info.setStyleSheet("QWidget #info {\n"
"    border-width: 3px; \n"
"    border-style: solid;\n"
"    border-color: #00afb9;\n"
"    border-radius: 15px;\n"
"}")
        self.info.setObjectName("info")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.info)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_16 = QtWidgets.QLabel(self.info)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_3.addWidget(self.label_16)
        self.splitter_10 = QtWidgets.QSplitter(self.info)
        self.splitter_10.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_10.setObjectName("splitter_10")
        self.label_2 = QtWidgets.QLabel(self.splitter_10)
        self.label_2.setMinimumSize(QtCore.QSize(75, 25))
        self.label_2.setMaximumSize(QtCore.QSize(75, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.temp_info = QtWidgets.QLineEdit(self.splitter_10)
        self.temp_info.setMinimumSize(QtCore.QSize(170, 25))
        self.temp_info.setMaximumSize(QtCore.QSize(170, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.temp_info.setFont(font)
        self.temp_info.setText("")
        self.temp_info.setObjectName("temp_info")
        self.verticalLayout_3.addWidget(self.splitter_10)
        self.splitter_11 = QtWidgets.QSplitter(self.info)
        self.splitter_11.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_11.setObjectName("splitter_11")
        self.label_3 = QtWidgets.QLabel(self.splitter_11)
        self.label_3.setMinimumSize(QtCore.QSize(75, 25))
        self.label_3.setMaximumSize(QtCore.QSize(75, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.time_info = QtWidgets.QLineEdit(self.splitter_11)
        self.time_info.setMinimumSize(QtCore.QSize(170, 25))
        self.time_info.setMaximumSize(QtCore.QSize(170, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.time_info.setFont(font)
        self.time_info.setText("")
        self.time_info.setObjectName("time_info")
        self.verticalLayout_3.addWidget(self.splitter_11)
        self.splitter_12 = QtWidgets.QSplitter(self.info)
        self.splitter_12.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_12.setObjectName("splitter_12")
        self.label_7 = QtWidgets.QLabel(self.splitter_12)
        self.label_7.setMinimumSize(QtCore.QSize(75, 25))
        self.label_7.setMaximumSize(QtCore.QSize(75, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.craft_info = QtWidgets.QLineEdit(self.splitter_12)
        self.craft_info.setMinimumSize(QtCore.QSize(170, 25))
        self.craft_info.setMaximumSize(QtCore.QSize(170, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.craft_info.setFont(font)
        self.craft_info.setObjectName("craft_info")
        self.verticalLayout_3.addWidget(self.splitter_12)
        self.splitter_13 = QtWidgets.QSplitter(self.info)
        self.splitter_13.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_13.setObjectName("splitter_13")
        self.label_13 = QtWidgets.QLabel(self.splitter_13)
        self.label_13.setMinimumSize(QtCore.QSize(75, 25))
        self.label_13.setMaximumSize(QtCore.QSize(75, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.amp_info = QtWidgets.QLineEdit(self.splitter_13)
        self.amp_info.setMinimumSize(QtCore.QSize(170, 25))
        self.amp_info.setMaximumSize(QtCore.QSize(170, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.amp_info.setFont(font)
        self.amp_info.setObjectName("amp_info")
        self.verticalLayout_3.addWidget(self.splitter_13)
        self.splitter_14 = QtWidgets.QSplitter(self.info)
        self.splitter_14.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_14.setObjectName("splitter_14")
        self.label_14 = QtWidgets.QLabel(self.splitter_14)
        self.label_14.setMinimumSize(QtCore.QSize(75, 25))
        self.label_14.setMaximumSize(QtCore.QSize(75, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.metal_info = QtWidgets.QLineEdit(self.splitter_14)
        self.metal_info.setMinimumSize(QtCore.QSize(170, 25))
        self.metal_info.setMaximumSize(QtCore.QSize(170, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.metal_info.setFont(font)
        self.metal_info.setObjectName("metal_info")
        self.verticalLayout_3.addWidget(self.splitter_14)
        self.splitter_15 = QtWidgets.QSplitter(self.info)
        self.splitter_15.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_15.setObjectName("splitter_15")
        self.label_15 = QtWidgets.QLabel(self.splitter_15)
        self.label_15.setMinimumSize(QtCore.QSize(75, 25))
        self.label_15.setMaximumSize(QtCore.QSize(75, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.no_info = QtWidgets.QLineEdit(self.splitter_15)
        self.no_info.setMinimumSize(QtCore.QSize(170, 25))
        self.no_info.setMaximumSize(QtCore.QSize(170, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.no_info.setFont(font)
        self.no_info.setObjectName("no_info")
        self.verticalLayout_3.addWidget(self.splitter_15)
        self.splitter = QtWidgets.QSplitter(self.info)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label_17 = QtWidgets.QLabel(self.splitter)
        self.label_17.setMinimumSize(QtCore.QSize(75, 25))
        self.label_17.setMaximumSize(QtCore.QSize(75, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.content_info = QtWidgets.QLineEdit(self.splitter)
        self.content_info.setMinimumSize(QtCore.QSize(170, 25))
        self.content_info.setMaximumSize(QtCore.QSize(170, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.content_info.setFont(font)
        self.content_info.setText("")
        self.content_info.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.content_info.setObjectName("content_info")
        self.verticalLayout_3.addWidget(self.splitter)
        self.splitter_17 = QtWidgets.QSplitter(self.info)
        self.splitter_17.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_17.setObjectName("splitter_17")
        self.label_18 = QtWidgets.QLabel(self.splitter_17)
        self.label_18.setMinimumSize(QtCore.QSize(75, 25))
        self.label_18.setMaximumSize(QtCore.QSize(75, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.update_info = QtWidgets.QLineEdit(self.splitter_17)
        self.update_info.setMinimumSize(QtCore.QSize(170, 25))
        self.update_info.setMaximumSize(QtCore.QSize(170, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.update_info.setFont(font)
        self.update_info.setObjectName("update_info")
        self.verticalLayout_3.addWidget(self.splitter_17)
        self.verticalLayout.addWidget(self.info)
        self.search_input = QtWidgets.QWidget(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_input.sizePolicy().hasHeightForWidth())
        self.search_input.setSizePolicy(sizePolicy)
        self.search_input.setMinimumSize(QtCore.QSize(275, 190))
        self.search_input.setMaximumSize(QtCore.QSize(275, 190))
        self.search_input.setObjectName("search_input")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.search_input)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter_16 = QtWidgets.QSplitter(self.search_input)
        self.splitter_16.setMinimumSize(QtCore.QSize(240, 0))
        self.splitter_16.setMaximumSize(QtCore.QSize(228, 25))
        self.splitter_16.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_16.setObjectName("splitter_16")
        self.label = QtWidgets.QLabel(self.splitter_16)
        self.label.setMinimumSize(QtCore.QSize(165, 25))
        self.label.setMaximumSize(QtCore.QSize(165, 25))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.resetImage = QtWidgets.QPushButton(self.splitter_16)
        self.resetImage.setMinimumSize(QtCore.QSize(56, 23))
        self.resetImage.setMaximumSize(QtCore.QSize(56, 23))
        self.resetImage.setObjectName("resetImage")
        self.verticalLayout_2.addWidget(self.splitter_16)
        self.splitter_6 = QtWidgets.QSplitter(self.search_input)
        self.splitter_6.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_6.setObjectName("splitter_6")
        self.label_9 = QtWidgets.QLabel(self.splitter_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QtCore.QSize(56, 25))
        self.label_9.setMaximumSize(QtCore.QSize(56, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.temp = QtWidgets.QLineEdit(self.splitter_6)
        self.temp.setMinimumSize(QtCore.QSize(0, 25))
        self.temp.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.temp.setFont(font)
        self.temp.setObjectName("temp")
        self.verticalLayout_2.addWidget(self.splitter_6)
        self.splitter_7 = QtWidgets.QSplitter(self.search_input)
        self.splitter_7.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_7.setObjectName("splitter_7")
        self.label_10 = QtWidgets.QLabel(self.splitter_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QtCore.QSize(56, 25))
        self.label_10.setMaximumSize(QtCore.QSize(56, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.time = QtWidgets.QLineEdit(self.splitter_7)
        self.time.setMinimumSize(QtCore.QSize(0, 25))
        self.time.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.time.setFont(font)
        self.time.setObjectName("time")
        self.verticalLayout_2.addWidget(self.splitter_7)
        self.splitter_8 = QtWidgets.QSplitter(self.search_input)
        self.splitter_8.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_8.setObjectName("splitter_8")
        self.label_11 = QtWidgets.QLabel(self.splitter_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QtCore.QSize(56, 25))
        self.label_11.setMaximumSize(QtCore.QSize(56, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.crafts = QtWidgets.QLineEdit(self.splitter_8)
        self.crafts.setMinimumSize(QtCore.QSize(0, 25))
        self.crafts.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.crafts.setFont(font)
        self.crafts.setText("")
        self.crafts.setObjectName("crafts")
        self.verticalLayout_2.addWidget(self.splitter_8)
        self.splitter_9 = QtWidgets.QSplitter(self.search_input)
        self.splitter_9.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_9.setObjectName("splitter_9")
        self.label_12 = QtWidgets.QLabel(self.splitter_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMinimumSize(QtCore.QSize(56, 25))
        self.label_12.setMaximumSize(QtCore.QSize(56, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.amp_factor = QtWidgets.QLineEdit(self.splitter_9)
        self.amp_factor.setMinimumSize(QtCore.QSize(0, 25))
        self.amp_factor.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.amp_factor.setFont(font)
        self.amp_factor.setObjectName("amp_factor")
        self.verticalLayout_2.addWidget(self.splitter_9)
        self.verticalLayout.addWidget(self.search_input)
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setMinimumSize(QtCore.QSize(275, 80))
        self.widget_4.setMaximumSize(QtCore.QSize(275, 80))
        self.widget_4.setStyleSheet("QPushButton {\n"
"    border: 1px solid white;\n"
"    border-radius: 10px;\n"
"    background-color: #f5f3f4;\n"
"    color: #161a1d;\n"
"}")
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.deleteImage = QtWidgets.QPushButton(self.widget_4)
        self.deleteImage.setMinimumSize(QtCore.QSize(75, 0))
        self.deleteImage.setMaximumSize(QtCore.QSize(75, 16777215))
        self.deleteImage.setObjectName("deleteImage")
        self.gridLayout_2.addWidget(self.deleteImage, 0, 2, 1, 1)
        self.searchImage = QtWidgets.QPushButton(self.widget_4)
        self.searchImage.setMinimumSize(QtCore.QSize(75, 0))
        self.searchImage.setMaximumSize(QtCore.QSize(75, 16777215))
        self.searchImage.setObjectName("searchImage")
        self.gridLayout_2.addWidget(self.searchImage, 0, 0, 1, 1)
        self.insertImage = QtWidgets.QPushButton(self.widget_4)
        self.insertImage.setMinimumSize(QtCore.QSize(75, 0))
        self.insertImage.setMaximumSize(QtCore.QSize(75, 16777215))
        self.insertImage.setObjectName("insertImage")
        self.gridLayout_2.addWidget(self.insertImage, 3, 0, 1, 1)
        self.modifyImage = QtWidgets.QPushButton(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modifyImage.sizePolicy().hasHeightForWidth())
        self.modifyImage.setSizePolicy(sizePolicy)
        self.modifyImage.setMinimumSize(QtCore.QSize(75, 0))
        self.modifyImage.setMaximumSize(QtCore.QSize(75, 16777215))
        self.modifyImage.setObjectName("modifyImage")
        self.gridLayout_2.addWidget(self.modifyImage, 3, 2, 1, 1)
        self.verticalLayout.addWidget(self.widget_4)
        self.horizontalLayout.addWidget(self.widget_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_8.setText(_translate("MainWindow", "??????????????????"))
        self.label_5.setText(_translate("MainWindow", "????????????"))
        self.label_4.setText(_translate("MainWindow", "SEM??????"))
        self.label_6.setText(_translate("MainWindow", "????????????"))
        self.label_16.setText(_translate("MainWindow", "???????????????"))
        self.label_2.setText(_translate("MainWindow", "??????(??C)"))
        self.label_3.setText(_translate("MainWindow", "??????(s)"))
        self.label_7.setText(_translate("MainWindow", "??????"))
        self.label_13.setText(_translate("MainWindow", "????????????"))
        self.label_14.setText(_translate("MainWindow", "??????"))
        self.label_15.setText(_translate("MainWindow", "??????"))
        self.label_17.setText(_translate("MainWindow", "????????????"))
        self.label_18.setText(_translate("MainWindow", "??????????????????"))
        self.label.setText(_translate("MainWindow", "????????????????????????????????????:"))
        self.resetImage.setText(_translate("MainWindow", "??????"))
        self.label_9.setText(_translate("MainWindow", "??????(??C)"))
        self.temp.setPlaceholderText(_translate("MainWindow", "e.g. 200"))
        self.label_10.setText(_translate("MainWindow", "??????(s)"))
        self.time.setPlaceholderText(_translate("MainWindow", "e.g. 30"))
        self.label_11.setText(_translate("MainWindow", "??????"))
        self.crafts.setPlaceholderText(_translate("MainWindow", "e.g. ??????"))
        self.label_12.setText(_translate("MainWindow", "????????????"))
        self.amp_factor.setPlaceholderText(_translate("MainWindow", "e.g. 1000"))
        self.deleteImage.setText(_translate("MainWindow", "??????"))
        self.searchImage.setText(_translate("MainWindow", "??????"))
        self.insertImage.setText(_translate("MainWindow", "??????"))
        self.modifyImage.setText(_translate("MainWindow", "??????"))
