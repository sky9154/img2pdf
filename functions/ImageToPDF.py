from PySide6 import QtWidgets, QtGui, QtCore
from PIL import Image
from os.path import join, basename
from os import listdir
from tqdm import tqdm


class ImageToPDF:
  def __init__(self, app) -> None:
    self.app = app
    self.upload_path = QtCore.QDir.homePath() + '/Downloads'
    self.export_path = QtCore.QDir.homePath() + '/Desktop'

  def upload(self) -> None:
    file_dialog = QtWidgets.QFileDialog()
    file_dialog.setWindowTitle('選擇資料夾')
    file_dialog.setFileMode(QtWidgets.QFileDialog.Directory)
    file_dialog.setDirectory(self.upload_path)

    if file_dialog.exec():
      folders = file_dialog.selectedFiles()
      self.upload_path = folders[0] if folders else self.upload_path

  def export(self) -> None:
    file_dialog = QtWidgets.QFileDialog()
    file_dialog.setWindowTitle('選擇儲存位置')
    file_dialog.setFileMode(QtWidgets.QFileDialog.Directory)
    file_dialog.setDirectory(self.export_path)

    if file_dialog.exec():
      folders = file_dialog.selectedFiles()
      self.export_path = folders[0] if folders else self.export_path

  def loading(self):
    QtWidgets.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))

  def finish(self):
    QtWidgets.QApplication.restoreOverrideCursor()
    self.app.message_label.setText('轉換完成！')

  def img2pdf(self) -> None:
    name = basename(self.upload_path)
    pdf_path = join(self.export_path, f'{name}.pdf')

    image_list = []

    self.loading()

    for image in listdir(self.upload_path):
      try:
        if Image.open(join(self.upload_path, image)):
          image_list.append(join(self.upload_path, image))
      except Exception:
        pass

    sources = [Image.open(file).convert('RGB') for file in tqdm(image_list, desc=name)]
    sources[0].save(pdf_path, 'pdf', save_all=True, append_images=sources[1:])

    self.finish()