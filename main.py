import sys
from PyQt5.QtWidgets import (
  QApplication, QLabel, QMainWindow,
  QVBoxLayout, QWidget, QPushButton,
  QFileDialog
)
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtCore import Qt, QDir
from functions.img2pdf import img2pdf


class App(QMainWindow):
  def __init__(self):
    super().__init__()
    self.init()

  def init(self):
    central_widget = QWidget(self)
    self.setCentralWidget(central_widget)
    self.setFixedSize(400, 200)
    self.setWindowIcon(QIcon('images/icon.ico'))

    layout = QVBoxLayout(central_widget)

    self.label = QLabel(self)
    self.label.setAlignment(Qt.AlignCenter)

    self.button = QPushButton('', self)
    self.button.setFixedSize(150, 150)
    self.button.setCursor(Qt.PointingHandCursor)
    self.button.clicked.connect(self.show_dialog)
    self.button.setIcon(QIcon('images/upload.png'))
    self.button.setIconSize(self.button.size())
    self.button.setStyleSheet('background-color: transparent;')

    h_layout = QVBoxLayout()
    h_layout.addWidget(self.button, alignment=Qt.AlignHCenter)
    h_layout.addStretch(1)

    layout.addWidget(self.label)
    layout.addLayout(h_layout)

    self.setWindowTitle('圖片轉 PDF')
    self.setGeometry(300, 300, 400, 200)

  def set_loading_cursor(self):
    QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))

  def restore_default_cursor(self):
    QApplication.restoreOverrideCursor()

  def show_dialog(self):
    default_path = QDir.homePath() + '/Downloads'
    save_path = QDir.homePath() + '/Desktop'
    folder_path = QFileDialog.getExistingDirectory(self, '選擇資料夾', default_path)

    if folder_path:
      self.set_loading_cursor()
      img2pdf(self, folder_path, save_path)
      self.restore_default_cursor()
      self.label.setText('轉換完成！')

    self.setWindowTitle('圖片轉 PDF')

if __name__ == '__main__':
  app = QApplication(sys.argv)

  window = App()
  window.show()

  sys.exit(app.exec_())