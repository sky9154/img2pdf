import sys
import json
from PySide6 import QtWidgets, QtGui
from components import Label, Button
from functions.ImageToPDF import ImageToPDF


with open('assets/data/config.json', 'r') as config_json:
  config = json.load(config_json)

application = config.get('application')

class App(QtWidgets.QMainWindow):
  def __init__(self):
    super().__init__()

    self.setWindowTitle(application['name'])
    self.setFixedSize(application['size']['width'], application['size']['height'])
    self.setWindowIcon(QtGui.QIcon(application['icon']))
    self.setGeometry(300, 300, 400, 200)

    self.main_widget = QtWidgets.QWidget()
    self.setCentralWidget(self.main_widget)

    self.main_layout = QtWidgets.QVBoxLayout(self.main_widget)
    self.message_label = Label.MessageLabel()
    self.upload_button = Button.UploadButton()

    self.main_layout.addWidget(self.message_label)
    self.main_layout.addWidget(self.upload_button)

    self.upload_button.clicked.connect(self.click)

  def click(self):
    img2pdf = ImageToPDF(self)
    img2pdf.upload()
    img2pdf.export()
    img2pdf.img2pdf()


if __name__ == '__main__':
  app = QtWidgets.QApplication(sys.argv)

  window = App()
  window.show()

  sys.exit(app.exec())