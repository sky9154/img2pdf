import importlib.resources as resources
from PySide6.QtCore import QSize, QDir, Signal
from PySide6.QtGui import QPixmap, QIcon, QDragEnterEvent, QDropEvent
from PySide6.QtWidgets import QPushButton, QSizePolicy, QFileDialog
from os.path import isdir, join
from functions import Config
from assets import images


class UploadButton(QPushButton):
  folder_path_changed = Signal(str)

  def __init__(self):
    super().__init__()

    self.config = Config()

    with resources.as_file(resources.files(images) /
                           'upload.png') as upload_path:
      self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
      self.setStyleSheet('background-color: transparent;')
      self.setIcon(QIcon(QPixmap(str(upload_path))))
      self.setIconSize(QSize(150, 150))
      self.setAcceptDrops(True)
      self.clicked.connect(self.open_folder_dialog)

  def open_folder_dialog(self):
    upload_path = join(QDir.homePath(), 'Downloads')
    folder_path = QFileDialog.getExistingDirectory(
        self, self.config['WIDGET']['DIALOG']['PDF'], upload_path)

    if isdir(folder_path):
      self.folder_path_changed.emit(folder_path)

  def dragEnterEvent(self, event: QDragEnterEvent):
    if event.mimeData().hasUrls():
      for url in event.mimeData().urls():
        if isdir(url.toLocalFile()):
          event.acceptProposedAction()

          return

    event.ignore()

  def dropEvent(self, event: QDropEvent):
    for url in event.mimeData().urls():
      folder_path = url.toLocalFile()

      if isdir(folder_path):
        self.folder_path_changed.emit(folder_path)

        break
