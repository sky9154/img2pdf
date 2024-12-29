from PySide6.QtCore import QDir, Qt
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QApplication, QFileDialog, QWidget
from PyPDF2 import PdfReader, PdfWriter
from PIL import Image
from os.path import join, basename, isdir
from os import listdir
from .config import Config


class ImageToPDF(QWidget):

  def __init__(self, app, upload_path):
    super().__init__()

    self.config = Config()
    self.app = app
    self.upload_path = upload_path
    self.export_path = ''

  def export(self):
    export_path = join(QDir.homePath(), 'Desktop')
    folder_path = QFileDialog.getExistingDirectory(
        self, self.config['WIDGET']['DIALOG']['STORAGE'], export_path)

    if isdir(folder_path):
      self.export_path = folder_path

  def loading(self):
    self.app.upload_button.setEnabled(False)
    QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))

  def finish(self):
    self.app.upload_button.setEnabled(True)
    QApplication.restoreOverrideCursor()

  def img2pdf(self):
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

      writer.add_metadata({'/Author': author})

      with open(pdf_path, 'wb') as pdf:
        writer.write(pdf)

    self.finish()