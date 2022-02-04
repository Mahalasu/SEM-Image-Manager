from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton

from Database import Database
from InsertPanel import InsertPanel
from MainPanel import MainPanel
import sys

# construct windows
from ModifyPanel import ModifyPanel
from SecondPanel import SecondPanel

app = QtWidgets.QApplication(sys.argv)
database = Database()
main_panel = MainPanel(database)
# second_panel = SecondPanel(database)


# slots
def show_insert_panel():
    insert_panel = InsertPanel(database.get_all_rows_from_metallographic(), database)
    insert_panel.exec_()
    main_panel.init_list_widget(main_panel.list_widget)


def show_modify_panel():
    image_info = main_panel.fetch_info()
    modify_panel = ModifyPanel(database.get_all_rows_from_metallographic(), database, image_info)
    modify_panel.exec_()
    main_panel.init_list_widget(main_panel.list_widget)


# slots connect with signals
main_panel.findChild(QPushButton, 'insertImage').clicked.connect(show_insert_panel)
main_panel.findChild(QPushButton, 'modifyImage').clicked.connect(show_modify_panel)

if __name__ == "__main__":
    sem_image_manager = main_panel
    sem_image_manager.show()
    sys.exit(app.exec_())
