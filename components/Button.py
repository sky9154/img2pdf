from PySide6 import QtWidgets, QtCore, QtGui


class UploadButton(QtWidgets.QPushButton):
  def __init__(self):
    super().__init__()

    image = QtGui.QPixmap('assets/images/upload.png')

    self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
    self.setStyleSheet('background-color: transparent;')
    self.setIcon(QtGui.QIcon(image))
    self.setIconSize(QtCore.QSize(150, 150))