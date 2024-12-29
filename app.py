import importlib.resources as resources
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QCursor
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from widgets import UploadButton
from functions import ImageToPDF, Config
from assets import images


class MainWindow(QMainWindow):

  def __init__(self):
    super().__init__()

    config = Config()

    with resources.as_file(resources.files(images) / 'icon.ico') as icon_path:
      self.setWindowTitle(config['WINDOW']['APP_NAME'])
      self.setFixedSize(config['WINDOW']['WIDTH'], config['WINDOW']['HEIGHT'])
      self.setWindowIcon(QIcon(str(icon_path)))
      self.setWindowFlag(Qt.WindowStaysOnTopHint)
      self.setGeometry(300, 300, 400, 200)


    main_widget = QWidget()

    main_layout = QVBoxLayout(main_widget)
    self.upload_button = UploadButton()
    self.upload_button.folder_path_changed.connect(self.folder_path_changed)

    main_layout.addWidget(self.upload_button)
    QApplication.setOverrideCursor(QCursor(Qt.PointingHandCursor))

    self.setCentralWidget(main_widget)

  def folder_path_changed(self, folder_path):
    img2pdf = ImageToPDF(self, folder_path)
    img2pdf.export()
    img2pdf.img2pdf()


if __name__ == '__main__':
  config = Config()

  app = QApplication([])
  app.setStyle(config['WINDOW']['STYLE'])

  window = MainWindow()

  window.show()
  app.exec()
