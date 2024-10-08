from PySide6 import QtWidgets, QtGui, QtCore
from PyPDF2 import PdfReader, PdfWriter
from PIL import Image
from os.path import join, basename
from os import listdir


class ImageToPDF:
  def __init__(self, app) -> None:
    self.app = app
    self.upload_path = QtCore.QDir.homePath() + '/Downloads'
    self.export_path = QtCore.QDir.homePath() + '/Desktop'

  def upload(self) -> None:
    file_dialog = QtWidgets.QFileDialog()
    file_dialog.setWindowTitle('Choose PDF folder')
    file_dialog.setFileMode(QtWidgets.QFileDialog.Directory)
    file_dialog.setDirectory(self.upload_path)

    if file_dialog.exec():
      folders = file_dialog.selectedFiles()
      self.upload_path = folders[0] if folders else self.upload_path

  def export(self) -> None:
    file_dialog = QtWidgets.QFileDialog()
    file_dialog.setWindowTitle('Choose storage location')
    file_dialog.setFileMode(QtWidgets.QFileDialog.Directory)
    file_dialog.setDirectory(self.export_path)

    if file_dialog.exec():
      folders = file_dialog.selectedFiles()
      self.export_path = folders[0] if folders else self.export_path

  def loading(self):
    QtWidgets.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))

  def finish(self):
    QtWidgets.QApplication.restoreOverrideCursor()
    self.app.message_label.setText('Conversion completed!')

  def img2pdf(self) -> None:
    name = basename(self.upload_path)
    pdf_path = join(self.export_path, f'{name}.pdf')

    image_list = []

    self.loading()

    images = listdir(self.upload_path)

    if '(' in images[0] or ')' in images[0]:
      images = sorted(images, key=lambda x: int(x.split('(')[1].split(')')[0]))

    for image in images:
      try:
        if Image.open(join(self.upload_path, image)):

          image_list.append(join(self.upload_path, image))
      except Exception:
        pass

    sources = [Image.open(file).convert('RGB') for file in image_list]
    sources[0].save(pdf_path, 'pdf', save_all=True, append_images=sources[1:])

    if ' - ' in name:
      reader = PdfReader(pdf_path)
      writer = PdfWriter()

      author = name.split(' - ')[0]

      for page in reader.pages:
        writer.add_page(page)

      writer.add_metadata({ '/Author': author })

      with open(pdf_path, 'wb') as pdf:
        writer.write(pdf)

    self.finish()