from PySide6 import QtWidgets, QtCore


class MessageLabel(QtWidgets.QLabel):
  def __init__(self):
    super().__init__()

    self.setAlignment(QtCore.Qt.AlignCenter)